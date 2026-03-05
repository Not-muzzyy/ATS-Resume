import re


STOP_WORDS = {
    "the", "and", "for", "with", "that", "this", "are", "you", "have",
    "will", "from", "your", "our", "not", "but", "they", "been", "more",
    "was", "has", "had", "its", "can", "all", "any", "may", "use", "used",
    "using", "each", "also", "than", "into", "about", "such", "their",
    "well", "both", "very", "over", "who", "how", "what", "when", "where"
}


def calculate_ats_score(resume_text: str, job_description: str):
    """
    Returns (score: int, missing_keywords: list[str])
    Score is 0-100 based on keyword overlap between resume and job description.
    """
    if not job_description.strip():
        return 0, []

    resume_lower = resume_text.lower()

    # Extract meaningful words (4+ chars) from job description
    job_words = set(re.findall(r'\b[a-z]{4,}\b', job_description.lower()))
    keywords = job_words - STOP_WORDS

    if not keywords:
        return 0, []

    matched = [kw for kw in keywords if kw in resume_lower]
    missing = sorted([kw for kw in keywords if kw not in resume_lower])

    score = int((len(matched) / len(keywords)) * 100)

    return score, missing
