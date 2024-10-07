from fastapi import FastAPI
import joblib
import numpy as np
from pydantic import BaseModel

# Load the trained model and preprocessor
model = joblib.load('best_random_forest_model.pkl')
preprocessor = joblib.load('preprocessor.pkl') 


app = FastAPI()

# Define request body structure
class PredictRequest(BaseModel):
    features: list

# Prediction endpoint
@app.post("/predict")
def predict(request: PredictRequest):
    features = np.array([request.features])

    # Apply the same preprocessing steps
    preprocessed_features = preprocessor.transform(features)
    prediction = model.predict(preprocessed_features)
    return {"prediction": prediction[0]}

# To run: uvicorn fastapi_app:app --reload



