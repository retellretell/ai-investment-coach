from fastapi import FastAPI

app = FastAPI(title="AI Investment Coach")

@app.get("/health")
async def health_check():
    return {"status": "ok"}

