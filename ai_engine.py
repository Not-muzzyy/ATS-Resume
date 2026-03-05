import os
import streamlit as st
from google import genai
from prompts import ATS_PROMPT, IMPROVE_PROMPT, BUILDER_PROMPT, TIPS_PROMPT


def get_api_key() -> str:
    """Safely fetch API key from Streamlit secrets or environment."""
    try:
        key = st.secrets.get("GEMINI_API_KEY", None)
        if key:
            return key
    except Exception:
        pass
    return os.getenv("GEMINI_API_KEY", "")


def get_client():
    api_key = get_api_key()
    if not api_key:
        st.error("⚠️ Gemini API key missing. Add GEMINI_API_KEY to Streamlit Secrets or .env file.")
        st.info("Get a free key at: https://aistudio.google.com/app/apikey")
        st.stop()
    return genai.Client(api_key=api_key)


def _call_gemini(prompt: str) -> str:
    """Single place for all Gemini API calls with error handling."""
    client = get_client()
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )
        return response.text if hasattr(response, "text") else str(response)
    except Exception as e:
        st.error(f"Gemini API error: {e}")
        return ""


def ats_check(resume: str, job: str) -> str:
    prompt = ATS_PROMPT.format(resume=resume, job_description=job)
    return _call_gemini(prompt)


def improve_resume(text: str) -> str:
    prompt = IMPROVE_PROMPT.format(resume=text)
    return _call_gemini(prompt)


def build_resume(name: str, education: str, exp: str,
                 skills: str, projects: str, certs: str) -> str:
    prompt = BUILDER_PROMPT.format(
        name=name,
        education=education,
        experience=exp,
        skills=skills,
        projects=projects,
        certs=certs
    )
    return _call_gemini(prompt)


def get_role_tips(role: str) -> str:
    prompt = TIPS_PROMPT.format(role=role)
    return _call_gemini(prompt)
