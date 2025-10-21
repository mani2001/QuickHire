from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "OK","message": "QuickHire backend is running"}

    