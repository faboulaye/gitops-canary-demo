from fastapi import FastAPI
import os


app = FastAPI(title="gitops-canary-demo")


@app.get("/manifest")
def manifest():
    return {
    "name": os.getenv("APP_NAME", "gitops-canary-demo"),
    "version": os.getenv("APP_VERSION", "unknown"),
    "buildTag": os.getenv("BUILD_TAG", "unknown"),
    "commit": os.getenv("GIT_COMMIT", os.getenv("BUILD_TAG", "unknown")),
    }


@app.get("/health")
def health():
    return {"status": "ok"}