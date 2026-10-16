from fastapi import APIRouter
from langchain_google_genai import ChatGoogleGenerativeAI
from schema import ChatRequest
from rag import retrieve_similar_chunks
import os

router = APIRouter()


llm = ChatGoogleGenerativeAI(google_api_key=os.getenv("GOOGLE_GEMINI_KEY"),model="gemini-3.5-flash", temperature=0)


@router.post("/chat")
async def chat(request: ChatRequest):

    full_context = retrieve_similar_chunks(request.query)
    print(full_context)

    if not full_context:
        return { "reply": "Couldnt find related data."}

    system_prompt = f"You are a helpful interview assistant. Only answer interview-related questions in short. Politely decline all unrelated queries without answering them. Respond in plain text only. Do not use Markdown, asterisks,headings, or bullet points. Use simple numbered lists if needed. CONTEXT: {full_context} "

    response = await llm.ainvoke([
    ("system",system_prompt),
    ("human", request.query)])
    

    return {"reply": response.content[0]["text"]}