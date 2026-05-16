# ai-resume-screening-FastAPI
ai-resume-screening-FastAPI
FastAPI used and deployment through render An NLP-based API that analyzes resumes, predicts job roles, and matches resumes with job descriptions using AI.

Features Upload resume (PDF) Extract text using NLP Predict job category Match resume with job description Generate similarity score & recommendation Tech Stack FastAPI Scikit-learn Sentence Transformers PyMuPDF PostgreSQL API Endpoints Upload Resume POST /upload-resume

Uploads a PDF and returns predicted job category.

Match Score POST /match-score

Upload resume + job description → returns match score and recommendation.

How to Run pip install -r requirements.txt uvicorn app.main:app --reload

Open:

http://127.0.0.1:8000/docs Project Goal

Helps recruiters automate resume screening using AI and NLP.
