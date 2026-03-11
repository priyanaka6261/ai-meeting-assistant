from fastapi import APIRouter
from app.services.meeting_service import (
    create_meeting,
    stop_meeting,
    get_transcript,
    get_summary,
    delete_meeting
)

router = APIRouter()


@router.post("/meeting/join")
def join_meeting(meeting_url: str):
    """
    Initiate bot to join a meeting.
    """

    meeting_id = create_meeting(meeting_url)

    return {
        "meeting_id": meeting_id,
        "status": "Meeting Assistant joined meeting"
    }


@router.post("/meeting/stop/{meeting_id}")
def stop(meeting_id: str):
    """
    Stop or remove meeting bot.
    """

    return stop_meeting(meeting_id)


@router.get("/transcript/{meeting_id}")
def transcript(meeting_id: str):
    """
    Retrieve transcript for a meeting.
    """

    return get_transcript(meeting_id)


@router.get("/summary/{meeting_id}")
def summary(meeting_id: str):
    """
    Retrieve summary and MOM for a meeting.
    """

    return get_summary(meeting_id)


@router.delete("/meeting/{meeting_id}")
def delete(meeting_id: str):
    """
    Delete meeting data when requested.
    """

    return delete_meeting(meeting_id)
