from fastapi import FastAPI
import joblib
import numpy as np
from pydantic import BaseModel
import logging

model = joblib.load('best_stacking_model.pkl')  
preprocessor = joblib.load('preprocessor.pkl')  

# Initialize FastAPI app
app = FastAPI()

# Define request body structure
class PredictRequest(BaseModel):
    features: list  

# Prediction endpoint
@app.post("/predict")
def predict(request: PredictRequest):
    try:
        # Log the received features
        logging.info(f"Received features: {request.features}")
        features = np.array([request.features])
        preprocessed_features = preprocessor.transform(features)
        logging.info(f"Preprocessed features: {preprocessed_features}")
        prediction = model.predict(preprocessed_features)
        logging.info(f"Prediction: {prediction}")
        return {"prediction": prediction[0]}
    except Exception as e:
        logging.error(f"Error during prediction: {str(e)}")
        return {"error": str(e)}





