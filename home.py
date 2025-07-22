# home.py

import streamlit as st

def show_home():
    st.markdown("""
        <style>
        .big-title {
            font-size: 3.5em;
            font-weight: 900;
            background: linear-gradient(90deg, #00b09b, #96c93d);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-align: center;
            margin-bottom: 0.5em;
        }
        .tagline {
            font-size: 1.4em;
            color: white;
            text-align: center;
            margin-bottom: 2em;
        }
        .stButton > button {
            border-radius: 15px;
            padding: 25px;
            margin-bottom: 20px;
            width: 100%;
            text-align: center;
            transition: all 0.3s;
            font-size: 1em;
            border: none;
            color: white;
        }
        .stButton > button:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 20px rgba(0,0,0,0.2);
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='big-title'>EduBridgeAI</div>", unsafe_allow_html=True)
    st.markdown("<div class='tagline'>Empowering rural learners through personalized AI education</div>", unsafe_allow_html=True)

    st.markdown("### Why EduBridgeAI?")
    st.write("""
        EduBridgeAI helps students in rural areas:
        -  **Personalized Quizzes** tailored to their level.
        - **Language Translation** for better understanding.
        - **Career Recommendations** based on their interests.
        - **Progress Tracking** to keep them motivated.
    """)

    st.markdown("---")
    st.markdown("## 🚀 Explore Features")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("📝 Quiz\nTest your knowledge", key="quiz"):
            st.session_state.page = "Quiz"
            st.rerun()

    with col2:
        if st.button("🌐 Translate\nRegional languages", key="translate"):
            st.session_state.page = "Translate"
            st.rerun()

    col3, col4 = st.columns(2)

    with col3:
        if st.button("🚀 Career Path\nBased on your skills", key="career"):
            st.session_state.page = "Career Path"
            st.rerun()

    with col4:
        if st.button("📄 Scan Notes\nConvert to Q&A", key="scan_notes"):
            st.session_state.page = "Scan Notes"
            st.rerun()

    st.info("✨ Click any card above or use the sidebar to explore EduBridgeAI!")
