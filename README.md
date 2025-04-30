# FastAPI ML Deployment 🚀

This project is a lightweight, Dockerized FastAPI app that loads a machine learning model and serves predictions via an API.

## Endpoints
- `GET /` → Health check
- `POST /predict` → Predict URL (pass a JSON body with `url` field)

## Running Locally

```bash
docker build -t my_fastapi_project .
docker run -p 8000:8000 my_fastapi_project
