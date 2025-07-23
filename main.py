# main.py
import streamlit as st
import home
import quiz_generator
import translator
import recommender
import notes_scanner
from botpress_embed import load_botpress_chatbot

# Set page configuration only once
st.set_page_config(page_title="EduBridgeAI", layout="wide")

# Inject custom CSS to remove whitespace and padding
st.markdown("""
    <style>
        /* Remove Streamlit default padding */
        .main > div {
            padding-top: 0rem;
            padding-bottom: 0rem;
        }

        .block-container {
            padding: 1rem;
        }

        /* Hide Streamlit footer and hamburger menu */
        footer, #MainMenu {
            visibility: hidden;
        }

        /* Reduce sidebar spacing */
        .css-1d391kg {
            padding-top: 1rem !important;
            padding-bottom: 1rem !important;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar Navigation
menu = ["Home", "Quiz", "Translate", "Career Path", "Scan Notes"]

if "page" not in st.session_state:
    st.session_state.page = "Home"

with st.sidebar:
    st.markdown("## 📚 EduBridgeAI")
    page_choice = st.radio("Navigate", menu, index=menu.index(st.session_state.page))
    if page_choice != st.session_state.page:
        st.session_state.page = page_choice
        st.rerun()

# Route Pages
try:
    if st.session_state.page == "Home":
        home.show_home()

    elif st.session_state.page == "Quiz":
        quiz_generator.generate_quiz()

    elif st.session_state.page == "Translate":
        translator.translate_ui()

    elif st.session_state.page == "Career Path":
        recommender.show_recommendations()

    elif st.session_state.page == "Scan Notes":
        notes_scanner.scan_notes_ui()

except Exception as e:
    st.error(f"An error occurred: {e}")

# Load Botpress Chatbot (No extra whitespace)
load_botpress_chatbot()
