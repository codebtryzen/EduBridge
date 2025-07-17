# scan2quiz.py

import streamlit as st
from PIL import Image
import pytesseract
from transformers import pipeline

pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
qa_generator = pipeline("text2text-generation", model="valhalla/t5-base-qg-hl")

def scan_and_generate_quiz():
    st.title("📷 Scan-2-Quiz: AI from Image to MCQs")
    uploaded_file = st.file_uploader("Upload textbook image or handwritten note", type=["jpg", "png", "jpeg"])

    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        if st.button("Generate Quiz"):
            extracted_text = pytesseract.image_to_string(image)
            st.subheader("📄 Extracted Text:")
            st.text_area("Text", extracted_text, height=200)

            if len(extracted_text.strip()) < 30:
                st.warning("Not enough text to summarize.")
                return

            summary = summarizer(extracted_text, max_length=80, min_length=30, do_sample=False)[0]['summary_text']
            st.subheader("📝 Summary:")
            st.write(summary)

            questions = qa_generator("generate questions: " + summary, max_length=128, do_sample=True, top_k=50)
            st.subheader("🧠 Generated Quiz Questions:")
            for i, q in enumerate(questions):
                st.markdown(f"**Q{i+1}:** {q['generated_text']}")
