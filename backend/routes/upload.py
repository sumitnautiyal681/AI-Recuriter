from fastapi import APIRouter, UploadFile, File
from services.resume_parser import extract_text
from services.ai_service import analyze_resume
import os
import shutil

router = APIRouter()

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@router.post("/upload")

async def upload_resumes(files: list[UploadFile] = File(...)):

    uploaded_files = []

    for file in files:

        file_path = os.path.join(UPLOAD_FOLDER, file.filename)

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        resume_text = extract_text(file_path)

        candidate = analyze_resume(resume_text)

        uploaded_files.append(candidate)

    return {
        "message": "Upload Successful",
        "files": uploaded_files
    }