import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "")

# e.g. "gemini-1.5-flash"
CHAT_MODEL_NAME = "gemini-3.5-flash-lite"

# local sentence-transformers model, no API key needed
EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
