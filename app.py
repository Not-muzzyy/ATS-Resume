import streamlit as st
from resume_parser import parse_pdf, parse_docx
from ai_engine import (
    ats_check, improve_resume, build_resume,
    get_role_tips, suggest_skills, improve_experience_bullets,
    career_fit
)
from ui_components import header, tips
from resume_to_docx import markdown_to_docx

st.set_page_config(page_title="ResumeAI", page_icon="📄", layout="wide")

header()

tab1, tab2, tab3, tab4 = st.tabs([
    "📊 ATS Checker",
    "🏗️ Resume Builder",
    "✏️ Resume Improver",
    "💡 Tips"
])


# ─────────────────────── ATS CHECKER ─────────────────────── #

with tab1:
    st.subheader("ATS Resume Checker")

    option = st.radio(
        "How do you want to provide your resume?",
        ["Upload PDF", "Upload DOCX", "Paste Text"],
        horizontal=True
    )

    resume_text = ""

    if option == "Upload PDF":
        file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])
        if file:
            resume_text = parse_pdf(file)
            st.success("PDF parsed successfully.")

    elif option == "Upload DOCX":
        file = st.file_uploader("Upload your resume (DOCX)", type=["docx"])
        if file:
            resume_text = parse_docx(file)
            st.success("DOCX parsed successfully.")

    else:
        resume_text = st.text_area("Paste your resume here", height=300)

    job_desc = st.text_area("Paste the Job Description here", height=200)

    if st.button("🔍 Analyze Resume", type="primary"):
        if not resume_text.strip():
            st.warning("Please upload or paste your resume first.")
        elif not job_desc.strip():
            st.warning("Please paste a job description to compare against.")
        else:
            with st.spinner("Analyzing with Groq AI..."):
                result = ats_check(resume_text, job_desc)
            if result:
                st.markdown(result)
                st.markdown("---")
                st.markdown("### 🎯 Where Should You Apply?")
                st.caption("Based on your resume, AI will suggest which roles you're best suited for.")
                if st.button("🔎 Find Best Job Matches for Me"):
                    with st.spinner("Analyzing your career fit..."):
                        fit_result = career_fit(resume_text)
                    if fit_result:
                        st.markdown(fit_result)


# ─────────────────────── RESUME BUILDER ─────────────────────── #

with tab2:
    st.subheader("AI Resume Builder")
    st.caption("Fill in your details — AI will write a professional ATS-optimized resume.")

    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("Full Name")
        certs = st.text_input("Certifications (e.g. AWS, Google, CompTIA)")

    with col2:
        education = st.text_area("Education (Degree, Institution, Year)", height=100)

    # Skills with AI suggestion
    skills = st.text_input("Skills (comma separated — type yours and get AI suggestions below)")

    if skills.strip():
        if st.button("💡 Suggest More Skills"):
            with st.spinner("Getting skill suggestions..."):
                suggestions = suggest_skills(skills)
            if suggestions:
                st.info(f"**Suggested skills to add:** {suggestions}")

    # Experience with AI improvement
    experience = st.text_area("Work Experience (job title, company, what you did)", height=150)

    if experience.strip():
        if st.button("✨ Improve Experience Bullets"):
            with st.spinner("Rewriting experience with action verbs..."):
                improved_exp = improve_experience_bullets(experience)
            if improved_exp:
                st.info("**AI-improved bullets (copy these into the box above):**")
                st.code(improved_exp, language=None)

    projects = st.text_area("Projects (name, tech stack, what it does)", height=120)

    if st.button("🚀 Generate Resume", type="primary"):
        if not name.strip():
            st.warning("Please enter your name.")
        else:
            with st.spinner("Groq AI is building your ATS resume..."):
                resume_md = build_resume(
                    name, education, experience,
                    skills, projects, certs
                )
            if resume_md:
                st.markdown("---")
                st.markdown(resume_md)

                # Generate DOCX
                docx_bytes = markdown_to_docx(resume_md, name)
                safe_name = name.strip().replace(" ", "_")

                col_a, col_b = st.columns(2)
                with col_a:
                    st.download_button(
                        "⬇️ Download as DOCX (Word)",
                        data=docx_bytes,
                        file_name=f"{safe_name}_resume.docx",
                        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                    )
                with col_b:
                    st.download_button(
                        "⬇️ Download as Markdown",
                        data=resume_md,
                        file_name=f"{safe_name}_resume.md",
                        mime="text/markdown"
                    )


# ─────────────────────── RESUME IMPROVER ─────────────────────── #

with tab3:
    st.subheader("Resume Improver")
    st.caption("Upload or paste your resume — Groq AI will rewrite it to be ATS optimized.")

    improve_option = st.radio(
        "How do you want to provide your resume?",
        ["Upload PDF", "Upload DOCX", "Paste Text"],
        horizontal=True,
        key="improve_radio"
    )

    improve_text = ""

    if improve_option == "Upload PDF":
        imp_file = st.file_uploader("Upload resume PDF", type=["pdf"], key="imp_pdf")
        if imp_file:
            improve_text = parse_pdf(imp_file)
            st.success("PDF parsed successfully.")

    elif improve_option == "Upload DOCX":
        imp_file = st.file_uploader("Upload resume DOCX", type=["docx"], key="imp_docx")
        if imp_file:
            improve_text = parse_docx(imp_file)
            st.success("DOCX parsed successfully.")

    else:
        improve_text = st.text_area("Paste your resume here", height=350, key="improve_text")

    if st.button("✨ Improve Resume", type="primary"):
        if not improve_text.strip():
            st.warning("Please upload or paste your resume first.")
        else:
            with st.spinner("Groq AI is improving your resume..."):
                result = improve_resume(improve_text)
            if result:
                st.markdown("---")
                st.markdown(result)

                # Extract name from first line for filename
                first_line = improve_text.strip().split('\n')[0]
                safe_name = first_line[:30].replace(" ", "_").replace("/", "")

                docx_bytes = markdown_to_docx(result, safe_name)

                col_a, col_b = st.columns(2)
                with col_a:
                    st.download_button(
                        "⬇️ Download Improved Resume (DOCX)",
                        data=docx_bytes,
                        file_name="improved_resume.docx",
                        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                    )
                with col_b:
                    st.download_button(
                        "⬇️ Download as Markdown",
                        data=result,
                        file_name="improved_resume.md",
                        mime="text/markdown"
                    )


# ─────────────────────── TIPS ─────────────────────── #

with tab4:
    st.subheader("Resume Tips")

    tips()

    st.markdown("---")
    st.markdown("### Get Role-Specific Tips from AI")
    role = st.text_input("Enter your target job title (e.g. SOC Analyst, Data Scientist)")

    if st.button("💡 Get AI Tips", type="primary"):
        if not role.strip():
            st.warning("Enter a job title first.")
        else:
            with st.spinner("Getting tips from Groq AI..."):
                ai_tips = get_role_tips(role)
            if ai_tips:
                st.markdown(ai_tips)
