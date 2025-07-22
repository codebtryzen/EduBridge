import streamlit as st
import streamlit.components.v1 as components

def chatbot_ui():
    if "chat_open" not in st.session_state:
        st.session_state.chat_open = False
        st.session_state.chat_stage = "greet"
        st.session_state.user_name = ""
        st.session_state.chat_log = []

    # --- CSS and JS for floating icon and chatbox ---
    st.markdown("""
        <style>
        .chatbot-float {
            position: fixed;
            bottom: 20px;
            right: 20px;
            width: 60px;
            height: 60px;
            background-image: url('https://cdn-icons-png.flaticon.com/512/4712/4712027.png');
            background-size: cover;
            background-repeat: no-repeat;
            border-radius: 50%;
            box-shadow: 0 4px 10px rgba(0,0,0,0.3);
            animation: bounce 2s infinite;
            cursor: pointer;
            z-index: 9999;
        }
        @keyframes bounce {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-8px); }
        }
        .chatbox-container {
            position: fixed;
            bottom: 90px;
            right: 20px;
            width: 320px;
            background-color: #fefefe;
            border-radius: 15px;
            box-shadow: 0 0 15px rgba(0,0,0,0.25);
            padding: 15px;
            z-index: 9999;
        }
        .chat-message {
            margin-bottom: 10px;
            font-size: 14px;
        }
        </style>

        <div class="chatbot-float" onclick="toggleChat()" title="Chat with us!"></div>

        <script>
        const streamlitEvent = (type, data={}) => {
            const iframe = window.parent.document.querySelector('iframe[srcdoc*="streamlit"]');
            iframe.contentWindow.postMessage({ isStreamlitMessage: true, type, data }, "*");
        };

        function toggleChat() {
            const iframe = window.parent.document.querySelector('iframe[srcdoc*="streamlit"]');
            iframe.contentWindow.postMessage({ type: "streamlit:setComponentValue", value: "toggle" }, "*");
        }
        </script>
    """, unsafe_allow_html=True)

    # Capture toggle event using a hidden component
    toggle = components.html(
        """<script>
            window.addEventListener("message", (event) => {
                if (event.data.type === "streamlit:setComponentValue") {
                    window.parent.postMessage({isStreamlitMessage: true, type: "streamlit:render", value: "toggle"}, "*");
                }
            });
        </script>""",
        height=0,
    )

    # Handle toggle manually
    if st.session_state.get("_component_value") == "toggle":
        st.session_state.chat_open = not st.session_state.chat_open
        st.session_state["_component_value"] = None  # reset

    # --- Chatbox UI ---
    if st.session_state.chat_open:
        st.markdown('<div class="chatbox-container">', unsafe_allow_html=True)

        for msg in st.session_state.chat_log:
            st.markdown(f"<div class='chat-message'><b>{msg['sender']}:</b> {msg['message']}</div>", unsafe_allow_html=True)

        if st.session_state.chat_stage == "greet":
            name = st.text_input("👋 Hi! What's your name?", key="chat_name")
            if name:
                st.session_state.user_name = name
                st.session_state.chat_log.append({"sender": "Bot", "message": f"Nice to meet you, {name}!"})
                st.session_state.chat_log.append({"sender": "Bot", "message": "How can I help you today? (Quiz / Translate / Career / Notes / Feedback)"})
                st.session_state.chat_stage = "ask"

        elif st.session_state.chat_stage == "ask":
            query = st.text_input("💬 Type your question:", key="chat_query")
            if query:
                st.session_state.chat_log.append({"sender": st.session_state.user_name, "message": query})
                if "quiz" in query.lower():
                    reply = "You can try our AI-powered quiz in the 'Quiz' section!"
                elif "translate" in query.lower():
                    reply = "Check the Translate page to convert content into regional languages."
                elif "career" in query.lower():
                    reply = "Visit Career Path for personalized suggestions."
                elif "notes" in query.lower():
                    reply = "Upload notes in the Scan Notes section to generate questions!"
                elif "feedback" in query.lower():
                    reply = "We'd love your feedback!"
                    st.session_state.chat_stage = "feedback"
                else:
                    reply = "Sorry, I didn't get that. Try asking about Quiz, Translate, Career, or Notes."
                st.session_state.chat_log.append({"sender": "Bot", "message": reply})

        elif st.session_state.chat_stage == "feedback":
            feedback = st.text_area("📝 Your feedback:", key="chat_feedback")
            if feedback:
                st.session_state.chat_log.append({"sender": st.session_state.user_name, "message": feedback})
                st.session_state.chat_log.append({"sender": "Bot", "message": "Thanks for your feedback! 😊"})
                st.session_state.chat_stage = "done"

        elif st.session_state.chat_stage == "done":
            st.success("Chat complete! Refresh or click the icon to restart.")

        if st.button("❌ Close Chat"):
            st.session_state.chat_open = False
            st.session_state.chat_stage = "greet"
            st.session_state.chat_log = []

        st.markdown("</div>", unsafe_allow_html=True)
