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

feature_columns = [
    "Gender",                        "Category",                   "Education_Level",      "Religion",              "Ethnicity",
    "State_of_Origin",               "Occupation",                 "Income",               "Exam_Score",           "Has_Credit",
    "Age",                           "Dependents",                 "Years_of_Work_Experience", "Monthly_Expense",    "Owns_House",
    "Family_Size",                   "Children",                   "Has_Car",             "Rooms",                "Last_Exam_Score",
    "Fail_Count",                    "Study_Hours",                "Favorite_Sport",      "Learning_Type",        "Exercise_Frequency",
    "Days_Exercised",                "Mood",                       "Has_Friends",         "Family_Strength",      "Marital_Status",
    "Degree",                        "Father's_Gender",           "Father's_Age",        "Subject",              "Parent_Degree",
    "Parent_Paid_Tuition",           "Parent_Available",          "Household_Size",      "Household_Earnings",   "Has_Electricity",
    "School_Start_Time",             "Living_With_Parents",       "Income_Limit",        "Homework_Hours",       "Test_Score",
    "Disciplinary_Actions_Taken",    "Student_Attendance_Rate",    "Health_Issue",       "Distance_From_Home_to_School_km", "Parental_Support",
    "Have_Lesson_Note",              "Teacher_Training",          "Salary_NGN",          "Duration_per_Session (Hours)", "Parental_Involvement_Score",
    "Tribe",                         "Average_Teacher_Experience_Years", "School_Facilities_Rating", "Teaching_Experience_Years", "Subject_Taught",
    "Resumption_Time",               "Special_Needs",             "Parent_Occupation",   "Attendance_Rate",      "School_Distance_From_Home_km",
    "Teacher_Student_Ratio",         "Activity_Category",          "School_Funding_Per_Student", "Student_Performance_Score", "Class_Level",
    "Parental_Status",               "Gender_y",                  "Activity_Type",       "Internet_Access_In_School", "Parent_Income",
    "School_Extracurricular_Activities", "Average_Class_Size",     "Impact_on_Performance", "Frequency_of_Participation", "Disability",
    "Gender_x",                      "Class_Section",             "Teacher_Supervisor" ]

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





