
---

# AI Meeting Assistant

## Overview

This project implements an **AI-powered meeting assistant backend** that can join meetings, process recorded meeting audio, generate transcripts, and produce structured meeting summaries including Minutes of Meeting (MOM).

The system uses **speech recognition and large language models** to analyze discussions and extract key insights such as decisions and action items.

---

# Architecture

System pipeline:

```
Meeting Link
      ↓
Meeting Bot API (Join / Leave)
      ↓
Audio Recording Upload
      ↓
Speech Recognition (Whisper)
      ↓
Transcript
      ↓
LLM Analysis (Nemotron via OpenRouter)
      ↓
Executive Summary
Decisions
Action Items
Minutes of Meeting
```

### Components

| Component          | Technology            |
| ------------------ | --------------------- |
| Backend            | FastAPI               |
| Speech Recognition | Whisper               |
| AI Analysis        | Nemotron (OpenRouter) |
| API Docs           | Swagger               |

---

# Setup Instructions

## 1 Install Python

Python version required:

```
Python 3.9+
```

---

## 2 Clone Project

```
git clone <repository-url>
cd meeting-ai-assistant
```

---

## 3 Create Virtual Environment

```
python -m venv venv
```

Activate:

Windows

```
venv\Scripts\activate
```

Mac/Linux

```
source venv/bin/activate
```

---

## 4 Install Dependencies

```
pip install fastapi uvicorn openai python-multipart
pip install openai-whisper
```

---

## 5 Start Server

```
uvicorn app.main:app --reload
```

Server runs at:

```
http://127.0.0.1:8000
```

API documentation:

```
http://127.0.0.1:8000/docs
```

---

# API Documentation

## Join Meeting

```
POST /meeting/join
```

Example request

```
meeting_url=https://meet.google.com/test123
```

Response

```
{
 "meeting_id": "1234-abcd",
 "status": "Meeting Assistant joined meeting"
}
```

---

## Stop Meeting

```
POST /meeting/stop/{meeting_id}
```

Example

```
POST /meeting/stop/1234-abcd
```

---

## Upload Audio for Transcription

```
POST /transcribe
```

Upload:

```
audio file (.mp3 / .wav)
```

Response

```
{
 "transcript": "Hello everyone welcome to the meeting..."
}
```

---

## Generate Meeting Analysis

```
POST /analyze-meeting
```

Input

```
Transcript text
```

Output includes:

* Executive summary
* Key decisions
* Action items
* Topic-wise summary
* Minutes of meeting

---

## Retrieve Transcript

```
GET /transcript/{meeting_id}
```

Example response

```
{
 "meeting_id": "1234-abcd",
 "transcript": "Hello everyone..."
}
```

---

## Retrieve Summary

```
GET /summary/{meeting_id}
```

Example response

```
{
 "meeting_id": "1234-abcd",
 "summary": "Executive summary..."
}
```

---

## Delete Meeting Data

```
DELETE /meeting/{meeting_id}
```

Response

```
{
 "message": "Meeting data deleted"
}
```

---

# Sample Outputs

## Example Transcript

```
Speaker 1: Welcome everyone to today's meeting.
Speaker 2: Let's discuss the new AI meeting assistant feature.
Speaker 1: The backend will be implemented using FastAPI.
```

---

## Executive Summary

```
The meeting focused on the development of an AI meeting assistant. 
The team discussed using FastAPI for backend services and integrating 
speech recognition for meeting transcription.
```

---

## Decisions

```
1. Use FastAPI for backend implementation.
2. Use Whisper for speech recognition.
```

---

## Action Items

```
Priyanka: Implement backend APIs.
Rahul: Research LLM models.
```

---

## Minutes of Meeting

```
Meeting Title: AI Meeting Assistant Planning
Date: 12 March 2026

Participants:
Team members

Discussion Points:
Development of AI meeting assistant

Decisions:
Use FastAPI and Whisper

Action Items:
Implement backend APIs
Research AI models
```

---

# Security & Data Handling

* Meeting recordings stored locally
* Data deleted via API request
* No permanent storage unless configured

---

# Demo Video Script

Record a **2–3 minute demo** showing:

### Step 1 Start Backend

Run

```
uvicorn app.main:app --reload
```

---

### Step 2 Open API Docs

```
http://127.0.0.1:8000/docs
```

---

### Step 3 Join Meeting

Call

```
POST /meeting/join
```

---

### Step 4 Upload Audio

Use

```
POST /transcribe
```

Upload sample meeting audio.

---

### Step 5 Generate AI Summary

Call

```
POST /analyze-meeting
```

Show generated:

* Executive summary
* Decisions
* Action items
* MOM

---

### Step 6 Retrieve Results

Call

```
GET /transcript/{meeting_id}
GET /summary/{meeting_id}
```

---

# Approach Explanation

The system processes meetings in multiple stages:

1. Meeting initiation via backend API
2. Audio capture and upload
3. Speech recognition converts audio to text
4. AI model analyzes transcript
5. System generates structured meeting insights

This modular architecture allows independent processing of meeting audio and scalable AI analysis.

---

# Technologies Used

* FastAPI
* Python
* Whisper
* OpenRouter
* Nemotron LLM

---

# Final Deliverables

This submission includes:

* Source code
* Setup instructions
* API documentation
* Sample outputs
* Architecture explanation
* Demonstration video

--
