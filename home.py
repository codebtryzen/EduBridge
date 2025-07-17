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
            margin-bottom: 0.4em;
            text-align: center;
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
        .feature-icon {
            font-size: 3em;
            margin-bottom: 10px;
            color: #2196F3;
        }

        /* Button background images */
        div[data-testid="stButton"][key="quiz"] > button {
            background-image: url("https://cdn-icons-png.flaticon.com/512/3135/3135715.png");
            background-size: cover;
            background-position: center;
            background-color: rgba(0,0,0,0.4);
            background-blend-mode: overlay;
        }
        div[data-testid="stButton"][key="translate"] > button {
            background-image: url("https://cdn-icons-png.flaticon.com/512/484/484582.png");
            background-size: cover;
            background-position: center;
            background-color: rgba(0,0,0,0.4);
            background-blend-mode: overlay;
        }
        div[data-testid="stButton"][key="career"] > button {
            background-image: url("https://cdn-icons-png.flaticon.com/512/2620/2620999.png");
            background-size: cover;
            background-position: center;
            background-color: rgba(0,0,0,0.4);
            background-blend-mode: overlay;
        }
        div[data-testid="stButton"][key="progress"] > button {
            background-image: url("https://cdn-icons-png.flaticon.com/512/3135/3135719.png");
            background-size: cover;
            background-position: center;
            background-color: rgba(0,0,0,0.4);
            background-blend-mode: overlay;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='big-title'>EduBridgeAI</div>", unsafe_allow_html=True)
    st.markdown("<div class='tagline'>Empowering rural learners through personalized AI education</div>", unsafe_allow_html=True)

    # st.image(
    #     "https://images.unsplash.com/photo-1581091226825-0ef34f62d2d8?fit=crop&w=1200&h=400",
    #     use_container_width=True
    # )

    st.markdown("### Why EduBridgeAI?")
    st.write("""
        EduBridgeAI helps students in rural areas:
        -  **Personalized Quizzes** tailored to their level.
        - **Language Translation** for better understanding.
        - **Career Recommendations** based on their interests.
        - **Progress Tracking** to keep them motivated.
    """)

    st.markdown("## Explore Features")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("📝\n\n**Quiz**\n\nTest your knowledge with interactive AI quizzes.", key="quiz"):
            st.session_state.page = "Quiz"

    with col2:
        if st.button("🌐\n\n**Translate**\n\nTranslate learning content into regional languages.", key="translate"):
            st.session_state.page = "Translate"

    col3, col4 = st.columns(2)

    with col3:
        if st.button("🚀\n\n**Career Path**\n\nDiscover career paths based on your interests and skills.", key="career"):
            st.session_state.page = "Career Path"

    with col4:
            if st.button("📊\n\n**Scan2Quiz**\n\nUpload your Image and Get Questions.", key="scan2quiz"):
                st.session_state.page = "scan2quiz"


    st.markdown("---")
    st.info("✨ Click any card above or use the sidebar to explore EduBridgeAI!")
