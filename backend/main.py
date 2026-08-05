from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from routes.upload import router as upload_router
from routes.evaluate import router as evaluate_router
print("Upload router imported successfully")
app = FastAPI()

# Allow React to access FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173","https://ai-recuriter-tawny.vercel.app",],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(upload_router)
app.include_router(evaluate_router)

