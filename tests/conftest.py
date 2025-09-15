import pytest
from fastapi.testclient import TestClient
from app.main import app

# Reusable client for all tests
@pytest.fixture()
def client():
    return TestClient(app)

# Clears relevant env vars before each test; returns monkeypatch to reuse
@pytest.fixture()
def clean_env(monkeypatch):
    for var in ("APP_NAME", "APP_VERSION", "GIT_COMMIT", "GIT_REPO", "BUILD_TIME"):
        monkeypatch.delenv(var, raising=False)
    return monkeypatch

# Helper fixture to set multiple env vars in one call
@pytest.fixture()
def set_env(monkeypatch):
    def _set_env(**kwargs):
        for k, v in kwargs.items():
            monkeypatch.setenv(k, str(v))
    return _set_env
