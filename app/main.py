from fastapi import FastAPI
from app.api import meeting_routes
from app.api import transcription_routes
from app.api import ai_routes

app = FastAPI(title="AI Meeting Assistant")

app.include_router(meeting_routes.router)
app.include_router(transcription_routes.router)
app.include_router(ai_routes.router)


@app.get("/")
def home():
    return {"message": "AI Meeting Assistant Running"}
