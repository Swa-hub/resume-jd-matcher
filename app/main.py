import streamlit as st
from resume_parser import extract_resume_text
from jd_parser import extract_jd_text
from similarity import compute_similarity_score
from rewrite_suggester import suggest_rewrite

# Page setup
st.set_page_config(page_title="Resume & JD Matcher", layout="centered")
st.title("📄 Resume & JD Matcher")

# File upload + JD input
resume_file = st.file_uploader("Upload Resume (PDF or DOCX)", type=["pdf", "docx"])
jd_text_input = st.text_area("Paste Job Description")

# Optional GPT rewrite checkbox
gpt_rewrite = st.checkbox("Suggest AI-powered resume improvements (Optional)")

# --------- Helper: Clean GPT Suggestions Display ---------
def display_suggestions(suggestions_text: str):
    st.markdown("### ✍️ GPT Resume Rewrite Suggestions")

    bullets = suggestions_text.strip().split("\n\n")
    for bullet in bullets:
        if ":" in bullet:
            title, desc = bullet.split(":", 1)
            st.markdown(f"**🔹 {title.strip()}**\n\n{desc.strip()}")
        else:
            st.markdown(f"🔸 {bullet.strip()}")
# ----------------------------------------------------------

# Main logic
if st.button("Match Now"):
    if resume_file and jd_text_input.strip():
        resume_text = extract_resume_text(resume_file)
        jd_text = extract_jd_text(jd_text_input)

        score = compute_similarity_score(resume_text, jd_text)
        st.success(f"✅ Match Score: {score}%")

        if gpt_rewrite:
            suggestions = suggest_rewrite(resume_text, jd_text)
            display_suggestions(suggestions)

    else:
        st.error("Upload a resume and paste a job description to proceed.")
