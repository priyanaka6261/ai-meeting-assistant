from fastapi import APIRouter
from app.services.ai_service import generate_meeting_summary

router = APIRouter()


@router.post("/analyze-meeting")
def analyze_meeting(transcript: str):

    result = generate_meeting_summary(transcript)

    return {"analysis": result}
