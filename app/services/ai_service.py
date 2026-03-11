import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)


def generate_meeting_summary(transcript):

    prompt = f"""
You are an AI meeting assistant.

From the transcript generate:
1. Executive Summary
2. Key Decisions
3. Action Items
4. Topic-wise Summary
5. Minutes of Meeting

Transcript:
{transcript}
"""

    response = client.chat.completions.create(
        model="nvidia/nemotron-3-nano-30b-a3b:free",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=800
    )

    return response.choices[0].message.content
