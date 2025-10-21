from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .config import ALLOWED_ORIGINS
from . import db
app = FastAPI(title="QuickHire API",version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def on_startup():
    _ = db.get_db()

@app.on_event("shutdown")
def on_shutdown():
    db.close()

@app.get("/health")
def health_check():
    return {"status": "OK","message": "QuickHire backend is running"}

@app.get("/db-health")
def db_health():
    ok = db.ping()
    return {"mongo":"up" if ok else "down"}
