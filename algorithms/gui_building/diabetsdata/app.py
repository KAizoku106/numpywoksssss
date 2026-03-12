import streamlit as st
import joblib

model = joblib.load("grade_model.pkl")
scaler = joblib.load("scaler.pkl")

st.title("dibetic assesment ")
pregnancy= st.number_input(" enter  no of pregnancies you had ")
glucose = st.number_input("enter your glucose level ")
bp = st.number_input("enter you bp level")
skin_thickness = st.number_input("enter skin thicknesslevel ")
insulin = st.number_input("enterr inslulin level ")
bmi = st.number_input("enter your bmi rate ")
dibetic_pedigree = st.number_input("enter diabetic pedigree function ")
age = st.number_input ("enter your age ")
#"'Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin',
 #      'BMI', 'DiabetesPedigreeFunction', 'Age'"

if st.button("PREDICT GRADE"):
    test_data= [[pregnancy,glucose,bp,skin_thickness,insulin,bmi,dibetic_pedigree,age]]

    result=model.predict(scaler.transform(test_data))[0]
    
    grade_map = {0:"No",1:"yes"}
    st.success(f"Your diabetic asssesment predicted as {grade_map.get(result)}")

