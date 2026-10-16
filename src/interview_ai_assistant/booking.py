import re
from datetime import date, time

from database.database import SessionLocal
from database.models import InterviewBooking
from booking_schema import BookingIntent

def save_booking(session_id: str, details: BookingIntent) -> str:

    if not all([
        details.user_name,
        details.email,
        details.interview_date,
        details.interview_time
    ]):
        return "Provide full details: name, email, interview date, and preferred time."


    if not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", details.email):
        return "Provide a valid email address."


    try:
        interview_date = date.fromisoformat(details.interview_date)
        interview_time = time.fromisoformat(details.interview_time)

    except ValueError:
        return "Provide a valid date and time."


    try:
        with SessionLocal() as session:

            booking = InterviewBooking(
                session_id=session_id,
                user_name=details.user_name,
                email=details.email,
                interview_date=interview_date,
                interview_time=interview_time,
                status="requested"
            )

            session.add(booking)
            session.commit()
            session.refresh(booking)

            return f"Booking request saved, id: {booking.id}"


    except Exception as e:
        print("Booking error:", repr(e))
        return "Sorry, Couldn't save booking."