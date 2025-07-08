# backend/main.py

from fastapi import FastAPI
from backend.ai.control_layer import router as ai_router
from backend.telegram.bot import router as telegram_router

app = FastAPI()

app.include_router(ai_router)
app.include_router(telegram_router)

@app.get("/")
def root():
    return {"message": "AutoDrop AI Backend Live ✅"}
