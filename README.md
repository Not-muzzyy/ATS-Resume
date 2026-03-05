<div align="center">

# 📄 ResumeAI

**Free AI-powered ATS Resume Checker, Builder & Improver**

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://ats-resume-6msv5xt7zszqwrpivawy65.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Groq](https://img.shields.io/badge/Powered%20by-Groq%20AI-F55036?style=for-the-badge)](https://groq.com)
[![License](https://img.shields.io/badge/License-MIT-22c55e?style=for-the-badge)](LICENSE)

![ResumeAI Banner](https://img.shields.io/badge/ATS%20Resume%20Checker-Free%20%26%20Open%20Source-1e3a5f?style=for-the-badge)

</div>

-----

## 🚀 What is ResumeAI?

**ResumeAI** is a free, open-source web app that helps job seekers — especially freshers — build, check, and improve their resumes using AI. It checks how well your resume passes ATS (Applicant Tracking System) filters used by companies to screen candidates automatically.

> Built by a BCA student, for students and freshers. No paid plans. No data stored. Ever.

-----

## ✨ Features

|Feature                 |Description                                                                             |
|------------------------|----------------------------------------------------------------------------------------|
|📊 **ATS Score Checker** |Upload your resume + job description → get an AI score out of 100 with detailed feedback|
|✍️ **Resume Builder**    |Fill in your details → AI writes a professional ATS-optimized resume                    |
|🔧 **Resume Improver**   |Upload your existing resume → AI rewrites it with stronger language                     |
|🎯 **Job Match Finder**  |AI analyzes your resume and suggests best-fit job roles                                 |
|💡 **Role-Specific Tips**|Enter any job title → get 8 tailored resume tips                                        |
|⬇️ **DOCX Download**     |Download your resume as a formatted Word document instantly                             |

-----

## 📸 Screenshots

> Check Resume Tab — ATS Score with visual ring indicator

> Build Resume Tab — Form-based resume builder with AI generation

> DOCX Output — Clean formatted Word document ready to send

-----

## 🛠️ Tech Stack

- **Frontend** — Streamlit with custom CSS (dark navy theme, Lucide SVG icons)
- **AI Engine** — Groq API running Llama 3.3 70B
- **Resume Parsing** — pdfplumber (PDF), python-docx (DOCX)
- **Document Generation** — python-docx with custom DOCX formatter
- **Deployment** — Streamlit Cloud (auto-deploys on push)

-----

## 📁 Project Structure

```
ATS-Resume/
│
├── app.py                 # Main Streamlit app — all tabs and UI logic
├── ui_components.py       # Hero, score card, section headers, SVG icons, CSS
├── ai_engine.py           # Groq API wrapper with retry logic
├── prompts.py             # All AI prompts (ATS, builder, improver, tips)
├── resume_parser.py       # PDF and DOCX text extraction
├── resume_to_docx.py      # Markdown → formatted Word document converter
├── ats_scoring.py         # Keyword matching algorithm
├── requirements.txt       # Python dependencies
└── .streamlit/
    └── secrets.toml       # API keys (not committed to GitHub)
```

-----

## ⚡ Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/Not-muzzyy/ATS-Resume.git
cd ATS-Resume
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Add your Groq API key

Create `.streamlit/secrets.toml`:

```toml
GROQ_API_KEY = "your_groq_api_key_here"
```

Get a free Groq API key at [console.groq.com](https://console.groq.com) — no credit card needed.

### 4. Run the app

```bash
streamlit run app.py
```

Open <http://localhost:8501> in your browser.

-----

## 🔑 Environment Variables

|Variable      |Description                 |Where to get it                             |
|--------------|----------------------------|--------------------------------------------|
|`GROQ_API_KEY`|Groq API key for AI features|[console.groq.com](https://console.groq.com)|

-----

## 📦 Requirements

```
streamlit
pdfplumber
python-docx
groq
pandas
```

-----

## 🌐 Deploy to Streamlit Cloud

1. Fork this repo
1. Go to [share.streamlit.io](https://share.streamlit.io)
1. Connect your GitHub repo
1. Set main file to `app.py`
1. Add `GROQ_API_KEY` in the Secrets section
1. Deploy — live in under 2 minutes

-----

## 🤝 Contributing

Contributions are welcome! If you find a bug or have a feature idea:

1. Fork the repo
1. Create a new branch — `git checkout -b feature/your-feature`
1. Commit your changes — `git commit -m "Add your feature"`
1. Push and open a Pull Request

-----

## 📋 Roadmap

- [ ] Resume preview before download
- [ ] Multiple resume templates (Modern, Classic, Minimal)
- [ ] Auto-fill builder from uploaded resume
- [ ] Before/after ATS score comparison
- [ ] Hindi language support
- [ ] Email resume to yourself

-----

## 👨‍💻 Author

**Muzzammil** — BCA Final Year Student, Bellary, Karnataka

[![GitHub](https://img.shields.io/badge/GitHub-Not--muzzyy-181717?style=flat&logo=github)](https://github.com/Not-muzzyy)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-muzzammilc7-0A66C2?style=flat&logo=linkedin)](https://linkedin.com/in/muzzammilc7)

-----

## 📄 License

MIT License — free to use, modify, and distribute.

-----

<div align="center">

**If this helped you — drop a ⭐ on the repo. It means a lot!**

*Built with ❤️ using Streamlit + Groq AI — Free Forever*

</div>
