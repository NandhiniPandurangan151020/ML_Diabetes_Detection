import os
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

# Define Pydantic model for input validation
class DiabetesInput(BaseModel):
    Glucose: float
    BloodPressure: float
    SkinThickness: float
    Insulin: float
    BMI: float
    DiabetesPedigreeFunction: float
    Pregnancies: float
    Age: float

# Load the pipeline at startup
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.path.join(BASE_DIR, "..", "models")  # adjust if your models folder path is different
pipeline_path = os.path.join(MODEL_DIR, "model.pkl")

pipeline = joblib.load(pipeline_path)

@app.post("/predict")
async def predict(data: DiabetesInput):
    # Extract features in the right order as numpy array
    features = np.array([
        data.Glucose,
        data.BloodPressure,
        data.SkinThickness,
        data.Insulin,
        data.BMI,
        data.DiabetesPedigreeFunction,
        data.Pregnancies,
        data.Age
    ]).reshape(1, -1)

    # Predict and get confidence (probability) if available
    prediction = pipeline.predict(features)[0]
    confidence = None
    if hasattr(pipeline, "predict_proba"):
        confidence = pipeline.predict_proba(features).max()

    return {
        "prediction": int(prediction),
        "confidence": float(confidence) if confidence is not None else None
    }
