import streamlit as st
import home
import quiz_generator
import translator
import recommender
import notes_scanner
import chatbot_ui

st.set_page_config(page_title="EduBridgeAI", layout="wide")

menu = ["Home", "Quiz", "Translate", "Career Path", "Scan Notes"]

# Initialize session state
if "page" not in st.session_state:
    st.session_state.page = "Home"

# Sidebar navigation
with st.sidebar:
    st.markdown("## 📚 EduBridgeAI")
    page_choice = st.radio("Navigate", menu, index=menu.index(st.session_state.page))
    if page_choice != st.session_state.page:
        st.session_state.page = page_choice
        st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)

# Page Routing
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

# Floating Chatbot
chatbot_ui.chatbot_ui()
