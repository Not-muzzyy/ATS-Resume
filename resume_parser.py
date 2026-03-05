import pdfplumber
from docx import Document


def parse_pdf(file) -> str:
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text.strip()


def parse_docx(file) -> str:
    doc = Document(file)
    text = "\n".join([p.text for p in doc.paragraphs if p.text.strip()])
    return text.strip()
