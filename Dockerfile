FROM python:3.13.7-slim

# Update system packages to reduce vulnerabilities
RUN apt-get update && apt-get upgrade -y && apt-get clean && rm -rf /var/lib/apt/lists/*


WORKDIR /app
COPY app/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY app ./app


# Build-time metadata (injected by CI)
ARG APP_NAME=gitops-canary-demo
ARG APP_VERSION=unknown
ARG GIT_COMMIT=unknown
ARG GIT_REPO=unknown
ARG BUILD_TIME=unknown


ENV APP_NAME=${APP_NAME} \
    APP_VERSION=${APP_VERSION} \
    GIT_COMMIT=${GIT_COMMIT} \
    GIT_REPO=${GIT_REPO} \
    BUILD_TIME=${BUILD_TIME}    

EXPOSE 8080
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]