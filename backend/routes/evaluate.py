from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from typing import List
from services.evaluation_service import evaluate

router = APIRouter()

@router.post("/evaluate")
async def evaluate_candidates(
    jobTitle: str = Form(...),
    jobDescription: str = Form(...),
    requiredSkills: str = Form(...),
    preferredSkills: str = Form(...),
    experience: str = Form(...),
    files: List[UploadFile] = File(...)
):

    job = {
        "jobTitle": jobTitle,
        "jobDescription": jobDescription,
        "requiredSkills": requiredSkills,
        "preferredSkills": preferredSkills,
        "experience": experience
    }

    try:
        return evaluate(job, files)

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))