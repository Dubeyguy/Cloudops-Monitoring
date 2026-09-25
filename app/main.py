from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {
        "application" : "Cloudops Monitoring Platform",
        "status" : "healthy",
        "environment" : "Local",
        "version" : "1.0.0"
    }

