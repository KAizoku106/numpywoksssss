import streamlit as st
import joblib

model = joblib.load("grade_model.pkl")

scaler= joblib.load("scaler.pkl")
st.title(":red [grade preditor ]")
study_time_weekly = st.number_input("enter weekly study time ")
absenece =st.number_input("enter no of absence ")
tutoring = st.number_input("tutoring or not,if yes enter 1 ")
parental_support_level = st.number_input("enter parental support level ")
extra_curricular_activity = st.number_input("wheather student participate in extra curricular activities if yes is one ")


if st.button("PREDICT GRADE"):
    test_data= [[study_time_weekly,absenece,tutoring,parental_support_level,extra_curricular_activity]]

    result=model.predict(scaler.transform(test_data))[0]
    
    grade_map = {0:"A",1:"B",2:"C",3:"D"}
    st.success(f"Your grade predicted as {grade_map.get(result)}")
