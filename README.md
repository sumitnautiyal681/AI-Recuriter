# AI Recruiter

An AI-powered resume screening application that evaluates candidates based on job requirements using Google Gemini AI.

## Features

- Upload PDF and DOCX resumes
- Extract candidate information using Gemini AI
- Match resumes with job requirements
- Calculate candidate scores
- Rank candidates based on scores
- Responsive UI

## Tech Stack

**Frontend**
- React
- JavaScript
- CSS
- Axios

**Backend**
- FastAPI
- Python
- Google Gemini API
- pdfplumber
- python-docx

## Run Locally

### Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

## Author

**Sumit Nautiyal**
