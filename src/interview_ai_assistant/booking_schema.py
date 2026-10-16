from pydantic import BaseModel
from typing import Literal


class BookingIntent(BaseModel):
    intent: Literal["book_interview", "question"]
    user_name: str | None = None
    email: str | None = None
    interview_date: str | None = None
    interview_time: str | None = None

    confirmed: bool = False