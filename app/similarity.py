from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('all-MiniLM-L6-v2')

def compute_similarity_score(resume_text, jd_text):
    resume_vec = model.encode([resume_text])[0]
    jd_vec = model.encode([jd_text])[0]
    score = cosine_similarity([resume_vec], [jd_vec])[0][0]
    return round(score * 100, 2)