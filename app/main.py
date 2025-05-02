
# ======================= IMPORTS =======================
import pickle
import os
from fastapi import FastAPI, HTTPException

from utils.preprocess import preprocess_url_single
from models.predictor import load_model, predict

# from .utils.preprocess import preprocess_url_single
# from .models.predictor import load_model, predict
import logging
from pydantic import BaseModel

from schemas.predict import URLRequest 

# from .schemas.predict import URLRequest 
import re
import numpy as np
import joblib


# Logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# ======================= SETUP =======================
app = FastAPI(title="URL Phishing Detector")

@app.on_event("startup")
async def startup():
    global model
    model = load_model()
    if model is not None:
        logger.info("Model loaded successfully")
    else:
        logger.error("Model failed to load")


@app.get("/")
def root():
    return {"message": "FastAPI app running"}
    


# ======================= PREDICTION ROUTE =======================
# Route that receives the validated request

@app.post("/predict")
async def predict_url(payload: URLRequest):
    if model is None:
        raise HTTPException(status_code=500, detail="Model not loaded.")

    try:
        url = str(payload.url)
        prediction = predict(model, url)
        label = "Legitimate" if prediction == 1 else "Phishing"
        return {"prediction": label}
    except Exception as e:
        logger.error(f"Prediction error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

