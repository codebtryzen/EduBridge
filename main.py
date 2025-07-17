# main.py

import streamlit as st
import home
import quiz_generator
import translator
import recommender
st.set_page_config(page_title="EduBridgeAI", layout="wide")

# Sidebar navigation
menu = ["Home", "Quiz", "Translate", "Career Path"]

if "page" not in st.session_state:
    st.session_state.page = "Home"

with st.sidebar:
    st.markdown("## 📚 EduBridgeAI")
    page_choice = st.radio("Navigate", menu, index=menu.index(st.session_state.page))
    st.session_state.page = page_choice

try:
    if st.session_state.page == "Home":
        home.show_home()
    elif st.session_state.page == "Quiz":
        quiz_generator.generate_quiz()
    elif st.session_state.page == "Translate":
        translator.translate_ui()
    elif st.session_state.page == "Career Path":
        recommender.show_recommendations()
except Exception as e:
    st.error(f"An error occurred: {e}")
