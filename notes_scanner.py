import streamlit as st
from PIL import Image
import requests

def scan_notes_ui():
    # Floating warning box using custom HTML + CSS
    st.markdown(
        """
        <style>
        .floating-warning {
            position: fixed;
            top: 20px;
            right: 20px;
            background-color: #fff3cd;
            color: #856404;
            padding: 12px 16px;
            border-radius: 8px;
            font-weight: bold;
            box-shadow: 0 2px 6px rgba(0,0,0,0.2);
            z-index: 1000;
        }
        </style>
        <div class="floating-warning">
            ⚠️ This is just a demo. It requires API for extracting text.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        "<h1 style='text-align:center;'>📄 Scan Notes & Generate Questions</h1>",
        unsafe_allow_html=True
    )

    uploaded_file = st.file_uploader("Upload your handwritten or printed notes image:", type=["png", "jpg", "jpeg"])

    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Notes', use_container_width=True)

        if st.button("🔍 Scan & Generate Questions"):
            with st.spinner("Extracting text and generating questions..."):
                extracted_text = extract_text_from_image(uploaded_file)

                st.subheader("Extracted Text:")
                st.write(extracted_text)

                st.subheader("Generated Questions:")
                questions = generate_questions(extracted_text)
                for i, q in enumerate(questions, 1):
                    st.write(f"**Q{i}.** {q}")

def extract_text_from_image(image_file):
    api_key = "K87423003988957"
    url = "https://api.ocr.space/parse/image"

    image_bytes = image_file.read()
    result = requests.post(
        url,
        files={"filename": image_bytes},
        data={
            "apikey": api_key,
            "language": "eng",
            "isOverlayRequired": False
        }
    )

    try:
        result_json = result.json()
        parsed_text = result_json["ParsedResults"][0]["ParsedText"]
        return parsed_text.strip()
    except Exception as e:
        return f"❌ Could not extract text. Error: {str(e)}"

def generate_questions(text):
    sentences = text.split('.')
    questions = []
    for s in sentences:
        s = s.strip()
        if len(s.split()) > 4:
            questions.append(f"What is meant by: '{s[:40]}...'?")
        if len(questions) >= 5:
            break
    if not questions:
        questions.append("Could not generate questions — please upload clearer notes.")
    return questions

if __name__ == "__main__":
    scan_notes_ui()
