import streamlit as st
import requests

# Streamlit app title
st.title("Academic Performance Predictor")

# Create input fields for numerical and categorical features
feature1 = st.number_input('Age', min_value=0)  # Numerical feature
feature2 = st.number_input('Attendance Rate', min_value=0)  # Numerical feature
feature3 = st.selectbox('Class Level', ['JSS1', 'JSS2', 'SS1', 'SS2', 'SS3'])  # Categorical feature
feature4 = st.selectbox('Class Section', ['A', 'B', 'C', 'D'])  # Categorical feature
# Add more input fields based on your model's features as required

# Collect the features into a list
features = [feature1, feature2, feature3, feature4]

# Button to trigger prediction
if st.button('Predict'):
    # Send the features to the FastAPI backend via a POST request
    response = requests.post("http://127.0.0.1:8000/predict", json={"features": features})

    if response.status_code == 200:
        prediction = response.json()["prediction"]
        st.success(f"Predicted Academic Performance: {prediction}")
    else:
        st.error("Failed to get prediction. Please try again.")

