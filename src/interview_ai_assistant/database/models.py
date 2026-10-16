from datetime import date, time

from sqlalchemy import String, Date, Time
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class InterviewBooking(Base):
    __tablename__ = "interview_bookings"

    id: Mapped[int] = mapped_column(primary_key=True)

    session_id: Mapped[str] = mapped_column(String(100))
    user_name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(255))

    interview_date: Mapped[date] = mapped_column(Date)
    interview_time: Mapped[time] = mapped_column(Time)

    status: Mapped[str] = mapped_column(String(30), default="requested")