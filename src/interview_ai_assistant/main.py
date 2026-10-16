from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parents[2] / ".env")

from fastapi import FastAPI
from api.document import router as document_router
from api.chat import router as chat_router

from database.database import engine
from database.models import Base, InterviewBooking

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(document_router)
app.include_router(chat_router)
