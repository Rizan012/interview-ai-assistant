import os
from pathlib import Path
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


load_dotenv(Path(__file__).resolve().parents[2] / ".env")


engine = create_engine(os.getenv("DATABASE_URL"))

SessionLocal = sessionmaker(bind=engine)