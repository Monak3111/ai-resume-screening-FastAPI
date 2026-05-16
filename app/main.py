from fastapi import FastAPI, UploadFile, File 
import shutil 
import os 
from resume_parser import extract_text_from_pdf 
from predictor import predict_category 
from matcher import calculate_match_score

app = FastAPI()

UPLOAD_FOLDER = "resumes"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # ✅ FIX

@app.get("/")
def home():
    return {"message": "AI Resume Screening API"}

@app.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = extract_text_from_pdf(file_path)

    category = predict_category(text)

    return {
        "filename": file.filename,
        "predicted_category": category
    }

@app.post("/match-score")
async def match_score(
    file: UploadFile = File(...),
    job_description: str = ""
):

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    resume_text = extract_text_from_pdf(file_path)

    score = calculate_match_score(resume_text, job_description)

    recommendation = "Good Match" if score > 70 else "Needs Improvement"

    return {
        "match_score": score,
        "recommendation": recommendation
    }