FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app
COPY app/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Build-time metadata (injected by CI)
ARG APP_NAME=gitops-canary-demo
ARG APP_DESCRIPTION="A demo app for GitOps with canary deployments"
ARG APP_VERSION=unknown
ARG GIT_COMMIT=unknown
ARG GIT_REPO=unknown
ARG BUILD_TIME=unknown


ENV APP_NAME=${APP_NAME} \
    APP_DESCRIPTION=${APP_DESCRIPTION} \
    APP_VERSION=${APP_VERSION} \
    GIT_COMMIT=${GIT_COMMIT} \
    GIT_REPO=${GIT_REPO} \
    BUILD_TIME=${BUILD_TIME}

LABEL org.opencontainers.image.title="${APP_NAME}" \
    org.opencontainers.image.description="${APP_DESCRIPTION}" \
    org.opencontainers.image.source="${GIT_REPO}" \
    org.opencontainers.image.version="${APP_VERSION}" \
    org.opencontainers.image.revision="${GIT_COMMIT}" \
    org.opencontainers.image.created="${BUILD_TIME}"


RUN addgroup --system app && adduser --system --ingroup app app
USER app

EXPOSE 8080
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]