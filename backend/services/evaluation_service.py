import os
import shutil

from services.resume_parser import extract_text
from services.ai_service import analyze_resume
from services.scorer import calculate_score

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

ALLOWED_EXTENSIONS = {".pdf", ".docx"}   # <-- Add this


def evaluate(job, files):

    results = []

    for file in files:

        # Validate file extension
        extension = os.path.splitext(file.filename)[1].lower()

        if extension not in ALLOWED_EXTENSIONS:
            raise ValueError(
                f"{file.filename} is not a supported file. Only PDF and DOCX files are allowed."
            )

        file_path = os.path.join(UPLOAD_FOLDER, file.filename)

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        resume_text = extract_text(file_path)

        try:
            candidate = analyze_resume(resume_text)
        except Exception as e:
            candidate = {
                "name": file.filename,
                "error": str(e)
            }

        candidate["evaluation"] = calculate_score(candidate, job)
        results.append(candidate)

    results.sort(
        key=lambda x: x["evaluation"]["score"],
        reverse=True
    )

    return {
        "job": job,
        "candidates": results
    }