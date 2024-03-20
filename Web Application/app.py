import streamlit as st
# Import the app functions from the other files
from make_prediction import app as make_prediction_page
from view_history import app as view_history_page

# Home page function defined within app.py
def home_page():
    st.write("Welcome to the Home Page!")

# Use local CSS to hide the hamburger menu and Streamlit footer
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        .stApp { background-color: black; }
    </style>
    """, unsafe_allow_html=True)

# Custom header
st.markdown("""
    <div style="background-color: black; padding: 10px; border-bottom: 2px solid white">
        <h1 style="color: white; text-align: center;">Forecast, Plan, and Prosper: The Future of Your Sales Starts Here</h1>
        <h2 style="color: white; text-align: center;">"Where Every Forecast Leads to Better Performance"</h2>
    </div>
    """, unsafe_allow_html=True)

# Navigation bar (tabs)
tab1, tab2, tab3 = st.tabs(["Home", "Forecast", "View History"])

with tab1:
    home_page()

with tab2:
    # Directly calling the function imported from make_prediction_page.py
    make_prediction_page()

with tab3:
    # Directly calling the function imported from view_history_page.py
    view_history_page()

# Footer
st.markdown('---')
st.markdown('<p style="color: white; text-align: center;">Develop by Sithum Dilshan ©2024</p>', unsafe_allow_html=True)
