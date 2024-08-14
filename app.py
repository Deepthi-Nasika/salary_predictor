import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page
from metrics_page import show_metrics_page

page = st.sidebar.selectbox("Select functionality", ("Explore", "Predict", "Model Performance"))

if page == "Predict":
    show_predict_page()
elif page == "Explore":
    show_explore_page()
else:
    show_metrics_page()