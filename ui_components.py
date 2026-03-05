import streamlit as st


def inject_css():
    st.markdown("""
<style>
    /* ── Global ── */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .block-container {
        padding: 1.5rem 2rem 3rem 2rem !important;
        max-width: 900px !important;
        margin: 0 auto !important;
    }

    /* ── Hero ── */
    .hero-wrap {
        background: linear-gradient(135deg, #0f172a 0%, #1e3a5f 100%);
        border-radius: 16px;
        padding: 2.5rem 2rem;
        text-align: center;
        margin-bottom: 2rem;
    }
    .hero-badge {
        display: inline-block;
        background: rgba(99,179,237,0.15);
        color: #63b3ed;
        border: 1px solid rgba(99,179,237,0.3);
        border-radius: 20px;
        padding: 4px 14px;
        font-size: 0.75rem;
        font-weight: 600;
        letter-spacing: 0.05em;
        text-transform: uppercase;
        margin-bottom: 1rem;
    }
    .hero-title {
        font-size: 2.4rem;
        font-weight: 700;
        color: #ffffff;
        margin: 0 0 0.5rem 0;
        line-height: 1.2;
    }
    .hero-title span {
        color: #63b3ed;
    }
    .hero-sub {
        font-size: 1rem;
        color: #94a3b8;
        margin: 0 0 1.5rem 0;
    }
    .hero-pills {
        display: flex;
        justify-content: center;
        flex-wrap: wrap;
        gap: 8px;
        margin-bottom: 1.5rem;
    }
    .hero-pill {
        background: rgba(255,255,255,0.07);
        color: #cbd5e1;
        border-radius: 20px;
        padding: 5px 14px;
        font-size: 0.82rem;
        border: 1px solid rgba(255,255,255,0.1);
    }
    .privacy-note {
        font-size: 0.78rem;
        color: #64748b;
        margin-top: 0.5rem;
    }
    .privacy-note span {
        color: #22c55e;
    }

    /* ── How it works ── */
    .steps-wrap {
        display: flex;
        justify-content: center;
        gap: 12px;
        flex-wrap: wrap;
        margin-bottom: 2rem;
    }
    .step-card {
        background: #1e293b;
        border: 1px solid #334155;
        border-radius: 12px;
        padding: 1rem 1.2rem;
        text-align: center;
        flex: 1;
        min-width: 140px;
        max-width: 200px;
    }
    .step-icon {
        font-size: 1.6rem;
        margin-bottom: 6px;
    }
    .step-num {
        font-size: 0.7rem;
        color: #63b3ed;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    .step-title {
        font-size: 0.88rem;
        font-weight: 600;
        color: #e2e8f0;
        margin-top: 4px;
    }
    .step-desc {
        font-size: 0.78rem;
        color: #64748b;
        margin-top: 3px;
    }

    /* ── Section header ── */
    .section-header {
        font-size: 1.15rem;
        font-weight: 700;
        color: #e2e8f0;
        margin: 1.5rem 0 0.3rem 0;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    .section-sub {
        font-size: 0.85rem;
        color: #64748b;
        margin-bottom: 1rem;
    }

    /* ── Info box ── */
    .info-box {
        background: #1e293b;
        border: 1px solid #334155;
        border-left: 4px solid #63b3ed;
        border-radius: 8px;
        padding: 0.9rem 1rem;
        margin: 0.8rem 0;
        font-size: 0.88rem;
        color: #94a3b8;
    }
    .info-box strong {
        color: #e2e8f0;
    }

    /* ── ATS Score card ── */
    .score-wrap {
        display: flex;
        align-items: center;
        gap: 1.5rem;
        background: #1e293b;
        border: 1px solid #334155;
        border-radius: 14px;
        padding: 1.2rem 1.5rem;
        margin: 1rem 0;
        flex-wrap: wrap;
    }
    .score-circle-high {
        width: 80px; height: 80px;
        border-radius: 50%;
        background: conic-gradient(#22c55e var(--pct), #1e293b 0);
        display: flex; align-items: center; justify-content: center;
        flex-shrink: 0;
        box-shadow: 0 0 0 4px #0f172a;
    }
    .score-circle-mid {
        width: 80px; height: 80px;
        border-radius: 50%;
        background: conic-gradient(#f59e0b var(--pct), #1e293b 0);
        display: flex; align-items: center; justify-content: center;
        flex-shrink: 0;
        box-shadow: 0 0 0 4px #0f172a;
    }
    .score-circle-low {
        width: 80px; height: 80px;
        border-radius: 50%;
        background: conic-gradient(#ef4444 var(--pct), #1e293b 0);
        display: flex; align-items: center; justify-content: center;
        flex-shrink: 0;
        box-shadow: 0 0 0 4px #0f172a;
    }
    .score-inner {
        width: 58px; height: 58px;
        border-radius: 50%;
        background: #0f172a;
        display: flex; align-items: center; justify-content: center;
        font-size: 1rem; font-weight: 700; color: #e2e8f0;
    }
    .score-label {
        font-size: 1.1rem;
        font-weight: 700;
        color: #e2e8f0;
    }
    .score-verdict {
        font-size: 0.85rem;
        margin-top: 3px;
    }
    .score-verdict-high { color: #22c55e; }
    .score-verdict-mid  { color: #f59e0b; }
    .score-verdict-low  { color: #ef4444; }
    .score-tip {
        font-size: 0.82rem;
        color: #64748b;
        margin-top: 5px;
    }

    /* ── Result card ── */
    .result-card {
        background: #1e293b;
        border: 1px solid #334155;
        border-radius: 12px;
        padding: 1.2rem 1.4rem;
        margin: 1rem 0;
    }

    /* ── Encourage box ── */
    .encourage-box {
        background: linear-gradient(135deg, #0d2137, #0f3460);
        border: 1px solid #1d4ed8;
        border-radius: 10px;
        padding: 0.9rem 1.1rem;
        font-size: 0.88rem;
        color: #93c5fd;
        margin: 0.8rem 0;
    }

    /* ── Next steps ── */
    .next-step-box {
        background: #1e293b;
        border: 1px solid #22c55e33;
        border-left: 4px solid #22c55e;
        border-radius: 8px;
        padding: 0.9rem 1rem;
        margin: 0.8rem 0;
        font-size: 0.88rem;
        color: #94a3b8;
    }
    .next-step-box strong {
        color: #22c55e;
    }

    /* ── Buttons ── */
    .stButton > button {
        width: 100% !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
        font-size: 0.95rem !important;
        padding: 0.55rem 1rem !important;
        transition: all 0.2s ease !important;
    }
    .stDownloadButton > button {
        width: 100% !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
    }

    /* ── Inputs ── */
    .stTextInput input, .stTextArea textarea {
        font-size: 0.95rem !important;
        border-radius: 8px !important;
        background: #1e293b !important;
        border: 1px solid #334155 !important;
        color: #e2e8f0 !important;
    }
    .stTextInput input:focus, .stTextArea textarea:focus {
        border-color: #63b3ed !important;
        box-shadow: 0 0 0 2px rgba(99,179,237,0.15) !important;
    }
    input::placeholder, textarea::placeholder {
        color: #475569 !important;
    }

    /* ── Tabs ── */
    .stTabs [data-baseweb="tab-list"] {
        gap: 4px;
        background: #0f172a;
        border-radius: 10px;
        padding: 4px;
    }
    .stTabs [data-baseweb="tab"] {
        border-radius: 8px !important;
        font-size: 0.88rem !important;
        font-weight: 500 !important;
        color: #64748b !important;
        padding: 0.4rem 0.9rem !important;
    }
    .stTabs [aria-selected="true"] {
        background: #1e3a5f !important;
        color: #63b3ed !important;
    }

    /* ── Success / warning / error ── */
    .stAlert {
        border-radius: 8px !important;
        font-size: 0.88rem !important;
    }

    /* ── Footer ── */
    .footer {
        text-align: center;
        padding: 2rem 0 1rem 0;
        color: #334155;
        font-size: 0.78rem;
        border-top: 1px solid #1e293b;
        margin-top: 3rem;
    }
    .footer a { color: #475569; text-decoration: none; }

    /* ── Mobile ── */
    @media (max-width: 640px) {
        .hero-title { font-size: 1.7rem; }
        .block-container { padding: 1rem !important; }
        .step-card { min-width: 120px; }
        [data-testid="column"] {
            width: 100% !important;
            flex: 1 1 100% !important;
            min-width: 100% !important;
        }
    }
</style>
""", unsafe_allow_html=True)


def header():
    inject_css()
    st.markdown("""
<div class="hero-wrap">
    <div class="hero-badge">✦ Free AI Resume Tool</div>
    <h1 class="hero-title">Land Your Dream Job with<br><span>ResumeAI</span></h1>
    <p class="hero-sub">ATS checker, resume builder, and career advisor — all powered by AI, completely free.</p>
    <div class="hero-pills">
        <span class="hero-pill">📄 ATS Score Checker</span>
        <span class="hero-pill">✍️ Resume Builder</span>
        <span class="hero-pill">🔧 Resume Improver</span>
        <span class="hero-pill">🎯 Job Match Finder</span>
        <span class="hero-pill">💡 Career Tips</span>
    </div>
    <p class="privacy-note"><span>🔒 Your resume is never stored.</span> &nbsp;Everything is processed in real-time and deleted immediately.</p>
</div>
""", unsafe_allow_html=True)

    st.markdown("""
<div class="steps-wrap">
    <div class="step-card">
        <div class="step-icon">📤</div>
        <div class="step-num">Step 1</div>
        <div class="step-title">Upload Resume</div>
        <div class="step-desc">PDF, DOCX or paste text</div>
    </div>
    <div class="step-card">
        <div class="step-icon">🤖</div>
        <div class="step-num">Step 2</div>
        <div class="step-title">AI Analyzes</div>
        <div class="step-desc">Checks ATS compatibility</div>
    </div>
    <div class="step-card">
        <div class="step-icon">📈</div>
        <div class="step-num">Step 3</div>
        <div class="step-title">Get Results</div>
        <div class="step-desc">Score, gaps & improvements</div>
    </div>
    <div class="step-card">
        <div class="step-icon">⬇️</div>
        <div class="step-num">Step 4</div>
        <div class="step-title">Download</div>
        <div class="step-desc">Updated resume as DOCX</div>
    </div>
</div>
""", unsafe_allow_html=True)


def ats_explainer():
    st.markdown("""
<div class="info-box">
    <strong>💡 What is ATS?</strong><br>
    ATS (Applicant Tracking System) is software used by companies to automatically filter resumes
    before a human ever reads them. If your resume isn't optimized, it gets rejected automatically —
    even if you're qualified. This tool checks how well your resume passes ATS filters.
</div>
""", unsafe_allow_html=True)


def score_card(score: int):
    """Render a visual score card based on score value."""
    pct = f"{score * 3.6}deg"

    if score >= 75:
        circle_class = "score-circle-high"
        verdict = "✅ Strong Match"
        verdict_class = "score-verdict-high"
        tip = "Your resume is well-optimized. Apply with confidence!"
        encourage = "🎉 Great work! Your resume is ATS-ready. Focus on tailoring your cover letter next."
    elif score >= 50:
        circle_class = "score-circle-mid"
        verdict = "⚡ Good — Needs Tweaks"
        verdict_class = "score-verdict-mid"
        tip = "Add the missing keywords and your score will jump significantly."
        encourage = "💪 You're close! Add the missing keywords below and your chances improve a lot."
    else:
        circle_class = "score-circle-low"
        verdict = "⚠️ Needs Improvement"
        verdict_class = "score-verdict-low"
        tip = "Don't worry — use the Resume Improver tab to fix this quickly."
        encourage = "🙌 Don't be discouraged! Many people start here. Use the Improver tab to fix this in minutes."

    st.markdown(f"""
<div class="score-wrap">
    <div class="{circle_class}" style="--pct: {pct}">
        <div class="score-inner">{score}%</div>
    </div>
    <div>
        <div class="score-label">ATS Score: {score}/100</div>
        <div class="score-verdict {verdict_class}">{verdict}</div>
        <div class="score-tip">{tip}</div>
    </div>
</div>
<div class="encourage-box">{encourage}</div>
""", unsafe_allow_html=True)


def next_steps_after_ats():
    st.markdown("""
<div class="next-step-box">
    <strong>✅ What to do next:</strong><br>
    1. Add the missing keywords naturally into your Skills or Experience section.<br>
    2. Use the <strong>Improver tab</strong> to rewrite weak bullet points.<br>
    3. Re-run ATS check to see your improved score.<br>
    4. Check job matches below to find roles you are best suited for.
</div>
""", unsafe_allow_html=True)


def next_steps_after_build():
    st.markdown("""
<div class="next-step-box">
    <strong>✅ Your resume is ready! What to do next:</strong><br>
    1. Download as DOCX and review it in Word or Google Docs.<br>
    2. Go to the <strong>ATS Checker tab</strong> to check its score against a job description.<br>
    3. Share the link on LinkedIn or send directly to recruiters.
</div>
""", unsafe_allow_html=True)


def next_steps_after_improve():
    st.markdown("""
<div class="next-step-box">
    <strong>✅ Resume improved! What to do next:</strong><br>
    1. Download the improved version as DOCX.<br>
    2. Go to the <strong>ATS Checker tab</strong> to verify the new score.<br>
    3. Tailor it further for each specific job you apply to.
</div>
""", unsafe_allow_html=True)


def tips():
    st.markdown("""
<div class="result-card">
<h4 style="color:#e2e8f0; margin-top:0;">📋 General Resume Tips</h4>

<p style="color:#94a3b8; font-size:0.9rem; line-height:1.8;">
1. <strong style="color:#e2e8f0;">Use simple formatting</strong> — No tables, columns, or graphics. ATS cannot read them.<br>
2. <strong style="color:#e2e8f0;">Use strong action verbs</strong> — Led, Built, Improved, Designed, Reduced, Increased.<br>
3. <strong style="color:#e2e8f0;">Quantify achievements</strong> — "Improved performance by 30%" beats "Improved performance".<br>
4. <strong style="color:#e2e8f0;">Tailor for each job</strong> — Mirror keywords directly from the job description.<br>
5. <strong style="color:#e2e8f0;">Keep it 1 page</strong> — Unless you have 10+ years of experience.<br>
6. <strong style="color:#e2e8f0;">Use standard section names</strong> — Experience, Education, Skills, Projects, Certifications.<br>
7. <strong style="color:#e2e8f0;">Save as PDF or DOCX</strong> — Preserves formatting across all systems.<br>
8. <strong style="color:#e2e8f0;">No photos or logos</strong> — ATS systems discard them and it wastes space.<br>
9. <strong style="color:#e2e8f0;">Get a job description first</strong> — Copy it from LinkedIn, Indeed, or Naukri before tailoring.<br>
10. <strong style="color:#e2e8f0;">Fresher tip</strong> — If you have no work experience, lead with Projects and Skills instead.
</p>
</div>
""", unsafe_allow_html=True)


def footer():
    st.markdown("""
<div class="footer">
    Built with ❤️ by <a href="https://github.com/Not-muzzyy" target="_blank">Muzzu</a> &nbsp;•&nbsp;
    Powered by <strong>Groq AI</strong> &nbsp;•&nbsp;
    Free Forever &nbsp;•&nbsp;
    🔒 No data stored
</div>
""", unsafe_allow_html=True)
