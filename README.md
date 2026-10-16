This project is a backend for an AI-powered interview assistant that can answer questions from uploaded documents (.pdf/.txt) and handle interview booking requests.

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

### File Description
main.py starts the FastAPI app, connects the API routes, and creates the database tables.
api/document.py handles document uploads, while api/chat.py manages chat messages, AI responses, conversation history, and interview bookings.
ingest.py extracts text from PDF and TXT files and splits it using recursive or semantic chunking.
embeddings.py sets up the Ollama embedding model, and qdrant_store.py stores document chunks and their embeddings in Qdrant.
rag.py finds relevant information from uploaded documents to help answer user questions.
redis_history.py saves and retrieves chat history using Redis.
booking.py checks the interview details and saves booking requests to PostgreSQL. booking_schema.py defines the structure of the booking information.
database/database.py manages the PostgreSQL connection, database/models.py defines the interview booking table, and database/database_schema.py provides the SQLAlchemy base for the models.
schema.py defines the format of requests sent to the chat API.
sample_files/info.txt is a sample text file that can be upload to test.

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
