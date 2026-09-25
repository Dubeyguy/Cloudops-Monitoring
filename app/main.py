from fastapi import FastAPI
from app.config import APP_VERSION, ENVIRONMENT

app = FastAPI()

@app.get("/")
def root():
    return {
        "application" : "Cloudops Monitoring Platform",
        "status" : "healthy",
        "environment" : ENVIRONMENT,
        "version" : APP_VERSION
    }

@app.get("/health")
def health():
    return {
        "status" : "healthy"
    }