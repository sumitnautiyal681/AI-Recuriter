import os
import json

from dotenv import load_dotenv
from google import genai

load_dotenv()
print("Current working directory:", os.getcwd())
print("API Key Loaded:", bool(os.getenv("GEMINI_API_KEY")))
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def analyze_resume(resume_text):
    prompt = f"""
You are an expert technical recruiter.

Analyze this resume carefully.

Return ONLY valid JSON.

{{
    "name":"",
    "email":"",
    "phone":"",
    "skills":[],
    "experience":"",
    "education":"",
    "projects":[],
    "certifications":[],
    "summary":""
}}

Rules:
- Do not invent information.
- If a field is missing, return an empty string or empty array.
- If no experience is mentioned, return "Fresher".
- Return ONLY JSON.

Resume:

{resume_text}
"""
    print("Calling Gemini...")
    response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents=prompt
    )

    text = response.text.strip()

    # Remove markdown if Gemini returns it
    text = text.replace("```json", "")
    text = text.replace("```", "")
    text = text.strip()

    return json.loads(text)