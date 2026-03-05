ATS_PROMPT = """
You are an ATS resume scanner.

Analyze the resume against the job description.

Return in clean markdown format:

ATS Score (0-100)

Keyword Match

Missing Keywords

Strengths

Improvements

Resume:
{resume}

Job Description:
{job_description}
"""


IMPROVE_PROMPT = """
Improve the following resume content to be ATS optimized.

Rewrite the bullet points to be stronger and more professional.

Resume Section:
{resume}
"""


BUILDER_PROMPT = """
Create an ATS optimized resume.

Name: {name}
Education: {education}
Experience: {experience}
Skills: {skills}
Projects: {projects}
Certifications: {certs}

Return a clean professional resume.
"""
