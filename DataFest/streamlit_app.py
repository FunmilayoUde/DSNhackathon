import streamlit as st
import requests

# Streamlit app title
st.title("Academic Performance Predictor")

# Create input fields for each feature based on the 45 expected features
# Categorical features
gender_x = st.selectbox('Gender (Student)', ['Male', 'Female'])
class_section = st.selectbox('Class Section', ['A', 'B', 'C', 'D'])
class_level = st.selectbox('Class Level', ['JSS1', 'JSS2', 'SS1', 'SS2', 'SS3'])
religion = st.selectbox('Religion', ['Christianity', 'Islam', 'Other'])
tribe = st.selectbox('Tribe', ['Igbo', 'Yoruba', 'Hausa', 'Other'])
state_of_origin = st.selectbox('State of Origin', ['Anambra', 'Lagos', 'Kano', 'Other'])
parent_occupation = st.text_input('Parent Occupation')
school_extracurricular = st.selectbox('School Extracurricular Activities', ['Yes', 'No'])
internet_access = st.selectbox('Internet Access in School', ['Yes', 'No'])
activity_type = st.selectbox('Activity Type', ['Sports', 'Arts', 'Academic'])
activity_category = st.selectbox('Activity Category', ['Physical', 'Creative', 'Theoretical'])
frequency_of_participation = st.selectbox('Frequency of Participation', ['Weekly', 'Monthly', 'Occasionally'])
impact_on_performance = st.selectbox('Impact on Performance', ['Positive', 'Negative', 'Neutral'])
teacher_supervisor = st.selectbox('Teacher Supervisor', ['Yes', 'No'])
parental_support = st.selectbox('Parental Support', ['Strong', 'Weak', 'Neutral'])
marital_status = st.selectbox('Marital Status', ['Married', 'Single', 'Divorced'])
education_level = st.selectbox('Education Level', ["Bachelor's Degree", 'High School', 'Masters', 'PhD'])
gender_y = st.selectbox('Gender (Teacher)', ['Male', 'Female'])
subject_taught = st.text_input('Subject Taught')
degree = st.selectbox('Degree', ['Bachelors', 'Masters', 'PhD'])
parental_status = st.selectbox('Parental Status', ['Yes', 'No'])
teacher_training = st.selectbox('Teacher Training', ['Yes', 'No'])
disability = st.selectbox('Disability', ['Yes', 'No'])
health_issue = st.selectbox('Health Issue', ['Yes', 'No'])
resumption_time = st.text_input('Resumption Time (e.g. 8:00 AM)')
have_lesson_note = st.selectbox('Has Lesson Note', ['Yes', 'No'])

# Numerical features
parent_income = st.number_input('Parent Income (₦)', min_value=0)
attendance_rate = st.number_input('Attendance Rate (%)', min_value=0.0)
teacher_student_ratio = st.number_input('Teacher Student Ratio', min_value=1)
average_teacher_experience = st.number_input('Average Teacher Experience (Years)', min_value=0.0)
average_class_size = st.number_input('Average Class Size', min_value=1)
school_funding_per_student = st.number_input('School Funding Per Student (₦)', min_value=0)
parental_involvement_score = st.number_input('Parental Involvement Score (1-10)', min_value=1, max_value=10)
school_facilities_rating = st.number_input('School Facilities Rating (1-10)', min_value=1, max_value=10)
school_distance_from_home = st.number_input('School Distance from Home (km)', min_value=0.0)
student_attendance_rate = st.number_input('Student Attendance Rate (%)', min_value=0.0)
disciplinary_actions = st.number_input('Disciplinary Actions Taken', min_value=0)
student_performance_score = st.number_input('Student Performance Score (1-100)', min_value=1, max_value=100)
duration_per_session = st.number_input('Duration per Session (Hours)', min_value=1.0)
distance_from_home_to_school = st.number_input('Distance From Home to School (km)', min_value=0.0)
salary_ngn = st.number_input('Salary (₦)', min_value=0)
teaching_experience_years = st.number_input('Teaching Experience (Years)', min_value=0)
age = st.number_input('Age (Years)', min_value=0)
years_since_admission = st.number_input('Years Since Admission', min_value=0)

# Collect the features into a list in the order the model expects
features = [
    gender_x, class_section, class_level, religion, tribe, state_of_origin, parent_occupation,
    parent_income, attendance_rate, school_extracurricular, teacher_student_ratio,
    average_teacher_experience, average_class_size, school_funding_per_student, parental_involvement_score,
    school_facilities_rating, internet_access, school_distance_from_home, student_attendance_rate,
    disciplinary_actions, student_performance_score, activity_type, activity_category, frequency_of_participation,
    duration_per_session, impact_on_performance, teacher_supervisor, parental_support, marital_status, education_level,
    gender_y, age, subject_taught, degree, parental_status, teacher_training, distance_from_home_to_school,
    disability, health_issue, resumption_time, have_lesson_note, salary_ngn, teaching_experience_years, years_since_admission
]

# Button to trigger prediction
if st.button('Predict'):
    # Send the features to the FastAPI backend via a POST request
    response = requests.post("http://127.0.0.1:8000/predict", json={"features": features})

    # Display the prediction result
    if response.status_code == 200:
        prediction = response.json()["prediction"]
        st.success(f"Predicted Academic Performance: {prediction}")
    else:
        st.error("Failed to get prediction. Please try again.")

