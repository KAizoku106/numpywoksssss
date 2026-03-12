import streamlit as st
st.title("Calculator")

num1=st.number_input("enter number ") 
num2 =st.number_input("enter number   2 " )
choice=   st.selectbox("select your option ",["ADD","SUB","DIV"])
if st.button("Choice"):
    if choice=="ADD":
        result=num1+num2
        st.success(f"result {result}")
    elif choice=="SUB":
        result=num1-num2
        st.success(f"result {result}")
    elif choice=="DIV":
        result = num1/num2
        st.success(f"result {result}")        