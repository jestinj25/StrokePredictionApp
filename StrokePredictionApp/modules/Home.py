import streamlit as st

st.header("About the App")
st.image("images/stroke-img.png")
st.markdown("""
This interactive web application helps assess an individual’s risk of having a stroke based on key health and demographic factors.
 It uses a machine learning model trained on real-world medical data to provide a prediction that can support early intervention and awareness.

**Key Features**
            
Accepts user inputs such as age, BMI, smoking status, hypertension, glucose levels, and more.

Predicts whether a user is at high or low risk of stroke.

Displays the prediction result instantly.
""")

