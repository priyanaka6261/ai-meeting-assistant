import whisper
import os

model = whisper.load_model("base")


def transcribe_audio(file_path):

    result = model.transcribe(file_path)

    transcript = result["text"]

    return transcript
