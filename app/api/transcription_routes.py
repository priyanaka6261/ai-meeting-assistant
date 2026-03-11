from fastapi import APIRouter, UploadFile, File
import shutil
import os
from app.services.transcription_service import transcribe_audio

router = APIRouter()

UPLOAD_FOLDER = "recordings"


@router.post("/transcribe")
async def transcribe(file: UploadFile = File(...)):

    print("Request received")

    os.makedirs(UPLOAD_FOLDER, exist_ok=True)

    filename = file.filename.replace(
        " ", "_").replace("(", "").replace(")", "")

    file_path = os.path.join(UPLOAD_FOLDER, filename)

    print("Saving file:", file_path)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    print("File saved. Starting transcription...")

    transcript = transcribe_audio(file_path)

    print("Transcription completed")

    return {
        "transcript": transcript
    }
