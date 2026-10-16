import os
import json
import redis
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parents[2] / ".env")

client = redis.from_url(
    os.getenv("REDIS_URL"),
    decode_responses=True,
)

def get_history(session_id: str) -> list:
    messages = client.lrange(f"chat:{session_id}", 0, -1)
    return [json.loads(message) for message in messages]

def save_message(session_id: str, role: str, content: str):
    key = f"chat:{session_id}"
    client.rpush(key, json.dumps({"role": role, "content": content}))
    client.expire(key, 1800)