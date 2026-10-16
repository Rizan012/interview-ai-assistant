from fastapi import APIRouter
from langchain_google_genai import ChatGoogleGenerativeAI
from schema import ChatRequest
from rag import retrieve_similar_chunks
from redis_history import get_history, save_message
from booking_schema import BookingIntent
from booking import save_booking
import os

router = APIRouter()


llm = ChatGoogleGenerativeAI(google_api_key=os.getenv("GOOGLE_GEMINI_KEY"), model="gemini-3.5-flash", temperature=0)


@router.post("/chat")
async def chat(request: ChatRequest):

    full_context = retrieve_similar_chunks(request.query)
    #print(full_context)

    history = get_history(request.session_id)

    system_prompt = f"You are a helpful interview assistant. Only answer interview-related questions in short. Politely decline all unrelated queries without answering them. Respond in plain text only. Do not use Markdown, asterisks, headings, or bullet points. Use simple numbered lists if needed. For bookings, collect the user's name, email, interview date, and preferred time. Ask for missing details and request confirmation before saving. Do not claim the interview is confirmed. CONTEXT: {full_context}"

    messages = [("system", system_prompt)]

    for message in history:
        role = "human" if message["role"] == "user" else "ai"
        messages.append((role, message["content"]))

    messages.append(("human", request.query))




    booking_llm = llm.with_structured_output(BookingIntent)

    try:
        details = await booking_llm.ainvoke(messages)

    except Exception:
        details = None


    if details and details.intent == "book_interview":

        if not all([
            details.user_name,
            details.email,
            details.interview_date,
            details.interview_time
        ]):
            response = await llm.ainvoke(messages)
            reply = response.content

        elif details.confirmed:
            reply = save_booking(request.session_id, details)

        else:
            reply = (
                f"Please confirm your booking details:\n"
                f"Name: {details.user_name}\n"
                f"Email: {details.email}\n"
                f"Date: {details.interview_date}\n"
                f"Time: {details.interview_time}\n"
                f"Reply yes to save this booking."
            )

    else:

        if not full_context:
            reply = "Couldnt find related data."

        else:
            response = await llm.ainvoke(messages)
            reply = response.content[0]["text"]


    save_message(request.session_id, "user", request.query)
    save_message(request.session_id, "assistant", reply)

    return {"reply": reply}