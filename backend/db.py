# backend/db.py
from typing import Optional
from pymongo import MongoClient
from pymongo.errors import PyMongoError
from .config import MONGO_URI, MONGO_DB

_client: Optional[MongoClient] = None

def get_client() -> MongoClient:
    global _client
    if _client is None:
        _client = MongoClient(
            MONGO_URI,
            serverSelectionTimeoutMS=5000,
            connectTimeoutMS=5000,
            socketTimeoutMS=5000,
            tls=True if "mongodb+srv://" in MONGO_URI else False,
        )
    return _client

def get_db():
    return get_client()[MONGO_DB]

def ping() -> bool:
    try:
        get_client().admin.command("ping")
        return True
    except PyMongoError:
        return False

def close():
    global _client
    if _client is not None:
        _client.close()
        _client = None
