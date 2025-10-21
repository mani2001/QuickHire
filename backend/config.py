import os
from dotenv import load_dotenv
from pathlib import Path

ENV_PATH = Path(__file__).parent / ".env"
load_dotenv()

MONGO_URI = os.getenv("MONGO_URI","")
MONGO_DB = os.getenv("MONGO_DB","quickhire")
if not MONGO_URI:
    raise RuntimeError(f"MONGO_URI is empty. Expected .env at: {ENV_PATH}")

# Comma-separated list of CORS
# CORS Origins (comma-separated in .env)
ALLOWED_ORIGINS = [
    origin.strip()
    for origin in os.getenv("ALLOWED_ORIGINS", "http://localhost:5173").split(",")
    if origin.strip()
]




