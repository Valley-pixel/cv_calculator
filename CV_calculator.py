import streamlit as st

st.title("CV Calculator")

mean = st.number_input("Enter Mean value:", min_value=0.0)
sd = st.number_input("Enter Standard Deviation:", min_value=0.0)

if mean > 0:
    cv = (sd / mean) * 100
    st.write("CV% =", round(cv, 2))
else:
    st.write("Please enter a mean greater than 0.")
