# pages/home.py
import streamlit as st

def app():
    st.title('Welcome to Our Prediction Application')
    st.write("""
    This application allows you to make predictions and view the prediction history.
    
    - Use the **Make Prediction** page to submit new predictions.
    - Go to the **View History** page to see past predictions.
    """)
