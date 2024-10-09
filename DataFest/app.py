from fastapi import FastAPI
import joblib
import numpy as np
from pydantic import BaseModel
import pandas as pd
import logging

model = joblib.load('best_stacking_model.pkl')  
preprocessor = joblib.load('preprocessor.pkl')  

# Initialize FastAPI app
app = FastAPI()

# Define request body structure
class PredictRequest(BaseModel):
    features: list  

feature_columns = ['Gender_x', 'Class_Section', 'Class_Level', 'Religion', 'Tribe',
       'State_of_Origin', 'Parent_Occupation', 'Parent_Income',
       'Attendance_Rate', 'Special_Needs', 'Teacher_Student_Ratio',
       'Average_Teacher_Experience_Years', 'Average_Class_Size',
       'School_Funding_Per_Student', 'School_Extracurricular_Activities',
       'Parental_Involvement_Score', 'School_Facilities_Rating',
       'Internet_Access_In_School', 'School_Distance_From_Home_km',
       'Student_Attendance_Rate', 'Disciplinary_Actions_Taken',
       'Student_Performance_Score', 'Activity_Type', 'Activity_Category',
       'Frequency_of_Participation', 'Duration_per_Session (Hours)',
       'Impact_on_Performance', 'Teacher_Supervisor', 'Parental_Support',
       'Marital_Status', 'Education_Level', 'Gender_y', 'Age',
       'Subject_Taught', 'Degree', 'Parental_Status', 'Teacher_Training',
       'Distance_From_Home_to_School_km', 'Disability', 'Health_Issue',
       'Resumption_Time', 'Have_Lesson_Note', 'Salary_NGN',
       'Teaching_Experience_Years', 'Years_Since_Admission']

# Prediction endpoint
@app.post("/predict")
def predict(request: PredictRequest):
    try:
        # Log the received features
        logging.info(f"Received features: {request.features}")
        features = np.array([request.features])
        features_df = pd.DataFrame(features, columns=feature_columns)

        preprocessed_features = preprocessor.transform(features_df)
        logging.info(f"Preprocessed features: {preprocessed_features}")
        prediction = model.predict(preprocessed_features)
        logging.info(f"Prediction: {prediction}")
        return {"prediction": prediction[0]}
    except Exception as e:
        logging.error(f"Error during prediction: {str(e)}")
        return {"error": str(e)}





