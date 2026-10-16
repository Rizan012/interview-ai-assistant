This project is a backend for an AI-powered interview assistant that can answer questions from uploaded documents and handle interview booking requests.

### Tech Stack:
FastAPI: Backend REST APIs.
Gemini 3.5 Flash: AI responses and query understanding.
Ollama Embeddings: Text embedding generation, since its runned locally.
Qdrant: Vector storage and similarity search.
Recursive Chunking: Preferred chunking strategy based on my results.
Semantic Chunking: Alternative chunking strategy for comparison.
RAG: Context-based answers from uploaded documents.
Redis: Conversation history and session management.
PostgreSQL: Interview booking storage.
SQLAlchemy: Database interaction and ORM.

### To pull and use:
1. Clone the repository:
git clone [https://github.com/Rizan012/interview-ai-assistant](https://github.com/Rizan012/interview-ai-assistant)
cd interview-ai-assistant
2. Install dependencies:
uv sync
3. Create a .env file with your Gemini API key and Qdrant, Redis, and PostgreSQL connection details.
4. Install Ollama and download the embedding model I used:
ollama pull nomic-embed-text
(I used OllamaEmbeddings(model="nomic-embed-text") since its runned locally.)
5. Run the API:
uv run uvicorn main:app --reload
6. Open [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to test the APIs.


### Results

A. Document Upload
![Document Upload](ss/doc_upload.png)

B. Normal Text Query
![Normal Text Query](ss/query.png)

C. Booking an Interview
![Booking Interview](ss/booking.png)

D. Confirming and Completing Booking
![Booking Confirmation](ss/booking1.png)

![Booking Saved in Database](ss/db.png)

E. Redis Conversation History:
![Redis Conversation History](ss/redis.png)

F. LLM Remembers History:
![LLM Query](ss/redis_history.png)

![LLM History](ss/redis_history1.png)
