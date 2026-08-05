import json
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def analyze_job(job_description):

    prompt = f"""
You are an expert HR recruiter.

Analyze this Job Description.

Return ONLY JSON.

{{
    "required_skills":[],
    "preferred_skills":[],
    "minimum_experience":"",
    "education":"",
    "certifications":[]
}}

Job Description:

{job_description}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    text = response.text.strip()

    text = text.replace("```json", "")
    text = text.replace("```", "")

    return json.loads(text)