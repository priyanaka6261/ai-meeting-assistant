import os
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)


def generate_meeting_summary(transcript):

    prompt = f"""
Analyze the following meeting transcript and return ONLY JSON.

Fields required:
- executive_summary
- key_decisions
- action_items
- topic_summary
- minutes_of_meeting

Transcript:
{transcript}
"""

    response = client.chat.completions.create(
        model="nvidia/nemotron-3-nano-30b-a3b:free",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=800
    )

    analysis_text = response.choices[0].message.content

    try:
        analysis_json = json.loads(analysis_text)
    except:
        analysis_json = {"analysis": analysis_text}

    return analysis_json
