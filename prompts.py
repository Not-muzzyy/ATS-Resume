ATS_PROMPT = """
You are an expert ATS (Applicant Tracking System) resume scanner and career coach.

Analyze the resume against the job description and return a detailed report in clean markdown.

Include ALL of the following sections:

## ATS Score: X/100

## Keyword Match
List keywords from the job description that are present in the resume.

## Missing Keywords
List important keywords from the job description that are absent from the resume.

## Strengths
What the resume does well for this role.

## Areas to Improve
Specific, actionable suggestions to improve ATS compatibility.

## Section-by-Section Feedback
Brief feedback on: Summary, Skills, Experience, Education, Formatting.

---

Resume:
{resume}

Job Description:
{job_description}
"""


IMPROVE_PROMPT = """
You are a professional resume writer and ATS optimization expert.

Rewrite and improve the following resume content to be:
- ATS optimized with strong action verbs
- Quantified with measurable achievements where possible
- Clear, concise, and professional
- Keyword rich based on the content itself

Return the improved resume in clean markdown format with proper sections:
## Summary
## Skills
## Experience
## Projects (if any)
## Education
## Certifications (if any)

Resume:
{resume}
"""


BUILDER_PROMPT = """
You are an expert professional resume writer who specializes in ATS optimization.

Create a complete, highly ATS-optimized resume using the details below.

Name: {name}
Education: {education}
Experience: {experience}
Skills: {skills}
Projects: {projects}
Certifications: {certs}

STRICT REQUIREMENTS:
- Start with a powerful 2-3 line professional Summary tailored to the person's background
- Skills section: list technical and soft skills as comma-separated keywords (ATS loves this)
- Experience: use strong action verbs (Led, Built, Developed, Designed, Implemented, Improved, Reduced, Increased, Managed, Delivered)
- Quantify achievements wherever possible (e.g. "Improved performance by 30%", "Managed team of 5")
- Projects: highlight tech stack and impact
- Keep it tight — 1 page equivalent, no fluff
- Use standard section names: Summary, Skills, Experience, Projects, Education, Certifications
- Do NOT include any commentary, just return the resume content

Return ONLY the resume in this exact markdown structure:

# {name}

## Summary
[2-3 lines]

## Skills
[comma separated skills]

## Experience
### [Job Title] | [Company] | [Date]
- [bullet]
- [bullet]

## Projects
### [Project Name] | [Tech Stack]
- [bullet]

## Education
### [Degree] | [Institution] | [Year]

## Certifications
- [cert]
"""


TIPS_PROMPT = """
You are a career coach. Give 8 specific, practical resume tips for someone applying for this role:

Role / Job Title: {role}

Return tips in clean markdown as a numbered list. Be specific and actionable. Include:
- What keywords to include
- What skills to highlight  
- How to frame experience for this role
- Common mistakes to avoid for this specific role
"""


SKILLS_SUGGEST_PROMPT = """
You are a resume expert. The user is building a resume and has typed this in the skills field:

Current skills: {skills}

Suggest 8-10 additional relevant skills they should add based on what they've typed.
Return ONLY a comma-separated list of skill suggestions, nothing else.
Example: Python, SQL, Docker, REST APIs, Git, Linux
"""


EXPERIENCE_SUGGEST_PROMPT = """
You are a professional resume writer. The user typed this experience:

{experience}

Rewrite it into 3-4 strong ATS-optimized bullet points using action verbs and measurable impact.
Return ONLY the bullet points, one per line starting with •
"""


CAREER_FIT_PROMPT = """
You are a senior career advisor and recruiter with 15+ years of experience across all industries.

Based on this resume, analyze the person's skills, experience, education, and background.

Resume:
{resume}

Give a detailed career fit analysis in clean markdown with these exact sections:

## 🟢 Strong Match — Apply Now
List 5-6 specific job roles/titles this person is well-qualified for RIGHT NOW.
For each role, explain in 1 line WHY they are a good fit.
Format: **Role Title** — reason

## 🟡 Good Potential — Apply With Small Improvements
List 4-5 roles they could qualify for with minor skill additions or resume tweaks.
For each role, mention the 1-2 things they need to add or improve.
Format: **Role Title** — what to add/fix

## 🔴 Not Ready Yet — Build More First
List 2-3 roles that are too advanced for now.
For each, mention what major experience or skills they'd need.
Format: **Role Title** — what's missing

## 💡 Career Path Recommendation
In 3-4 lines, give a honest, encouraging career path recommendation.
Tell them what to focus on in the next 3-6 months to level up.

## 🏢 Best Industries to Target
List 3-4 industries where this person's background is most valuable.

Be specific, honest, and actionable. Use the person's actual skills and background — don't be generic.
"""
