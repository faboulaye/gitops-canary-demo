from fastapi import FastAPI
from pydantic import BaseModel

import os
from datetime import datetime


app = FastAPI(title="gitops-canary-demo")

class Manifest(BaseModel):
    name: str
    version: str
    commit: str
    repository: str
    build_time: str


@app.get("/manifest")
def manifest() -> Manifest:
    return Manifest(
        name=os.getenv("APP_NAME", "gitops-canary-demo"),
        version=os.getenv("APP_VERSION", "unknown"),
        commit=os.getenv("GIT_COMMIT", "unknown"),
        repository=os.getenv("GIT_REPO", "https://github.com/faboulaye/gitops-canary-demo"),
        build_time=os.getenv("BUILD_TIME", datetime.now().isoformat())
    )


@app.get("/health")
def health():
    return {"status": "ok"}