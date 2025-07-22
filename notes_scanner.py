import streamlit as st
from PIL import Image
import pytesseract
import random

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def scan_notes_ui():
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
                extracted_text = pytesseract.image_to_string(image)

                st.subheader("Extracted Text:")
                st.write(extracted_text)

                st.subheader("Generated Questions:")
                questions = generate_questions(extracted_text)
                for i, q in enumerate(questions, 1):
                    st.write(f"**Q{i}.** {q}")

def generate_questions(text):
    # Very simple mock logic — you can improve this with NLP
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
