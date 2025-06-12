import pdfplumber
import docx2txt

def extract_resume_text(uploaded_file):
    if uploaded_file.type == "application/pdf":
        with pdfplumber.open(uploaded_file) as pdf:
            return " ".join([page.extract_text() for page in pdf.pages if page.extract_text()])
    elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        return docx2txt.process(uploaded_file)
    return ""