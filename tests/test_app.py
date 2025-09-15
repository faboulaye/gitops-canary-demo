from datetime import datetime, timedelta

def test_health_ok(client):
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json() == {"status": "ok"}


def test_manifest_defaults(client, clean_env):
    """When no env vars are set, defaults are returned."""
    resp = client.get("/manifest")
    assert resp.status_code == 200
    body = resp.json()

    assert body["name"] == "gitops-canary-demo"
    assert body["version"] == "unknown"
    assert body["commit"] == "unknown"
    assert body["repository"] == "https://github.com/faboulaye/gitops-canary-demo"

    # build_time should be a valid ISO-8601 string and "recent" (generated at call time)
    parsed = datetime.fromisoformat(body["build_time"])
    # sanity: should be within ~5 minutes of now
    assert abs(datetime.now() - parsed) < timedelta(minutes=5)


def test_manifest_env_overrides(client, clean_env, set_env):
    """Env vars override all manifest fields."""
    set_env(
        APP_NAME="demo-app",
        APP_VERSION="1.2.3",
        GIT_COMMIT="abc1234",
        GIT_REPO="https://github.com/example/demo",
        BUILD_TIME="2025-09-15T12:00:00+00:00",  # ISO-8601 with offset
    )

    resp = client.get("/manifest")
    assert resp.status_code == 200
    body = resp.json()

    assert body["name"] == "demo-app"
    assert body["version"] == "1.2.3"
    assert body["commit"] == "abc1234"
    assert body["repository"] == "https://github.com/example/demo"
    assert body["build_time"] == "2025-09-15T12:00:00+00:00"


def test_manifest_commit_fallback_behavior(client, clean_env, set_env):
    """
    If only BUILD_TIME or repo are provided, other fields should still use defaults.
    (This verifies no accidental cross-field coupling.)
    """
    set_env(BUILD_TIME="2030-01-01T00:00:00+00:00", GIT_REPO="https://github.com/acme/repo")

    resp = client.get("/manifest")
    assert resp.status_code == 200
    body = resp.json()

    assert body["name"] == "gitops-canary-demo"
    assert body["version"] == "unknown"
    assert body["commit"] == "unknown"
    assert body["repository"] == "https://github.com/acme/repo"
    assert body["build_time"] == "2030-01-01T00:00:00+00:00"
