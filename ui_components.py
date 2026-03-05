import streamlit as st

# ─────────────────────── LUCIDE SVG ICONS ─────────────────────── #
# All icons are inline SVG from lucide.dev — no install needed
# stroke="currentColor" means they inherit text color automatically

def _icon(paths, size=18, color="#63b3ed", extra=""):
    """Render a lucide-style SVG icon safely."""
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" '
        f'viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="2" '
        f'stroke-linecap="round" stroke-linejoin="round" '
        f'style="vertical-align:middle;flex-shrink:0;{extra}">{paths}</svg>'
    )

# Define every icon used in the app as a plain string of SVG path elements
ICO_UPLOAD    = _icon('<path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="17 8 12 3 7 8"/><line x1="12" y1="3" x2="12" y2="15"/>')
ICO_CPU       = _icon('<rect x="4" y="4" width="16" height="16" rx="2"/><rect x="9" y="9" width="6" height="6"/><line x1="9" y1="1" x2="9" y2="4"/><line x1="15" y1="1" x2="15" y2="4"/><line x1="9" y1="20" x2="9" y2="23"/><line x1="15" y1="20" x2="15" y2="23"/><line x1="20" y1="9" x2="23" y2="9"/><line x1="20" y1="14" x2="23" y2="14"/><line x1="1" y1="9" x2="4" y2="9"/><line x1="1" y1="14" x2="4" y2="14"/>')
ICO_CHART     = _icon('<line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/><line x1="2" y1="20" x2="22" y2="20"/>')
ICO_DOWNLOAD  = _icon('<path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/>')
ICO_SHIELD    = _icon('<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><polyline points="9 12 11 14 15 10"/>', color="#22c55e")
ICO_SEARCH    = _icon('<circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/>')
ICO_FILEEDIT  = _icon('<path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"/><path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"/>')
ICO_WRENCH    = _icon('<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/>')
ICO_LIGHTBULB = _icon('<line x1="9" y1="18" x2="15" y2="18"/><line x1="10" y1="22" x2="14" y2="22"/><path d="M15.09 14c.18-.98.65-1.74 1.41-2.5A4.65 4.65 0 0 0 18 8A6 6 0 0 0 6 8c0 1 .23 2.23 1.5 3.5A4.61 4.61 0 0 1 8.91 14"/>')
ICO_TARGET    = _icon('<circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/>')
ICO_USER      = _icon('<path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/>')
ICO_BOOK      = _icon('<path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/>')
ICO_STAR      = _icon('<polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/>')
ICO_AWARD     = _icon('<circle cx="12" cy="8" r="6"/><path d="M15.477 12.89L17 22l-5-3-5 3 1.523-9.11"/>', color="#f59e0b")
ICO_BRIEFCASE = _icon('<rect x="2" y="7" width="20" height="14" rx="2" ry="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/>')
ICO_ROCKET    = _icon('<path d="M4.5 16.5c-1.5 1.26-2 5-2 5s3.74-.5 5-2c.71-.84.7-2.13-.09-2.91a2.18 2.18 0 0 0-2.91-.09z"/><path d="m12 15-3-3a22 22 0 0 1 2-3.95A12.88 12.88 0 0 1 22 2c0 2.72-.78 7.5-6 11a22.35 22.35 0 0 1-4 2z"/><path d="M9 12H4s.55-3.03 2-4c1.62-1.08 5 0 5 0"/><path d="M12 15v5s3.03-.55 4-2c1.08-1.62 0-5 0-5"/>')
ICO_CHECK     = _icon('<polyline points="20 6 9 17 4 12"/>', color="#22c55e")
ICO_INFO      = _icon('<circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/>', color="#63b3ed")
ICO_LOCK      = _icon('<rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/>', color="#22c55e", size=14)
ICO_SPARKLE   = _icon('<path d="m12 3-1.912 5.813a2 2 0 0 1-1.275 1.275L3 12l5.813 1.912a2 2 0 0 1 1.275 1.275L12 21l1.912-5.813a2 2 0 0 1 1.275-1.275L21 12l-5.813-1.912a2 2 0 0 1-1.275-1.275L12 3Z"/>')
ICO_LIST      = _icon('<line x1="8" y1="6" x2="21" y2="6"/><line x1="8" y1="12" x2="21" y2="12"/><line x1="8" y1="18" x2="21" y2="18"/><line x1="3" y1="6" x2="3.01" y2="6"/><line x1="3" y1="12" x2="3.01" y2="12"/><line x1="3" y1="18" x2="3.01" y2="18"/>')
ICO_ARROW     = _icon('<line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/>', color="#64748b", size=14)


# ─────────────────────── CSS ─────────────────────── #

def inject_css():
    st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    .block-container {
        padding: 1.5rem 2rem 3rem 2rem !important;
        max-width: 900px !important;
        margin: 0 auto !important;
    }

    /* Hero */
    .hero-wrap {
        background: linear-gradient(135deg, #0f172a 0%, #1e3a5f 100%);
        border-radius: 16px;
        padding: 2.5rem 2rem;
        text-align: center;
        margin-bottom: 2rem;
    }
    .hero-badge {
        display: inline-flex;
        align-items: center;
        gap: 6px;
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
    .hero-title span { color: #63b3ed; }
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
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background: rgba(255,255,255,0.07);
        color: #cbd5e1;
        border-radius: 20px;
        padding: 5px 14px;
        font-size: 0.82rem;
        border: 1px solid rgba(255,255,255,0.1);
    }
    .privacy-note {
        display: inline-flex;
        align-items: center;
        gap: 5px;
        font-size: 0.78rem;
        color: #64748b;
        margin-top: 0.5rem;
    }
    .privacy-note span { color: #22c55e; }

    /* Steps */
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
        transition: border-color 0.2s;
    }
    .step-card:hover { border-color: #63b3ed; }
    .step-icon {
        display: flex;
        justify-content: center;
        margin-bottom: 8px;
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

    /* Section header */
    .section-header {
        font-size: 1.05rem;
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
        padding-left: 26px;
    }

    /* Info box */
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
    .info-box strong { color: #e2e8f0; }

    /* Score card */
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
        width: 80px; height: 80px; border-radius: 50%;
        background: conic-gradient(#22c55e var(--pct), #0f172a 0);
        display: flex; align-items: center; justify-content: center;
        flex-shrink: 0; box-shadow: 0 0 0 4px #0f172a;
    }
    .score-circle-mid {
        width: 80px; height: 80px; border-radius: 50%;
        background: conic-gradient(#f59e0b var(--pct), #0f172a 0);
        display: flex; align-items: center; justify-content: center;
        flex-shrink: 0; box-shadow: 0 0 0 4px #0f172a;
    }
    .score-circle-low {
        width: 80px; height: 80px; border-radius: 50%;
        background: conic-gradient(#ef4444 var(--pct), #0f172a 0);
        display: flex; align-items: center; justify-content: center;
        flex-shrink: 0; box-shadow: 0 0 0 4px #0f172a;
    }
    .score-inner {
        width: 58px; height: 58px; border-radius: 50%;
        background: #0f172a;
        display: flex; align-items: center; justify-content: center;
        font-size: 1rem; font-weight: 700; color: #e2e8f0;
    }
    .score-label { font-size: 1.1rem; font-weight: 700; color: #e2e8f0; }
    .score-verdict { font-size: 0.85rem; margin-top: 3px; display:flex; align-items:center; gap:5px; }
    .score-verdict-high { color: #22c55e; }
    .score-verdict-mid  { color: #f59e0b; }
    .score-verdict-low  { color: #ef4444; }
    .score-tip { font-size: 0.82rem; color: #64748b; margin-top: 5px; }

    /* Result card */
    .result-card {
        background: #1e293b;
        border: 1px solid #334155;
        border-radius: 12px;
        padding: 1.2rem 1.4rem;
        margin: 1rem 0;
    }

    /* Encourage box */
    .encourage-box {
        background: linear-gradient(135deg, #0d2137, #0f3460);
        border: 1px solid #1d4ed8;
        border-radius: 10px;
        padding: 0.9rem 1.1rem;
        font-size: 0.88rem;
        color: #93c5fd;
        margin: 0.8rem 0;
        display: flex;
        align-items: flex-start;
        gap: 8px;
    }

    /* Next steps */
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
    .next-step-box strong { color: #22c55e; }
    .next-step-row {
        display: flex;
        align-items: flex-start;
        gap: 6px;
        margin: 4px 0;
    }

    /* Buttons */
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

    /* Inputs */
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
    input::placeholder, textarea::placeholder { color: #475569 !important; }

    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 4px; background: #0f172a;
        border-radius: 10px; padding: 4px;
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

    /* Alerts */
    .stAlert { border-radius: 8px !important; font-size: 0.88rem !important; }

    /* Footer */
    .footer {
        text-align: center;
        padding: 2rem 0 1rem 0;
        color: #334155;
        font-size: 0.78rem;
        border-top: 1px solid #1e293b;
        margin-top: 3rem;
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 8px;
        flex-wrap: wrap;
    }
    .footer a { color: #475569; text-decoration: none; }
    .footer a:hover { color: #63b3ed; }

    /* Mobile */
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


# ─────────────────────── COMPONENTS ─────────────────────── #

def header():
    inject_css()
    st.markdown(f"""
<div class="hero-wrap">
    <div class="hero-badge">{ICO_SPARKLE} Free AI Resume Tool</div>
    <h1 class="hero-title">Land Your Dream Job with<br><span>ResumeAI</span></h1>
    <p class="hero-sub">ATS checker, resume builder &amp; career advisor — powered by AI, completely free.</p>
    <div class="hero-pills">
        <span class="hero-pill">{_icon('<polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/>', size=14, color="#94a3b8")} ATS Score Checker</span>
        <span class="hero-pill">{_icon('<path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"/><path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"/>', size=14, color="#94a3b8")} Resume Builder</span>
        <span class="hero-pill">{_icon('<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/>', size=14, color="#94a3b8")} Resume Improver</span>
        <span class="hero-pill">{_icon('<circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/>', size=14, color="#94a3b8")} Job Match Finder</span>
        <span class="hero-pill">{_icon('<line x1="9" y1="18" x2="15" y2="18"/><line x1="10" y1="22" x2="14" y2="22"/><path d="M15.09 14c.18-.98.65-1.74 1.41-2.5A4.65 4.65 0 0 0 18 8A6 6 0 0 0 6 8c0 1 .23 2.23 1.5 3.5A4.61 4.61 0 0 1 8.91 14"/>', size=14, color="#94a3b8")} Career Tips</span>
    </div>
    <p class="privacy-note">{ICO_LOCK} <span>Your resume is never stored.</span> &nbsp;Everything is processed in real-time and deleted immediately.</p>
</div>
""", unsafe_allow_html=True)

    st.markdown(f"""
<div class="steps-wrap">
    <div class="step-card">
        <div class="step-icon">{_icon('<path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="17 8 12 3 7 8"/><line x1="12" y1="3" x2="12" y2="15"/>', size=28, color="#63b3ed")}</div>
        <div class="step-num">Step 1</div>
        <div class="step-title">Upload Resume</div>
        <div class="step-desc">PDF, DOCX or paste text</div>
    </div>
    <div class="step-card">
        <div class="step-icon">{_icon('<rect x="4" y="4" width="16" height="16" rx="2"/><rect x="9" y="9" width="6" height="6"/><line x1="9" y1="1" x2="9" y2="4"/><line x1="15" y1="1" x2="15" y2="4"/><line x1="9" y1="20" x2="9" y2="23"/><line x1="15" y1="20" x2="15" y2="23"/><line x1="20" y1="9" x2="23" y2="9"/><line x1="20" y1="14" x2="23" y2="14"/><line x1="1" y1="9" x2="4" y2="9"/><line x1="1" y1="14" x2="4" y2="14"/>', size=28, color="#63b3ed")}</div>
        <div class="step-num">Step 2</div>
        <div class="step-title">AI Analyzes</div>
        <div class="step-desc">Checks ATS compatibility</div>
    </div>
    <div class="step-card">
        <div class="step-icon">{_icon('<line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/><line x1="2" y1="20" x2="22" y2="20"/>', size=28, color="#63b3ed")}</div>
        <div class="step-num">Step 3</div>
        <div class="step-title">Get Results</div>
        <div class="step-desc">Score, gaps &amp; improvements</div>
    </div>
    <div class="step-card">
        <div class="step-icon">{_icon('<path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/>', size=28, color="#63b3ed")}</div>
        <div class="step-num">Step 4</div>
        <div class="step-title">Download</div>
        <div class="step-desc">Updated resume as DOCX</div>
    </div>
</div>
""", unsafe_allow_html=True)


def ats_explainer():
    st.markdown(f"""
<div class="info-box">
    <div style="display:flex;align-items:flex-start;gap:8px;">
        {ICO_INFO}
        <div><strong>What is ATS?</strong><br>
        ATS (Applicant Tracking System) is software used by companies to automatically filter resumes
        before a human ever reads them. If your resume is not optimized, it gets rejected automatically —
        even if you are qualified. This tool checks how well your resume passes ATS filters.</div>
    </div>
</div>
""", unsafe_allow_html=True)


def score_card(score: int):
    pct = f"{score * 3.6}deg"
    if score >= 75:
        circle_class = "score-circle-high"
        verdict_icon = _icon('<polyline points="20 6 9 17 4 12"/>', size=14, color="#22c55e")
        verdict = "Strong Match"
        verdict_class = "score-verdict-high"
        tip = "Your resume is well-optimized. Apply with confidence!"
        encourage_icon = _icon('<polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/>', size=16, color="#93c5fd")
        encourage = "Great work! Your resume is ATS-ready. Focus on tailoring your cover letter next."
    elif score >= 50:
        circle_class = "score-circle-mid"
        verdict_icon = _icon('<circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/>', size=14, color="#f59e0b")
        verdict = "Good — Needs Tweaks"
        verdict_class = "score-verdict-mid"
        tip = "Add the missing keywords and your score will jump significantly."
        encourage_icon = _icon('<path d="M14.5 10c-.83 0-1.5-.67-1.5-1.5v-5c0-.83.67-1.5 1.5-1.5s1.5.67 1.5 1.5v5c0 .83-.67 1.5-1.5 1.5z"/><path d="M20.5 10H19V8.5c0-.83.67-1.5 1.5-1.5s1.5.67 1.5 1.5-.67 1.5-1.5 1.5z"/><path d="M9.5 14c.83 0 1.5.67 1.5 1.5v5c0 .83-.67 1.5-1.5 1.5S8 21.33 8 20.5v-5c0-.83.67-1.5 1.5-1.5z"/><path d="M3.5 14H5v1.5c0 .83-.67 1.5-1.5 1.5S2 16.33 2 15.5 2.67 14 3.5 14z"/><path d="M14 20.5c0-.83.67-1.5 1.5-1.5h5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5h-5c-.83 0-1.5-.67-1.5-1.5z"/><path d="M10 3.5c0 .83-.67 1.5-1.5 1.5h-5C2.67 5 2 4.33 2 3.5S2.67 2 3.5 2h5C9.33 2 10 2.67 10 3.5z"/>', size=16, color="#93c5fd")
        encourage = "You are close! Add the missing keywords below and your chances improve a lot."
    else:
        circle_class = "score-circle-low"
        verdict_icon = _icon('<circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/>', size=14, color="#ef4444")
        verdict = "Needs Improvement"
        verdict_class = "score-verdict-low"
        tip = "Don't worry — use the Improve Resume tab to fix this quickly."
        encourage_icon = _icon('<path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/>', size=16, color="#93c5fd")
        encourage = "Don't be discouraged! Many people start here. Use the Improve Resume tab to fix this in minutes."

    st.markdown(f"""
<div class="score-wrap">
    <div class="{circle_class}" style="--pct:{pct}">
        <div class="score-inner">{score}%</div>
    </div>
    <div>
        <div class="score-label">ATS Score: {score}/100</div>
        <div class="score-verdict {verdict_class}">{verdict_icon} {verdict}</div>
        <div class="score-tip">{tip}</div>
    </div>
</div>
<div class="encourage-box">{encourage_icon} <span>{encourage}</span></div>
""", unsafe_allow_html=True)


def _step_row(icon_svg, text):
    return f'<div class="next-step-row">{icon_svg}<span>{text}</span></div>'


def next_steps_after_ats():
    st.markdown(f"""
<div class="next-step-box">
    <strong>What to do next:</strong><br>
    {_step_row(ICO_ARROW, "Add the missing keywords naturally into your Skills or Experience section.")}
    {_step_row(ICO_ARROW, "Use the <strong>Improve Resume tab</strong> to rewrite weak bullet points.")}
    {_step_row(ICO_ARROW, "Re-run ATS check to see your improved score.")}
    {_step_row(ICO_ARROW, "Check job matches below to find roles best suited for you.")}
</div>
""", unsafe_allow_html=True)


def next_steps_after_build():
    st.markdown(f"""
<div class="next-step-box">
    <strong>Your resume is ready! What to do next:</strong><br>
    {_step_row(ICO_ARROW, "Download as DOCX and review it in Word or Google Docs.")}
    {_step_row(ICO_ARROW, "Go to the <strong>Check Resume tab</strong> to verify your ATS score.")}
    {_step_row(ICO_ARROW, "Share on LinkedIn or send directly to recruiters.")}
</div>
""", unsafe_allow_html=True)


def next_steps_after_improve():
    st.markdown(f"""
<div class="next-step-box">
    <strong>Resume improved! What to do next:</strong><br>
    {_step_row(ICO_ARROW, "Download the improved version as DOCX.")}
    {_step_row(ICO_ARROW, "Go to the <strong>Check Resume tab</strong> to verify the new score.")}
    {_step_row(ICO_ARROW, "Tailor it further for each specific job you apply to.")}
</div>
""", unsafe_allow_html=True)


def tips():
    ar = ICO_ARROW
    st.markdown(f"""
<div class="result-card">
    <div style="display:flex;align-items:center;gap:8px;margin-bottom:1rem;">
        {ICO_LIST}
        <h4 style="color:#e2e8f0;margin:0;">General Resume Tips</h4>
    </div>
    <div style="color:#94a3b8;font-size:0.9rem;line-height:2;">
        {_step_row(ar, "<strong style='color:#e2e8f0;'>Use simple formatting</strong> — No tables, columns, or graphics. ATS cannot read them.")}
        {_step_row(ar, "<strong style='color:#e2e8f0;'>Use strong action verbs</strong> — Led, Built, Improved, Designed, Reduced, Increased.")}
        {_step_row(ar, "<strong style='color:#e2e8f0;'>Quantify achievements</strong> — Improved performance by 30% beats Improved performance.")}
        {_step_row(ar, "<strong style='color:#e2e8f0;'>Tailor for each job</strong> — Mirror keywords directly from the job description.")}
        {_step_row(ar, "<strong style='color:#e2e8f0;'>Keep it 1 page</strong> — Unless you have 10+ years of experience.")}
        {_step_row(ar, "<strong style='color:#e2e8f0;'>Use standard section names</strong> — Experience, Education, Skills, Projects, Certifications.")}
        {_step_row(ar, "<strong style='color:#e2e8f0;'>Save as PDF or DOCX</strong> — Preserves formatting across all systems.")}
        {_step_row(ar, "<strong style='color:#e2e8f0;'>No photos or logos</strong> — ATS systems discard them and it wastes space.")}
        {_step_row(ar, "<strong style='color:#e2e8f0;'>Get the job description first</strong> — Copy from LinkedIn, Indeed, or Naukri before tailoring.")}
        {_step_row(ar, "<strong style='color:#e2e8f0;'>Fresher tip</strong> — No work experience? Lead with Projects and Skills instead.")}
    </div>
</div>
""", unsafe_allow_html=True)


def footer():
    st.markdown(f"""
<div class="footer">
    {_icon('<path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/>', size=13, color="#475569")}
    Built by <a href="https://github.com/Not-muzzyy" target="_blank">Muzzu</a>
    &nbsp;•&nbsp;
    {_icon('<path d="M4.5 16.5c-1.5 1.26-2 5-2 5s3.74-.5 5-2c.71-.84.7-2.13-.09-2.91a2.18 2.18 0 0 0-2.91-.09z"/><path d="m12 15-3-3a22 22 0 0 1 2-3.95A12.88 12.88 0 0 1 22 2c0 2.72-.78 7.5-6 11a22.35 22.35 0 0 1-4 2z"/>', size=13, color="#475569")}
    Powered by Groq AI
    &nbsp;•&nbsp;
    {ICO_LOCK} No data stored
</div>
""", unsafe_allow_html=True)
