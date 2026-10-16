from typing import Literal
from pydantic import BaseModel, Field


class BookingIntent(BaseModel):
    intent: Literal["book_interview", "question"] = Field(
        description="Whether the latest user message requests or continues booking an interview, or asks a general question."
    )
    user_name: str | None = None
    email: str | None = None
    interview_date: str | None = None
    interview_time: str | None = None