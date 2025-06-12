import os
import cohere
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv("COHERE_API_KEY")
client = cohere.Client(api_key)

def suggest_rewrite(resume: str, jd: str) -> str:
    prompt = f"""
Act as a resume coach. Given the job description and resume below, suggest 4–6 practical, specific improvements to better align the resume with the role.

Job Description:
{jd}

Resume:
{resume}

Your suggestions should be in this format:

🔹 Title  
Explanation (1–2 lines)

End with a brief encouragement or reminder if possible.
"""

    try:
        response = client.chat(
            model="command-r",
            message=prompt,
            temperature=0.7,
            max_tokens=600,
            stop_sequences=["---"]
        )

        suggestions = response.text.strip()

        # Optional: Graceful end if the response cuts off
        if not suggestions.endswith("."):
            suggestions = suggestions.rsplit("\n", 1)[0].strip() + "."

        return suggestions

    except Exception as e:
        return f"⚠️ Error fetching suggestions: {str(e)}"
