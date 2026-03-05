import re


def extract_keywords(text):
    words = re.findall(r'\b[A-Za-z]+\b', text.lower())
    return set(words)


def calculate_ats_score(resume, job_description):

    resume_words = extract_keywords(resume)
    job_words = extract_keywords(job_description)

    matched = resume_words.intersection(job_words)

    if len(job_words) == 0:
        return 0, []

    score = int((len(matched) / len(job_words)) * 100)

    missing = list(job_words - resume_words)[:20]

    return score, missing
