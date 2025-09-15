from fastapi import FastAPI
import os


app = FastAPI(title="gitops-canary-demo")


@app.get("/manifest")
def manifest():
    return {
    "name": os.getenv("APP_NAME", "unknown"),
    "version": os.getenv("APP_VERSION", "unknown"),
    "commit": os.getenv("GIT_COMMIT", "unknown"),
    "repository": os.getenv("GIT_REPO", "unknown"),
    "build_time": os.getenv("BUILD_TIME", "unknown"),
    }


@app.get("/health")
def health():
    return {"status": "ok"}