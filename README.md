# gitops-canary-demo

[![Publish Docker image to GitHub Container Registry](https://github.com/faboulaye/gitops-canary-demo/actions/workflows/ci.yaml/badge.svg)](https://github.com/faboulaye/gitops-canary-demo/actions/workflows/ci.yaml)

Learning/playground repository that shows a FastAPI service shipped with CI → Helm → Argo CD, using **Argo Rollouts** for canary deployments.

## Run locally

### Run unit test

```bash
task test
```

### Start server

```bash
task run
```

### Call endpoint

```bash
curl http://localhost:8080/manifest
```
