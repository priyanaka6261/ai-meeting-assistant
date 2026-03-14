import os
import requests
import streamlit as st
from typing import Optional


BACKEND_URL = os.getenv("BACKEND_URL", "http://127.0.0.1:8000")


def _post(path: str, **kwargs):
    url = f"{BACKEND_URL.rstrip('/')}{path}"
    return requests.post(url, **kwargs)


def _get(path: str, **kwargs):
    url = f"{BACKEND_URL.rstrip('/')}{path}"
    return requests.get(url, **kwargs)


def _delete(path: str, **kwargs):
    url = f"{BACKEND_URL.rstrip('/')}{path}"
    return requests.delete(url, **kwargs)


def set_page_config():
    st.set_page_config(
        page_title="AI Meeting Assistant",
        page_icon="🧠",
        layout="wide",
        initial_sidebar_state="expanded",
    )


def render_sidebar():
    with st.sidebar:
        st.markdown("### 🧠 AI Meeting Assistant")
        st.markdown(
            "Modern dashboard on top of your FastAPI backend. "
            "Join meetings, upload recordings, transcribe and view smart summaries."
        )

        st.markdown("---")
        st.markdown("#### Backend URL")
        st.text_input(
            "FastAPI base URL",
            value=BACKEND_URL,
            key="backend_url_input",
            help="Example: http://127.0.0.1:8000",
        )
        st.session_state["backend_url"] = st.session_state.get(
            "backend_url_input", BACKEND_URL
        )

        st.markdown("---")
        st.caption("Start backend: `uvicorn app.main:app --reload`")


def section_title(title: str, subtitle: Optional[str] = None):
    st.markdown(
        f"""
        <div style="
            padding: 0.6rem 0.9rem;
            border-radius: 0.9rem;
            background: #0b1220;
            color: #e5e7eb;
            margin-bottom: 1rem;
            box-shadow: 0 10px 30px rgba(15,23,42,0.7);
        ">
            <div style="font-size:0.8rem; text-transform:uppercase; opacity:0.7;">Project Meeting</div>
            <h3 style="margin: 0.1rem 0 0.2rem 0; font-size: 1.2rem;">{title}</h3>
            <p style="margin: 0; font-size: 0.9rem; opacity: 0.8;">{subtitle or ""}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_meeting_stage():
    st.markdown(
        """
        <div style="
            background: #020617;
            border-radius: 1.4rem;
            padding: 1rem 1.2rem 0.8rem 1.2rem;
            box-shadow: 0 20px 60px rgba(15,23,42,0.9);
        ">
          <!-- window header -->
          <div style="display:flex; align-items:center; gap:0.4rem; margin-bottom:0.7rem;">
            <div style="width:10px;height:10px;border-radius:999px;background:#f97373;"></div>
            <div style="width:10px;height:10px;border-radius:999px;background:#facc15;"></div>
            <div style="width:10px;height:10px;border-radius:999px;background:#4ade80;"></div>
          </div>

          <!-- 2x2 video grid -->
          <div style="display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:0.6rem;">
            <div style="background:#111827;border-radius:0.9rem;padding:0.8rem;display:flex;align-items:flex-end;justify-content:flex-start;
                        background-image:linear-gradient(145deg,#1f2937,#020617);">
              <div style="background:rgba(15,23,42,0.75);padding:0.4rem 0.7rem;border-radius:999px;font-size:0.75rem;color:#e5e7eb;">
                👨‍💼 Alex – Speaking
              </div>
            </div>
            <div style="background:#111827;border-radius:0.9rem;padding:0.8rem;display:flex;align-items:flex-end;justify-content:flex-start;
                        background-image:linear-gradient(145deg,#0f172a,#020617);">
              <div style="background:rgba(15,23,42,0.75);padding:0.4rem 0.7rem;border-radius:999px;font-size:0.75rem;color:#e5e7eb;">
                🙋‍♀️ Priyanka – Host
              </div>
            </div>
            <div style="background:#111827;border-radius:0.9rem;display:flex;align-items:center;justify-content:center;
                        border:1px dashed rgba(148,163,184,0.6);">
              <span style="font-size:0.8rem;color:#9ca3af;">Waiting for participant...</span>
            </div>
            <div style="background:#0f172a;border-radius:0.9rem;display:flex;align-items:center;justify-content:center;flex-direction:column;
                        gap:0.3rem;">
              <div style="
                    width:52px;height:52px;border-radius:999px;
                    background:linear-gradient(145deg,#38bdf8,#818cf8);
                    display:flex;align-items:center;justify-content:center;
                    color:white;font-size:1.6rem;
              ">
                🤖
              </div>
              <div style="font-size:0.8rem;color:#e5e7eb;font-weight:600;">Meeting Bot</div>
              <div style="font-size:0.7rem;color:#9ca3af;">Listening & capturing notes</div>
            </div>
          </div>

          <!-- bottom controls -->
          <div style="display:flex;justify-content:center;gap:0.8rem;margin-top:0.9rem;padding:0.45rem 0.7rem;
                      background:#020617;border-radius:999px;">
            <div style="width:34px;height:34px;border-radius:999px;background:#111827;display:flex;align-items:center;justify-content:center;color:#e5e7eb;font-size:0.9rem;">🎙</div>
            <div style="width:34px;height:34px;border-radius:999px;background:#111827;display:flex;align-items:center;justify-content:center;color:#e5e7eb;font-size:0.9rem;">🎥</div>
            <div style="width:34px;height:34px;border-radius:999px;background:#111827;display:flex;align-items:center;justify-content:center;color:#e5e7eb;font-size:0.9rem;">💬</div>
            <div style="width:34px;height:34px;border-radius:999px;background:#b91c1c;display:flex;align-items:center;justify-content:center;color:#fee2e2;font-size:0.9rem;">⏻</div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def page_live_meeting():
    """Page 1 – live meeting controls + visual stage + notes panel."""
    transcript = st.session_state.get("transcript")
    analysis = st.session_state.get("analysis")

    cols = st.columns([2, 1])

    # Left: meeting controls
    with cols[0]:
        section_title(
            "Live Meeting Control",
            "Connect the bot to your online meeting and manage it from here.",
        )
        meeting_url = st.text_input(
            "Meeting link",
            placeholder="Paste Google Meet / Zoom / Teams link",
        )
        meeting_id = st.text_input(
            "Meeting ID",
            value=st.session_state.get("current_meeting_id", ""),
        )

        c1, c2, c3, c4, c5 = st.columns(5)
        with c1:
            if st.button("Join", use_container_width=True):
                if not meeting_url:
                    st.warning("Please paste a meeting URL.")
                else:
                    try:
                        resp = _post("/meeting/join", params={"meeting_url": meeting_url})
                        resp.raise_for_status()
                        data = resp.json()
                        mid = data.get("meeting_id")
                        st.session_state["current_meeting_id"] = mid
                        st.success(f"Joined meeting. ID: {mid}")
                    except Exception as e:
                        st.error(f"Join failed: {e}")

        with c2:
            if st.button("Stop", use_container_width=True, disabled=not meeting_id):
                try:
                    resp = _post(f"/meeting/stop/{meeting_id}")
                    st.success(resp.json())
                except Exception as e:
                    st.error(f"Stop failed: {e}")

        with c3:
            if st.button("Transcript", use_container_width=True, disabled=not meeting_id):
                try:
                    resp = _get(f"/transcript/{meeting_id}")
                    data = resp.json()
                    st.session_state["transcript"] = data.get("transcript")
                    st.success("Transcript loaded from backend.")
                    transcript = st.session_state["transcript"]
                except Exception as e:
                    st.error(f"Failed to get transcript: {e}")

        with c4:
            if st.button("Summary", use_container_width=True, disabled=not meeting_id):
                try:
                    resp = _get(f"/summary/{meeting_id}")
                    data = resp.json()
                    st.session_state["analysis"] = data.get("summary")
                    st.success("Summary loaded from backend.")
                    analysis = st.session_state["analysis"]
                except Exception as e:
                    st.error(f"Failed to get summary: {e}")

        with c5:
            if st.button("Delete", use_container_width=True, disabled=not meeting_id):
                try:
                    resp = _delete(f"/meeting/{meeting_id}")
                    st.success(resp.json())
                except Exception as e:
                    st.error(f"Failed to delete meeting: {e}")

    # Right: visual stage
    with cols[1]:
        render_meeting_stage()

    st.markdown("---")

    # Notes panel
    section_title(
        "AI Notes",
        "Transcript and summary associated with this meeting.",
    )
    with st.container():
        st.markdown("**Live Transcript**")
        st.text_area(
            "Transcript",
            value=transcript or "",
            height=180,
            label_visibility="collapsed",
            placeholder="Transcript will appear after you fetch it or run transcription.",
        )

    st.markdown("---")

    st.markdown("**Highlights & Action Items**")
    if isinstance(analysis, dict):
        exec_summary = analysis.get("executive_summary")
        if exec_summary:
            st.caption("Executive Summary")
            st.write(exec_summary)

        key_decisions = analysis.get("key_decisions")
        if key_decisions:
            st.caption("Key Decisions")
            if isinstance(key_decisions, list):
                for item in key_decisions:
                    st.markdown(f"- {item}")
            else:
                st.markdown(f"- {key_decisions}")

        action_items = analysis.get("action_items")
        if action_items:
            st.caption("Action Items")
            if isinstance(action_items, list):
                for item in action_items:
                    st.markdown(f"- {item}")
            else:
                st.markdown(f"- {action_items}")

        minutes = analysis.get("minutes_of_meeting")
        if minutes:
            st.caption("Minutes of Meeting (MOM)")
            st.write(minutes)

    elif analysis:
        st.write(analysis)
    else:
        st.caption("Summary from backend will appear here.")


def page_recording_and_notes():
    """Page 2 – upload recording, transcribe, analyze, and see notes layout."""
    backend_url = st.session_state.get("backend_url", BACKEND_URL)
    transcript = st.session_state.get("transcript")
    analysis = st.session_state.get("analysis")

    section_title(
        "Recording Upload",
        "Upload a recording, transcribe it and generate AI notes.",
    )

    uploaded_file = st.file_uploader(
        "Upload meeting audio",
        type=["mp3", "wav", "m4a"],
        help=f"Sent to {backend_url}/transcribe",
    )
    auto_analyze = st.checkbox(
        "Auto-run AI analysis after transcription", value=True
    )

    st.markdown("---")
    st.markdown("**Or paste an existing transcript to analyze**")

    with st.form("manual_analysis_form"):
        manual_transcript = st.text_area(
            "Transcript to analyze",
            value=transcript or "",
            height=160,
            placeholder="Paste or type a meeting transcript here and press Enter or click Analyze.",
        )
        manual_submit = st.form_submit_button("Analyze Transcript")

    if uploaded_file is not None:
        st.audio(uploaded_file)

    if st.button(
        "Transcribe & Analyze" if auto_analyze else "Transcribe Only",
        use_container_width=True,
        disabled=uploaded_file is None,
    ):
        if uploaded_file is None:
            st.warning("Please upload an audio file first.")
        else:
            with st.spinner("Transcribing audio via backend..."):
                try:
                    files = {
                        "file": (
                            uploaded_file.name,
                            uploaded_file,
                            uploaded_file.type,
                        )
                    }
                    resp = _post("/transcribe", files=files)
                    resp.raise_for_status()
                    data = resp.json()
                    transcript = data.get("transcript")
                    st.session_state["transcript"] = transcript
                    st.success("Transcription completed.")
                except Exception as e:
                    st.error(f"Transcription failed: {e}")

            if auto_analyze and transcript:
                with st.spinner("Running AI meeting analysis..."):
                    try:
                        resp = _post("/analyze-meeting", params={"transcript": transcript})
                        resp.raise_for_status()
                        analysis = resp.json().get("analysis")
                        st.session_state["analysis"] = analysis
                        st.success("Analysis completed.")
                    except Exception as e:
                        st.error(f"Analysis failed: {e}")

    # Manual analysis path (also triggered by pressing Enter inside the form)
    if manual_submit and manual_transcript.strip():
        with st.spinner("Running AI meeting analysis on pasted transcript..."):
            try:
                resp = _post("/analyze-meeting", params={"transcript": manual_transcript})
                resp.raise_for_status()
                analysis = resp.json().get("analysis")
                st.session_state["analysis"] = analysis
                st.session_state["transcript"] = manual_transcript
                st.success("Analysis completed.")
            except Exception as e:
                st.error(f"Analysis failed: {e}")

    st.markdown("---")
    section_title(
        "AI Notes from Recording",
        "Transcript and key points detected from the uploaded audio.",
    )

    col_left, col_right = st.columns([2.2, 1.3], gap="large")

    with col_left:
        st.markdown("**Transcript**")
        st.text_area(
            "Transcript",
            value=transcript or "",
            height=260,
            label_visibility="collapsed",
            placeholder="Transcript will appear here after you transcribe.",
        )

    with col_right:
        st.markdown("**Highlights & Action Items**")
        if isinstance(analysis, dict):
            exec_summary = analysis.get("executive_summary")
            if exec_summary:
                st.caption("Executive Summary")
                st.write(exec_summary)

            key_decisions = analysis.get("key_decisions")
            if key_decisions:
                st.caption("Key Decisions")
                if isinstance(key_decisions, list):
                    for item in key_decisions:
                        st.markdown(f"- {item}")
                else:
                    st.markdown(f"- {key_decisions}")

            action_items = analysis.get("action_items")
            if action_items:
                st.caption("Action Items")
                if isinstance(action_items, list):
                    for item in action_items:
                        st.markdown(f"- {item}")
                else:
                    st.markdown(f"- {action_items}")

            minutes = analysis.get("minutes_of_meeting")
            if minutes:
                st.caption("Minutes of Meeting (MOM)")
                st.write(minutes)
        elif analysis:
            st.write(analysis)
        else:
            st.caption("Run analysis to see decisions, actions and MOM here.")


def main():
    set_page_config()
    st.markdown(
        """
        <style>
        .stApp {
            background: #0f172a;
            color: #e5e7eb;
        }
        .block-container {
            padding-top: 1.5rem;
            padding-bottom: 3rem;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    render_sidebar()

    # Simple navigation: separate pages for each core functionality
    page = st.sidebar.radio(
        "Pages",
        ["Overview", "Live Meeting", "Recording & AI Notes"],
        index=0,
    )

    if page == "Overview":
        section_title(
            "AI Meeting Dashboard",
            "Use the menu to manage live meetings or work with recordings.",
        )
        st.markdown(
            "- **Live Meeting**: control the bot with join / stop / transcript / summary.\n"
            "- **Recording & AI Notes**: upload audio, transcribe and see AI-generated notes.\n"
            "- Backend URL is configurable in the sidebar."
        )
        render_meeting_stage()
    elif page == "Live Meeting":
        page_live_meeting()
    else:
        page_recording_and_notes()


if __name__ == "__main__":
    main()


