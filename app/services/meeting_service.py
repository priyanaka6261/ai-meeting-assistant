import uuid

# In-memory storage for meetings
meetings = {}


def create_meeting(meeting_url: str):
    """
    Create a new meeting entry when bot joins.
    """

    meeting_id = str(uuid.uuid4())

    meetings[meeting_id] = {
        "meeting_url": meeting_url,
        "status": "running",
        "transcript": None,
        "summary": None
    }

    return meeting_id


def stop_meeting(meeting_id: str):
    """
    Stop the meeting bot.
    """

    if meeting_id in meetings:
        meetings[meeting_id]["status"] = "stopped"

        return {
            "meeting_id": meeting_id,
            "status": "Meeting Assistant left meeting"
        }

    return {"error": "Meeting not found"}


def save_transcript(meeting_id: str, transcript: str):
    """
    Save transcript after transcription.
    """

    if meeting_id in meetings:
        meetings[meeting_id]["transcript"] = transcript

        return {"message": "Transcript saved"}

    return {"error": "Meeting not found"}


def save_summary(meeting_id: str, summary: str):
    """
    Save AI generated summary and MOM.
    """

    if meeting_id in meetings:
        meetings[meeting_id]["summary"] = summary

        return {"message": "Summary saved"}

    return {"error": "Meeting not found"}


def get_transcript(meeting_id: str):
    """
    Retrieve transcript for a meeting.
    """

    if meeting_id in meetings:
        return {
            "meeting_id": meeting_id,
            "transcript": meetings[meeting_id]["transcript"]
        }

    return {"error": "Meeting not found"}


def get_summary(meeting_id: str):
    """
    Retrieve summary / MOM for a meeting.
    """

    if meeting_id in meetings:
        return {
            "meeting_id": meeting_id,
            "summary": meetings[meeting_id]["summary"]
        }

    return {"error": "Meeting not found"}


def delete_meeting(meeting_id: str):
    """
    Delete meeting data when requested.
    """

    if meeting_id in meetings:
        del meetings[meeting_id]

        return {"message": "Meeting data deleted"}

    return {"error": "Meeting not found"}
