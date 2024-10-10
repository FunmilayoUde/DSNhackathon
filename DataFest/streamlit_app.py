import streamlit as st
import requests

# Streamlit app title
st.title("Academic Performance Predictor")

# Create input fields for each feature based on the 45 expected features
# Categorical features
import streamlit as st

# Creating select boxes for all features
gender = st.selectbox("Gender", ["Female", "Male"])  # Example options
category = st.selectbox("Category", ["A", "B", "C"])  # Example options
education_level = st.selectbox("Education Level", ["SS1", "SS2", "SS3"])  # Example options
religion = st.selectbox("Religion", ["Christianity", "Islam", "Other"])  # Example options
ethnicity = st.selectbox("Ethnicity", ["Igbo", "Yoruba", "Hausa"])  # Example options
state_of_origin = st.selectbox("State of Origin", ["Anambra", "Lagos", "Kano"])  # Example options
occupation = st.selectbox("Occupation", ["Trader", "Teacher", "Engineer"])  # Example options
income = st.selectbox("Income", [50000, 60000, 70000])  # Example options
exam_score = st.selectbox("Exam Score", [85.5, 90.0, 75.0])  # Example options
has_credit = st.selectbox("Has Credit", ["Yes", "No"])  # Example options
age = st.selectbox("Age", [15, 16, 17, 18])  # Example options
dependents = st.selectbox("Dependents", [0, 1, 2, 3])  # Example options
years_of_work_experience = st.selectbox("Years of Work Experience", [0, 1, 2, 3])  # Example options
monthly_expense = st.selectbox("Monthly Expense", [2000, 2500, 3000])  # Example options
owns_house = st.selectbox("Owns House", ["Yes", "No"])  # Example options
family_size = st.selectbox("Family Size", [1, 2, 3, 4, 5])  # Example options
children = st.selectbox("Children", [0, 1, 2, 3, 4, 5, 6, 7])  # Example options
has_car = st.selectbox("Has Car", ["Yes", "No"])  # Example options
rooms = st.selectbox("Rooms", [1, 2, 3, 4, 5])  # Example options
last_exam_score = st.selectbox("Last Exam Score", [90.2, 85.0, 95.0])  # Example options
fail_count = st.selectbox("Fail Count", [0, 1, 2, 3])  # Example options
study_hours = st.selectbox("Study Hours", [80.0, 90.0, 100.0])  # Example options
favorite_sport = st.selectbox("Favorite Sport", ["Sports", "Music", "Art"])  # Example options
learning_type = st.selectbox("Learning Type", ["Physical", "Visual", "Auditory"])  # Example options
exercise_frequency = st.selectbox("Exercise Frequency", ["Daily", "Weekly", "Monthly"])  # Example options
days_exercised = st.selectbox("Days Exercised", [0, 1, 2, 3, 4, 5, 6, 7])  # Example options
mood = st.selectbox("Mood", ["Positive", "Neutral", "Negative"])  # Example options
has_friends = st.selectbox("Has Friends", ["Yes", "No"])  # Example options
family_strength = st.selectbox("Family Strength", ["Strong", "Average", "Weak"])  # Example options
marital_status = st.selectbox("Marital Status", ["Married", "Single", "Divorced"])  # Example options
degree = st.selectbox("Degree", ["Bachelor's Degree", "Master's Degree", "PhD"])  # Example options
father_gender = st.selectbox("Father's Gender", ["Male", "Female"])  # Example options
father_age = st.selectbox("Father's Age", [30, 40, 50])  # Example options
subject = st.selectbox("Subject", ["Mathematics", "Science", "English"])  # Example options
parent_degree = st.selectbox("Parent Degree", ["PhD", "Masters", "Bachelors"])  # Example options
parent_paid_tuition = st.selectbox("Parent Paid Tuition", ["Yes", "No"])  # Example options
parent_available = st.selectbox("Parent Available", ["Yes", "No"])  # Example options
household_size = st.selectbox("Household Size", [1, 2, 3, 4, 5, 6])  # Example options
household_earnings = st.selectbox("Household Earnings", ["Yes", "No"])  # Example options
has_electricity = st.selectbox("Has Electricity", ["Yes", "No"])  # Example options
school_start_time = st.selectbox("School Start Time", ["8:00 AM", "9:00 AM"])  # Example options
living_with_parents = st.selectbox("Living With Parents", ["Yes", "No"])  # Example options
income_limit = st.selectbox("Income Limit", [50000, 60000, 70000])  # Example options
homework_hours = st.selectbox("Homework Hours", [1, 2, 3, 4, 5])  # Example options
test_score = st.selectbox("Test Score", [5, 10, 15])  # Example options
disciplinary_actions_taken = st.selectbox("Disciplinary Actions Taken", ["None", "Warning", "Suspension"])  # Example options
student_attendance_rate = st.selectbox("Student Attendance Rate", [None, "75%", "80%"])  # Example options
health_issue = st.selectbox("Health Issue", ["Yes", "No"])  # Example options
distance_from_home_to_school_km = st.selectbox("Distance From Home to School (km)", [1, 2, 3, 4, 5])  # Example options
parental_support = st.selectbox("Parental Support", ["High", "Medium", "Low"])  # Example options
have_lesson_note = st.selectbox("Have Lesson Note", ["Yes", "No"])  # Example options
teacher_training = st.selectbox("Teacher Training", ["Yes", "No"])  # Example options
salary_ngn = st.selectbox("Salary (NGN)", [None, 50000, 60000])  # Example options
duration_per_session_hours = st.selectbox("Duration per Session (Hours)", [1, 2, 3])  # Example options
parental_involvement_score = st.selectbox("Parental Involvement Score", [None, 1, 2, 3])  # Example options
tribe = st.selectbox("Tribe", ["Igbo", "Yoruba", "Hausa"])  # Example options
average_teacher_experience_years = st.selectbox("Average Teacher Experience (Years)", [0, 1, 2])  # Example options
school_facilities_rating = st.selectbox("School Facilities Rating", [1, 2, 3, 4, 5])  # Example options
teaching_experience_years = st.selectbox("Teaching Experience (Years)", [0, 1, 2])  # Example options
subject_taught = st.selectbox("Subject Taught", ["Mathematics", "Science", "English"])  # Example options
resumption_time = st.selectbox("Resumption Time", ["8:00 AM", "9:00 AM"])  # Example options
special_needs = st.selectbox("Special Needs", ["Yes", "No"])  # Example options
parent_occupation = st.selectbox("Parent Occupation", ["Teacher", "Doctor", "Engineer"])  # Example options
attendance_rate = st.selectbox("Attendance Rate", [None, "75%", "80%"])  # Example options
school_distance_from_home_km = st.selectbox("School Distance From Home (km)", [1, 2, 3, 4, 5])  # Example options
teacher_student_ratio = st.selectbox("Teacher Student Ratio", [None, 1, 15])  # Example options
activity_category = st.selectbox("Activity Category", ["Academic", "Sports", "Arts"])  # Example options
school_funding_per_student = st.selectbox("School Funding Per Student", [None, 5000, 6000])  # Example options
student_performance_score = st.selectbox("Student Performance Score", [None, 1, 2, 3])  # Example options
class_level = st.selectbox("Class Level", [None, "SS1", "SS2", "SS3"])  # Example options
parental_status = st.selectbox("Parental Status", ["Alive", "Deceased"])  # Example options
gender_y = st.selectbox("Gender_y", ["Male", "Female"])  # Example options
activity_type = st.selectbox("Activity Type", ["Sport", "Study", "Work"])  # Example options
internet_access_in_school = st.selectbox("Internet Access In School", ["Yes", "No"])  # Example options
parent_income = st.selectbox("Parent Income", [50000, 60000, 70000])  # Example options
school_extracurricular_activities = st.selectbox("School Extracurricular Activities", ["Yes", "No"])  # Example options
average_class_size = st.selectbox("Average Class Size", [20, 30, 40])  # Example options
impact_on_performance = st.selectbox("Impact on Performance", ["High", "Medium", "Low"])  # Example options
frequency_of_participation = st.selectbox("Frequency of Participation", ["Daily", "Weekly", "Monthly"])  # Example options
disability = st.selectbox("Disability", ["Yes", "No"])  # Example options
gender_x = st.selectbox("Gender_x", ["Male", "Female"])  # Example options
class_section = st.selectbox("Class Section", ["A", "B", "C"])  # Example options
teacher_supervisor = st.selectbox("Teacher Supervisor", ["Mr. Smith", "Mrs. Johnson", "Ms. Brown"])  # Example options

# Collect the features into a list in the order the model expects
features = [
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
    "Gender_x",                      "Class_Section",             "Teacher_Supervisor"
]




# Button to trigger prediction
if st.button('Predict'):
    # Send the features to the FastAPI backend via a POST request
    response = requests.post("http://127.0.0.1:8000/predict", json={"features": features})

    # Display the prediction result
    if response.status_code == 200:
        prediction = response.json()["prediction"]
    
    # Classify performance based on the prediction value
    if prediction[0] < 50:
        performance = "Student Performance is bad."
    elif 50 <= prediction[0] < 70:
        performance = "Student Performance is good."
    else:
        performance = "Student had an Excellent Performance."
    
    # Display the prediction and performance classification in Streamlit
    st.success(f"Predicted Academic Performance: {prediction[0]}")
    st.success(performance)
else:
    st.error("Failed to get prediction. Please try again.")

