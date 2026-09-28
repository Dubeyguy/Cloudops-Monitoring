from fastapi import FastAPI
from app.config import APP_VERSION, ENVIRONMENT
from app.storage import list_reports

app = FastAPI()

@app.get("/")
def root():
    return {
        "application" : "CloudOps Monitoring Platform",
        "status" : "healthy",
        "environment" : ENVIRONMENT,
        "version" : APP_VERSION
    }

@app.get("/health")
def health():
    return {
        "status" : "healthy"
    }

@app.get("/reports")
def reports():
    return {
        "container" : "reports",
        "files" : list_reports()

    }
