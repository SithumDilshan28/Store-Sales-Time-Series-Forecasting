import streamlit as st

def app():
    st.title('Prediction History')
    history_file_path = 'prediction_history.txt'
    
    try:
        with open(history_file_path, 'r') as file:
            history_content = file.read()
        st.text_area("History", history_content, height=300)
    except FileNotFoundError:
        st.write("No history found.")
