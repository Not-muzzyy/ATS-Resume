import re
import streamlit as st
from resume_parser import parse_pdf, parse_docx
from ai_engine import (
    ats_check, improve_resume, build_resume,
    get_role_tips, suggest_skills, improve_experience_bullets,
    career_fit
)
from ui_components import (
    header, tips, footer,
    ats_explainer, score_card,
    next_steps_after_ats,
    next_steps_after_build,
    next_steps_after_improve
)
from resume_to_docx import markdown_to_docx

st.set_page_config(
    page_title="ResumeAI — Free ATS Resume Checker & Builder",
    page_icon="📄",
    layout="centered"
)

# ── Session state init ──
for key in ["ats_result", "ats_resume_text", "ats_score",
            "career_fit_result", "improved_result", "built_resume",
            "skill_suggestions", "exp_bullets", "role_tips"]:
    if key not in st.session_state:
        st.session_state[key] = "" if key != "ats_score" else 0

header()

# ── Tab labels — clean text only, no emojis (SVGs can't go in st.tabs) ──
tab1, tab2, tab3, tab4 = st.tabs([
    "Check Resume",
    "Build Resume",
    "Improve Resume",
    "Tips & Advice"
])

# ── Reusable inline SVG helper (same as ui_components) ──
def _svg(paths, size=16, color="#63b3ed"):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" '
        f'viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="2" '
        f'stroke-linecap="round" stroke-linejoin="round" '
        f'style="vertical-align:middle;flex-shrink:0;">{paths}</svg>'
    )

def _sh(icon_svg, text):
    """Section header with SVG icon."""
    return f'<div class="section-header">{icon_svg} {text}</div>'

def _sub(text):
    """Section subtitle."""
    return f'<div class="section-sub">{text}</div>'

# Pre-defined icons used in app.py
I_UPLOAD  = _svg('<path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="17 8 12 3 7 8"/><line x1="12" y1="3" x2="12" y2="15"/>')
I_BRIEF   = _svg('<rect x="2" y="7" width="20" height="14" rx="2" ry="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/>')
I_TARGET  = _svg('<circle cx="12" cy="12" r="10"/><line x1="22" y1="12" x2="18" y2="12"/><line x1="6" y1="12" x2="2" y2="12"/><line x1="12" y1="6" x2="12" y2="2"/><line x1="12" y1="22" x2="12" y2="18"/>')
I_USER    = _svg('<path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/>')
I_BOOK    = _svg('<path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/>')
I_CODE    = _svg('<polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/>')
I_WRENCH  = _svg('<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/>')
I_ROCKET  = _svg('<path d="M4.5 16.5c-1.5 1.26-2 5-2 5s3.74-.5 5-2c.71-.84.7-2.13-.09-2.91a2.18 2.18 0 0 0-2.91-.09z"/><path d="m12 15-3-3a22 22 0 0 1 2-3.95A12.88 12.88 0 0 1 22 2c0 2.72-.78 7.5-6 11a22.35 22.35 0 0 1-4 2z"/>')
I_AWARD   = _svg('<circle cx="12" cy="8" r="6"/><path d="M15.477 12.89L17 22l-5-3-5 3 1.523-9.11"/>', color="#f59e0b")
I_LIST    = _svg('<line x1="8" y1="6" x2="21" y2="6"/><line x1="8" y1="12" x2="21" y2="12"/><line x1="8" y1="18" x2="21" y2="18"/><line x1="3" y1="6" x2="3.01" y2="6"/><line x1="3" y1="12" x2="3.01" y2="12"/><line x1="3" y1="18" x2="3.01" y2="18"/>')
I_BULB    = _svg('<line x1="9" y1="18" x2="15" y2="18"/><line x1="10" y1="22" x2="14" y2="22"/><path d="M15.09 14c.18-.98.65-1.74 1.41-2.5A4.65 4.65 0 0 0 18 8A6 6 0 0 0 6 8c0 1 .23 2.23 1.5 3.5A4.61 4.61 0 0 1 8.91 14"/>')
I_SEARCH  = _svg('<circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/>')
I_STARS   = _svg('<path d="m12 3-1.912 5.813a2 2 0 0 1-1.275 1.275L3 12l5.813 1.912a2 2 0 0 1 1.275 1.275L12 21l1.912-5.813a2 2 0 0 1 1.275-1.275L21 12l-5.813-1.912a2 2 0 0 1-1.275-1.275L12 3Z"/>')
I_EDIT    = _svg('<path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"/><path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"/>')
I_DOWN    = _svg('<path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/>')
I_INFO    = _svg('<circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/>')


# ─────────────────────── ATS CHECKER ─────────────────────── #

with tab1:

    ats_explainer()

    st.markdown(_sh(I_UPLOAD, "Your Resume"), unsafe_allow_html=True)
    st.markdown(_sub("Upload your resume or paste the text below"), unsafe_allow_html=True)

    option = st.radio(
        "Choose input method",
        ["Upload PDF", "Upload DOCX", "Paste Text"],
        horizontal=True,
        label_visibility="collapsed"
    )

    resume_text = ""

    if option == "Upload PDF":
        file = st.file_uploader(
            "Upload PDF",
            type=["pdf"],
            help="Upload a text-based PDF resume. Scanned or image PDFs won't work.",
            label_visibility="collapsed"
        )
        if file:
            try:
                resume_text = parse_pdf(file)
                if not resume_text.strip():
                    st.error("Could not read text from this PDF. Please upload a text-based resume PDF — not a scanned image or photo.")
                    resume_text = ""
                else:
                    st.success(f"Resume loaded — {len(resume_text.split())} words detected.")
            except Exception:
                st.error("Failed to read PDF. Please try a different file.")
                resume_text = ""

    elif option == "Upload DOCX":
        file = st.file_uploader(
            "Upload DOCX",
            type=["docx"],
            help="Upload a Word document resume.",
            label_visibility="collapsed"
        )
        if file:
            try:
                resume_text = parse_docx(file)
                if not resume_text.strip():
                    st.error("Could not read text from this DOCX. Please upload a valid Word resume document.")
                    resume_text = ""
                else:
                    st.success(f"Resume loaded — {len(resume_text.split())} words detected.")
            except Exception:
                st.error("Failed to read DOCX. Please try a different file.")
                resume_text = ""

    else:
        resume_text = st.text_area(
            "Paste your resume here",
            height=260,
            placeholder="Paste your full resume text here...\n\nExample:\nJohn Doe\njohn@email.com | LinkedIn\n\nSummary\nSoftware engineer with 3 years experience...\n\nSkills\nPython, SQL, React, AWS...",
            label_visibility="collapsed"
        )

    st.markdown(_sh(I_BRIEF, "Job Description"), unsafe_allow_html=True)
    st.markdown(_sub("Copy the job description from LinkedIn, Indeed, or Naukri and paste it here"), unsafe_allow_html=True)

    job_desc = st.text_area(
        "Job description",
        height=180,
        placeholder="Paste the full job description here...\n\nTip: Copy it directly from the job posting on LinkedIn or Indeed.",
        label_visibility="collapsed"
    )

    if st.button("Check My ATS Score", type="primary"):
        if not resume_text.strip():
            st.warning("Please upload or paste your resume first.")
        elif not job_desc.strip():
            st.warning("Please paste a job description. You can copy it from LinkedIn or Indeed.")
        else:
            with st.spinner("AI is analyzing your resume..."):
                result = ats_check(resume_text, job_desc)
                st.session_state.ats_result = result
                st.session_state.ats_resume_text = resume_text
                st.session_state.career_fit_result = ""
                score = 0
                try:
                    match = re.search(r'(\d{1,3})\s*/\s*100|(\d{1,3})%', result)
                    if match:
                        score = int(match.group(1) or match.group(2))
                        score = max(0, min(100, score))
                except Exception:
                    score = 0
                st.session_state.ats_score = score

    if st.session_state.ats_result:
        if st.session_state.ats_score > 0:
            score_card(st.session_state.ats_score)
        st.markdown('<div class="result-card">', unsafe_allow_html=True)
        st.markdown(st.session_state.ats_result)
        st.markdown('</div>', unsafe_allow_html=True)
        next_steps_after_ats()
        st.markdown("---")
        st.markdown(_sh(I_TARGET, "Where Should You Apply?"), unsafe_allow_html=True)
        st.markdown(_sub("Based on your resume, AI will suggest which job roles match you best right now"), unsafe_allow_html=True)
        if st.button("Find My Best Job Matches"):
            with st.spinner("Analyzing your career profile..."):
                st.session_state.career_fit_result = career_fit(
                    st.session_state.ats_resume_text
                )

    if st.session_state.career_fit_result:
        st.markdown('<div class="result-card">', unsafe_allow_html=True)
        st.markdown(st.session_state.career_fit_result)
        st.markdown('</div>', unsafe_allow_html=True)


# ─────────────────────── RESUME BUILDER ─────────────────────── #

with tab2:

    st.markdown(f"""
<div class="info-box">
    <div style="display:flex;align-items:flex-start;gap:8px;">
        {I_INFO}
        <div><strong>How this works:</strong> Fill in your details below — even rough notes are fine.
        AI will turn them into a professional, ATS-optimized resume and generate a Word document for you to download.
        <br><br><strong>No experience?</strong> No problem — just fill in your projects, education, and skills.</div>
    </div>
</div>
""", unsafe_allow_html=True)

    st.markdown(_sh(I_USER, "Personal Details"), unsafe_allow_html=True)
    name = st.text_input("Full Name", placeholder="e.g. Muzzammil Khan")

    st.markdown(_sh(I_BOOK, "Education"), unsafe_allow_html=True)
    education = st.text_area(
        "Education",
        height=90,
        placeholder="e.g. BCA — Nandi Institute of Management and Science, Bellary (2022–2025)\n12th — XYZ School (2022)",
        label_visibility="collapsed"
    )

    st.markdown(_sh(I_CODE, "Skills"), unsafe_allow_html=True)
    st.markdown(_sub("List your technical and soft skills — the more the better for ATS"), unsafe_allow_html=True)
    skills = st.text_input(
        "Skills",
        placeholder="e.g. Python, Machine Learning, SQL, Git, Linux, Cybersecurity, Streamlit",
        label_visibility="collapsed"
    )
    if skills.strip():
        if st.button("Suggest More Skills"):
            with st.spinner("Finding relevant skills..."):
                st.session_state.skill_suggestions = suggest_skills(skills)
    if st.session_state.skill_suggestions:
        st.markdown(f"""
<div class="info-box">
    <div style="display:flex;align-items:flex-start;gap:8px;">
        {I_STARS}
        <div><strong>Suggested skills to add:</strong><br>{st.session_state.skill_suggestions}</div>
    </div>
</div>
""", unsafe_allow_html=True)

    st.markdown(_sh(I_BRIEF, "Work Experience"), unsafe_allow_html=True)
    st.markdown(_sub("No work experience? Leave this blank or describe internships, freelance work, or college activities"), unsafe_allow_html=True)
    experience = st.text_area(
        "Experience",
        height=130,
        placeholder="e.g. Intern at ABC Company (June 2024 — Aug 2024)\n- Worked on Python automation scripts\n- Helped with data analysis using Pandas\n\nOr for freshers:\n- No formal experience yet (just leave blank)",
        label_visibility="collapsed"
    )
    if experience.strip():
        if st.button("Rewrite Experience with Strong Action Verbs"):
            with st.spinner("Improving your experience bullets..."):
                st.session_state.exp_bullets = improve_experience_bullets(experience)
    if st.session_state.exp_bullets:
        st.markdown(f"""
<div class="info-box">
    <div style="display:flex;align-items:flex-start;gap:8px;">
        {I_EDIT}
        <div><strong>AI-improved version — copy this into the box above:</strong></div>
    </div>
</div>
""", unsafe_allow_html=True)
        st.code(st.session_state.exp_bullets, language=None)

    st.markdown(_sh(I_ROCKET, "Projects"), unsafe_allow_html=True)
    st.markdown(_sub("Projects are very important for freshers — list everything you have built"), unsafe_allow_html=True)
    projects = st.text_area(
        "Projects",
        height=120,
        placeholder="e.g. Mini-SIEM AI — Python, Streamlit, Scikit-learn\nDetects threats in log files using ML. Achieved 97% accuracy.\n\nPhishing Detector — Python, NLP\nClassifies phishing URLs with 0.97 accuracy.",
        label_visibility="collapsed"
    )

    st.markdown(_sh(I_AWARD, "Certifications"), unsafe_allow_html=True)
    certs = st.text_input(
        "Certifications",
        placeholder="e.g. Google Cybersecurity Certificate, HuggingFace AI Agents, AWS Cloud Practitioner",
        label_visibility="collapsed"
    )

    if st.button("Build My Resume Now", type="primary"):
        if not name.strip():
            st.warning("Please enter your full name to continue.")
        else:
            with st.spinner("AI is writing your professional resume..."):
                st.session_state.built_resume = build_resume(
                    name, education, experience, skills, projects, certs
                )

    if st.session_state.built_resume:
        st.markdown("---")
        st.markdown('<div class="result-card">', unsafe_allow_html=True)
        st.markdown(st.session_state.built_resume)
        st.markdown('</div>', unsafe_allow_html=True)
        next_steps_after_build()
        try:
            docx_bytes = markdown_to_docx(st.session_state.built_resume, name)
            safe_name = name.strip().replace(" ", "_") if name.strip() else "resume"
            st.download_button(
                "Download Resume as Word Document (.docx)",
                data=docx_bytes,
                file_name=f"{safe_name}_resume.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )
        except Exception:
            pass
        st.download_button(
            "Download Resume as Markdown (.md)",
            data=st.session_state.built_resume,
            file_name=f"{name.strip().replace(' ', '_') or 'resume'}_resume.md",
            mime="text/markdown"
        )


# ─────────────────────── RESUME IMPROVER ─────────────────────── #

with tab3:

    st.markdown(f"""
<div class="info-box">
    <div style="display:flex;align-items:flex-start;gap:8px;">
        {I_WRENCH}
        <div><strong>How this works:</strong> Upload or paste your existing resume.
        AI will rewrite it with stronger language, better structure, and ATS-friendly keywords —
        then generate a Word document you can download immediately.</div>
    </div>
</div>
""", unsafe_allow_html=True)

    st.markdown(_sh(I_UPLOAD, "Upload Your Existing Resume"), unsafe_allow_html=True)

    improve_option = st.radio(
        "Choose input method",
        ["Upload PDF", "Upload DOCX", "Paste Text"],
        horizontal=True,
        key="improve_radio",
        label_visibility="collapsed"
    )

    improve_text = ""

    if improve_option == "Upload PDF":
        imp_file = st.file_uploader(
            "Upload PDF",
            type=["pdf"],
            key="imp_pdf",
            label_visibility="collapsed"
        )
        if imp_file:
            try:
                improve_text = parse_pdf(imp_file)
                if not improve_text.strip():
                    st.error("Could not read text from this PDF. Please upload a text-based resume PDF — not a scanned image.")
                    improve_text = ""
                else:
                    st.success(f"Resume loaded — {len(improve_text.split())} words detected.")
            except Exception:
                st.error("Failed to read PDF. Please try a different file.")
                improve_text = ""

    elif improve_option == "Upload DOCX":
        imp_file = st.file_uploader(
            "Upload DOCX",
            type=["docx"],
            key="imp_docx",
            label_visibility="collapsed"
        )
        if imp_file:
            try:
                improve_text = parse_docx(imp_file)
                if not improve_text.strip():
                    st.error("Could not read text from this DOCX. Please upload a valid Word document.")
                    improve_text = ""
                else:
                    st.success(f"Resume loaded — {len(improve_text.split())} words detected.")
            except Exception:
                st.error("Failed to read DOCX. Please try a different file.")
                improve_text = ""

    else:
        improve_text = st.text_area(
            "Paste resume",
            height=300,
            key="improve_text",
            placeholder="Paste your existing resume text here and AI will rewrite it to be stronger and ATS-optimized...",
            label_visibility="collapsed"
        )

    if st.button("Improve My Resume Now", type="primary"):
        if not improve_text.strip():
            st.warning("Please upload or paste your resume first.")
        else:
            with st.spinner("AI is rewriting your resume..."):
                st.session_state.improved_result = improve_resume(improve_text)

    if st.session_state.improved_result:
        st.markdown("---")
        st.markdown('<div class="result-card">', unsafe_allow_html=True)
        st.markdown(st.session_state.improved_result)
        st.markdown('</div>', unsafe_allow_html=True)
        next_steps_after_improve()
        try:
            first_line = improve_text.strip().split('\n')[0] if improve_text.strip() else "resume"
            safe_name = re.sub(r'[^a-zA-Z0-9_]', '_', first_line[:30])
            docx_bytes = markdown_to_docx(st.session_state.improved_result, safe_name)
            st.download_button(
                "Download Improved Resume as Word Document (.docx)",
                data=docx_bytes,
                file_name="improved_resume.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )
        except Exception:
            pass
        st.download_button(
            "Download as Markdown (.md)",
            data=st.session_state.improved_result,
            file_name="improved_resume.md",
            mime="text/markdown"
        )


# ─────────────────────── TIPS ─────────────────────── #

with tab4:

    st.markdown(_sh(I_LIST, "Resume Tips for Everyone"), unsafe_allow_html=True)
    tips()

    st.markdown("---")
    st.markdown(_sh(I_BULB, "Get Tips for Your Specific Job"), unsafe_allow_html=True)
    st.markdown(_sub("Enter any job title and AI gives you 8 specific tips tailored for that role"), unsafe_allow_html=True)

    role = st.text_input(
        "Job title",
        placeholder="e.g. SOC Analyst, Software Engineer, Data Scientist, Product Manager",
        label_visibility="collapsed"
    )

    if st.button("Get My Personalized Tips", type="primary"):
        if not role.strip():
            st.warning("Please enter a job title first.")
        else:
            with st.spinner(f"Getting tips for {role}..."):
                st.session_state.role_tips = get_role_tips(role)

    if st.session_state.role_tips:
        st.markdown('<div class="result-card">', unsafe_allow_html=True)
        st.markdown(st.session_state.role_tips)
        st.markdown('</div>', unsafe_allow_html=True)


# ── Footer ──
footer()
