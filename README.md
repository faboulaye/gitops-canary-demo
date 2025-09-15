# gitops-canary-demo

Learning/playground repository that shows a FastAPI service shipped with CI → Helm → Argo CD, using **Argo Rollouts** for canary deployments.

## Run locally

### Start server

```bash
APP_VERSION=1.0.0 GIT_COMMIT=$(git rev-parse --short HEAD) task run
```

### Call endpoint

```bash
curl http://localhost:8080/manifest
```
