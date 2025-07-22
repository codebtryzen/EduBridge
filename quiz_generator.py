import streamlit as st
import matplotlib.pyplot as plt
from reportlab.pdfgen import canvas
from io import BytesIO
import random

# --------------- 1. Quiz Data Bank (all your original questions) ---------------

quiz_bank = {
    "AI Basics": [
        {"question": "What is AI?", "options": ["Artificial Intelligence", "Apple Inc", "All India", "None"], "answer": "Artificial Intelligence"},
        {"question": "Which of these is NOT a branch of AI?", "options": ["Machine Learning", "Robotics", "Database Management", "Computer Vision"], "answer": "Database Management"},
        {"question": "Which language is most popular for AI development?", "options": ["Python", "C", "JavaScript", "COBOL"], "answer": "Python"},
        {"question": "AI systems mainly rely on?", "options": ["Data", "Magic", "Luck", "Fiction"], "answer": "Data"},
        {"question": "Which is NOT a type of AI?", "options": ["Narrow AI", "General AI", "Super AI", "Alien AI"], "answer": "Alien AI"},
        {"question": "Turing Test is used to measure?", "options": ["Speed", "Intelligence", "Strength", "Cost"], "answer": "Intelligence"},
        {"question": "Which company created AlphaGo?", "options": ["DeepMind", "IBM", "Apple", "Meta"], "answer": "DeepMind"},
        {"question": "Which AI domain relates to understanding text?", "options": ["NLP", "CV", "RL", "IoT"], "answer": "NLP"},
        {"question": "Which AI technique mimics human neurons?", "options": ["Neural Networks", "SQL", "Java", "HTML"], "answer": "Neural Networks"},
        {"question": "AI can be used in?", "options": ["Healthcare", "Finance", "Education", "All of these"], "answer": "All of these"}
    ],
    "Machine Learning": [
        {"question": "Which algorithm is used for classification?", "options": ["K-Nearest Neighbors", "Apriori", "QuickSort", "Dijkstra"], "answer": "K-Nearest Neighbors"},
        {"question": "Overfitting means?", "options": ["Fits noise in training data", "Performs well on unseen data", "Training stopped early", "None of the above"], "answer": "Fits noise in training data"},
        {"question": "Which is supervised learning?", "options": ["Regression", "Clustering", "Anomaly Detection", "Association"], "answer": "Regression"},
        {"question": "What is feature scaling?", "options": ["Normalizing data", "Sorting data", "Encrypting data", "Compressing data"], "answer": "Normalizing data"},
        {"question": "Which library is used for ML in Python?", "options": ["scikit-learn", "NumPy", "Photoshop", "TikTok"], "answer": "scikit-learn"},
        {"question": "Which is an unsupervised learning algorithm?", "options": ["K-Means", "Decision Tree", "Random Forest", "Logistic Regression"], "answer": "K-Means"},
        {"question": "Cross-validation helps with?", "options": ["Model validation", "Data cleaning", "Feature engineering", "Visualization"], "answer": "Model validation"},
        {"question": "Which metric is for classification?", "options": ["Accuracy", "RMSE", "MAPE", "MAE"], "answer": "Accuracy"},
        {"question": "Which method avoids overfitting?", "options": ["Regularization", "Multiplication", "Hashing", "Encryption"], "answer": "Regularization"},
        {"question": "ML models learn from?", "options": ["Data", "Movies", "Paintings", "Songs"], "answer": "Data"}
    ],
    "Data Science": [
        {"question": "What is the first step in data science?", "options": ["Data Collection", "Modeling", "Training", "Deployment"], "answer": "Data Collection"},
        {"question": "Which library is best for data manipulation?", "options": ["Pandas", "TensorFlow", "Matplotlib", "Scikit-learn"], "answer": "Pandas"},
        {"question": "What is EDA?", "options": ["Exploratory Data Analysis", "Extended Data Access", "Efficient Data Algorithm", "None"], "answer": "Exploratory Data Analysis"},
        {"question": "What is a DataFrame?", "options": ["2D data structure", "Image file", "Database", "None"], "answer": "2D data structure"},
        {"question": "Which visual library is for plots?", "options": ["Matplotlib", "Numpy", "Scikit", "Pandas"], "answer": "Matplotlib"},
        {"question": "What does CSV stand for?", "options": ["Comma Separated Values", "Code Stored Values", "Combined Sorted View", "None"], "answer": "Comma Separated Values"},
        {"question": "Which Python lib is used for statistics?", "options": ["statsmodels", "cv2", "pygame", "flask"], "answer": "statsmodels"},
        {"question": "What is null value?", "options": ["Missing data", "Duplicate", "Cleaned data", "None"], "answer": "Missing data"},
        {"question": "Outlier is?", "options": ["An unusual data point", "Middle value", "Average", "Clean data"], "answer": "An unusual data point"},
        {"question": "Which is used for hypothesis testing?", "options": ["t-test", "dropna", "merge", "append"], "answer": "t-test"}
    ],
    "Python Programming": [
        {"question": "What is a list?", "options": ["Ordered collection", "Set", "Loop", "Variable"], "answer": "Ordered collection"},
        {"question": "Which keyword defines function?", "options": ["def", "fun", "define", "function"], "answer": "def"},
        {"question": "Which symbol is used for comment?", "options": ["#", "//", "/*", "<!--"], "answer": "#"},
        {"question": "What is output of print(2**3)?", "options": ["8", "6", "9", "5"], "answer": "8"},
        {"question": "Which loop is used to iterate list?", "options": ["for", "while", "loop", "repeat"], "answer": "for"},
        {"question": "Which data type is immutable?", "options": ["Tuple", "List", "Dict", "Set"], "answer": "Tuple"},
        {"question": "Which module is for random numbers?", "options": ["random", "math", "time", "os"], "answer": "random"},
        {"question": "What does len() return?", "options": ["Length of item", "Data type", "Memory size", "None"], "answer": "Length of item"},
        {"question": "What is indentation in Python?", "options": ["Block structure", "Spacing", "Loop", "Function"], "answer": "Block structure"},
        {"question": "Which is NOT a valid type?", "options": ["integer", "decimal", "float", "string"], "answer": "decimal"}
    ],
    "Cybersecurity": [
        {"question": "What is a firewall?", "options": ["Security system", "Game", "Antivirus", "Software bug"], "answer": "Security system"},
        {"question": "Phishing means?", "options": ["Fraudulent email", "Fishing game", "Virus", "Firewall"], "answer": "Fraudulent email"},
        {"question": "What is malware?", "options": ["Malicious software", "Update file", "Antivirus", "Firewall"], "answer": "Malicious software"},
        {"question": "SSL is used for?", "options": ["Securing websites", "Speed", "Storage", "Compression"], "answer": "Securing websites"},
        {"question": "What is a strong password?", "options": ["Mixed characters", "1234", "admin", "name"], "answer": "Mixed characters"},
        {"question": "Two-factor auth adds?", "options": ["Extra security", "More speed", "Longer password", "Bug"], "answer": "Extra security"},
        {"question": "Which of these is a threat?", "options": ["Ransomware", "Excel", "Word", "Zoom"], "answer": "Ransomware"},
        {"question": "HTTPS stands for?", "options": ["HyperText Transfer Protocol Secure", "High Tech Transport Protocol Secure", "None", "Hyper Tool Test Secure"], "answer": "HyperText Transfer Protocol Secure"},
        {"question": "What is brute-force attack?", "options": ["Password guessing", "Virus", "Firewall", "Phishing"], "answer": "Password guessing"},
        {"question": "VPN stands for?", "options": ["Virtual Private Network", "Visual Protocol Node", "Very Private Network", "Verified Private Net"], "answer": "Virtual Private Network"}
    ]
}

# --------------- 2. Quiz UI Logic ---------------


def generate_quiz():
    # ---------- 🎨 Gradient Animation Title & Line ----------
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@600&display=swap');

        .quiz-title {
            font-family: 'Poppins', sans-serif;
            font-size: 2.6rem;
            font-weight: 700;
            text-align: center;
            margin: 0 0 0.4em;
            background: linear-gradient(270deg, #00c6ff, #0072ff, #8e2de2, #4a00e0, #00c6ff);
            background-size: 400% 400%;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            animation: gradientShift 9s ease infinite;
        }

        .gradient-line {
            height: 4px;
            width: 100%;
            border: none;
            background: linear-gradient(270deg, #00c6ff, #0072ff, #8e2de2, #4a00e0, #00c6ff);
            background-size: 400% 400%;
            animation: gradientShift 9s ease infinite;
            margin: 0 auto 2rem;
        }

        @keyframes gradientShift {
            0% {background-position: 0% 50%;}
            50% {background-position: 100% 50%;}
            100% {background-position: 0% 50%;}
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<h1 class="quiz-title">🧠 AI Quiz Game</h1>', unsafe_allow_html=True)
    st.markdown('<hr class="gradient-line">', unsafe_allow_html=True)

    # 👇 rest of your quiz logic stays as-is


    # 👉 If no category picked yet → show selector
    if "current_cat" not in st.session_state:
        categories = list(quiz_bank.keys())
        chosen_cat = st.selectbox(
            "📚 Select a Category to Start",
            ["-- Select --"] + categories,
            index=0
        )

        if chosen_cat != "-- Select --":
            st.session_state.current_cat = chosen_cat
            st.session_state.remaining_questions = quiz_bank[chosen_cat][:]
            random.shuffle(st.session_state.remaining_questions)
            st.session_state.current_q_index = 0
            st.session_state.answered = False
            st.session_state.feedback = ""
            st.session_state.selected_option = None
            st.session_state.correct_count = 0
            st.session_state.incorrect_count = 0
            st.session_state.shuffled_questions = []
            st.rerun()

        else:
            st.info("Please select a category to start the quiz.")
            return

    else:
        # ✅ BACK ARROW top left with HTML + simple style
        st.markdown("""
            <style>
                .back-arrow {
                    position: fixed;
                    top: 15px;
                    left: 15px;
                    font-size: 24px;
                    color: white;
                    text-decoration: none;
                    background: none;
                }
                .back-arrow:hover {
                    color: #4CAF50;
                    cursor: pointer;
                }
            </style>
            <a href="#" class="back-arrow" onclick="window.location.reload();">←</a>
        """, unsafe_allow_html=True)

        if st.button("🔙"):
            for key in ["current_cat", "remaining_questions", "current_q_index",
                        "answered", "feedback", "selected_option",
                        "correct_count", "incorrect_count", "shuffled_questions"]:
                if key in st.session_state:
                    del st.session_state[key]
            st.rerun()

    # 👉 Show questions
    if st.session_state.current_q_index < len(st.session_state.remaining_questions):

        q_index = st.session_state.current_q_index

        if len(st.session_state.shuffled_questions) <= q_index:
            q_dict = st.session_state.remaining_questions[q_index]
            options = q_dict["options"][:]
            random.shuffle(options)
            st.session_state.shuffled_questions.append({
                "question": q_dict["question"],
                "options": options,
                "correct_answer": q_dict["answer"]
            })

        q_dict = st.session_state.shuffled_questions[q_index]

        st.markdown(
            f"<h3 style='color:#1976D2;'>Question {q_index + 1} of {len(st.session_state.remaining_questions)}</h3>",
            unsafe_allow_html=True
        )
        st.markdown(
            f"<p style='font-size: 20px;'>{q_dict['question']}</p>",
            unsafe_allow_html=True
        )

        selected = st.radio(
            "",
            q_dict["options"],
            index=None,
            key=f"radio_q_{q_index}",
            horizontal=False
        )

        col_submit, col_next = st.columns([1, 1])

        with col_submit:
            if st.button("✅ Submit Answer", use_container_width=True, disabled=st.session_state.answered or selected is None):
                st.session_state.answered = True
                st.session_state.selected_option = selected
                if selected == q_dict["correct_answer"]:
                    st.session_state.feedback = "✅ **Correct! Great job.**"
                    st.session_state.correct_count += 1
                else:
                    st.session_state.feedback = f"❌ **Incorrect.** The correct answer is **{q_dict['correct_answer']}**."
                    st.session_state.incorrect_count += 1

        with col_next:
            if st.session_state.answered:
                if st.button("➡️ Next Question", use_container_width=True):
                    st.session_state.current_q_index += 1
                    st.session_state.answered = False
                    st.session_state.feedback = ""
                    st.session_state.selected_option = None
                    st.rerun()

        if st.session_state.feedback:
            st.markdown("<hr>", unsafe_allow_html=True)
            st.info(st.session_state.feedback)

    else:
        st.success("🎉 You have completed the quiz!")
        show_dashboard()

# ---------------- 3. Dashboard ----------------

def show_dashboard():
    correct = st.session_state.get("correct_count", 0)
    incorrect = st.session_state.get("incorrect_count", 0)

    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown(
        "<h2 style='color:#4CAF50;'>📊 Quiz Performance Summary</h2>",
        unsafe_allow_html=True
    )
    st.write(f"✅ **Correct Answers:** {correct}")
    st.write(f"❌ **Incorrect Answers:** {incorrect}")

    # Pie chart
    labels = ['Correct', 'Incorrect']
    sizes = [correct, incorrect]
    colors = ['#4CAF50', '#F44336']

    fig, ax = plt.subplots(figsize=(3, 3), facecolor='white')
    ax.pie(
        sizes,
        labels=labels,
        colors=colors,
        autopct='%1.1f%%',
        startangle=90,
        shadow=True,
        wedgeprops=dict(edgecolor='black', linewidth=1)
    )
    ax.axis('equal')
    pie_buffer = BytesIO()
    fig.savefig(pie_buffer, format='PNG', bbox_inches='tight')
    pie_buffer.seek(0)
    plt.close(fig)

    st.image(pie_buffer, caption="Your Score Pie Chart")

    col1, col2 = st.columns([1, 1])

    with col1:
        if st.button("🔄 Retry Quiz", use_container_width=True):
            for key in ["current_cat", "remaining_questions", "current_q_index",
                        "answered", "feedback", "selected_option",
                        "correct_count", "incorrect_count", "shuffled_questions"]:
                if key in st.session_state:
                    del st.session_state[key]
            st.rerun()

    with col2:
        buffer = BytesIO()
        c = canvas.Canvas(buffer)
        c.setFont("Helvetica-Bold", 14)
        c.drawString(100, 780, "Quiz Performance Report")
        c.setFont("Helvetica", 12)
        c.drawString(100, 750, f"Category: {st.session_state.get('current_cat', '-')}")
        c.drawString(100, 730, f"Correct Answers: {correct}")
        c.drawString(100, 710, f"Incorrect Answers: {incorrect}")
        total = correct + incorrect
        percentage = (correct / total) * 100 if total > 0 else 0
        c.drawString(100, 690, f"Score: {percentage:.2f}%")

        from reportlab.lib.utils import ImageReader
        pie_image = ImageReader(pie_buffer)
        c.drawImage(pie_image, 100, 500, width=200, height=200)

        c.save()
        buffer.seek(0)

        st.download_button(
            label="📄 Download PDF Report",
            data=buffer,
            file_name="quiz_report.pdf",
            mime="application/pdf",
            use_container_width=True
        )

# ---------------- 4. Run App ----------------

if __name__ == "__main__":
    generate_quiz()