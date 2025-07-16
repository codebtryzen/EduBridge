import streamlit as st
from googletrans import Translator
from gtts import gTTS
import io, textwrap

def translate_ui():
    # ---------- 🎨 Scoped CSS ----------
    st.markdown(
        textwrap.dedent(
            """
            <style>
            @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');

            .translate-stack{
                font-family:'Poppins',sans-serif;
                max-width:760px;
                margin:4rem auto;
                padding:0 1rem;
            }
            .translate-title{
                font-size:2.6rem;font-weight:700;text-align:center;margin:0 0 .4em;
                background:linear-gradient(270deg,#00c6ff,#0072ff,#8e2de2,#4a00e0,#00c6ff);
                background-size:400% 400%;
                -webkit-background-clip:text;-webkit-text-fill-color:transparent;
                animation:gradientShift 9s ease infinite;
            }
            @keyframes gradientShift{0%{background-position:0% 50%}50%{background-position:100% 50%}100%{background-position:0% 50%}}

            .translate-sub{text-align:center;font-size:1.05rem;color:#444;margin-bottom:2.2rem;}

            .translate-stack textarea{
                min-height:180px!important;
                font-size:1.05rem!important;
                line-height:1.55!important;
                padding:1.25rem!important;
                border-radius:18px!important;
                background:#f9fbff!important;
                border:2px solid #c7d0e0!important;
                box-shadow:none!important;
                transition:all .25s ease;
            }
            .translate-stack textarea:focus{
                border-color:#0072ff!important;
                box-shadow:0 0 0 4px rgba(0,114,255,.18)!important;
            }
            .translate-stack textarea::placeholder{
                color:#7a88a4!important;
                font-style:italic;
            }

            input, select{
                font-size:1rem!important;border-radius:14px!important;
            }

            div[data-testid="stButton"]>button{
                width:100%;padding:1.05rem 1.6rem;font-weight:600;border:none;border-radius:16px;color:#fff;
                background:linear-gradient(90deg,#0072ff 0%,#8e2de2 100%);
                transition:transform .25s,box-shadow .25s;
            }
            div[data-testid="stButton"]>button:hover{
                transform:translateY(-4px);box-shadow:0 12px 28px rgba(0,0,0,.18);
            }

            .translate-result{margin-top:1.8rem;padding:1.2rem 1.4rem;border-left:5px solid #0072ff;background:#000;
                              border-radius:14px;font-size:1.06rem;color:#fafafa;}
            .translate-info{margin-top:.6rem;font-size:.9rem;color:#888;text-align:right;}
            </style>
            """
        ),
        unsafe_allow_html=True,
    )

    # ---------- 🖥 UI ----------
    st.markdown('<div class="translate-stack">', unsafe_allow_html=True)
    st.markdown('<h2 class="translate-title">Text Translator</h2>', unsafe_allow_html=True)
    st.markdown('<div class="translate-sub">Translate & listen instantly in regional or global languages</div>', unsafe_allow_html=True)

    # ✅ Updated Language Dictionary
    lang_dict = {
        "Kannada": "kn",
        "Hindi": "hi",
        "Tamil": "ta",
        "Telugu": "te",
        "Marathi": "mr",
        "Bengali": "bn",
        "Gujarati": "gu",
        "Malayalam": "ml",
        "Punjabi": "pa",
        "Urdu": "ur",
        "Assamese": "as",
        "Oriya": "or",
        "Nepali": "ne",
        "Sanskrit": "sa",
        "French": "fr",
        "Spanish": "es",
        "German": "de",
        "Italian": "it",
        "Arabic": "ar",
        "Japanese": "ja",
        "Chinese (Simplified)": "zh-cn",
        "Chinese (Traditional)": "zh-tw",
        "Russian": "ru",
        "Portuguese": "pt",
        "Dutch": "nl",
        "Korean": "ko",
        "Thai": "th",
        "Vietnamese": "vi",
        "Greek": "el",
    }

    translator = Translator()

    text = st.text_area("Enter text:", placeholder="Type or paste text here…")

    lang_name = st.selectbox("Translate to:", list(lang_dict.keys()))
    lang_code = lang_dict[lang_name]

    if st.button("🌐  Translate & Speak"):
        if not text.strip():
            st.warning("Please enter text to translate.")
        else:
            try:
                with st.spinner("Translating…"):
                    translated = translator.translate(text, dest=lang_code)

                st.markdown(f'<div class="translate-result">{translated.text}</div>', unsafe_allow_html=True)
                st.markdown(
                    f'<div class="translate-info">Detected language: <b>{translated.src.upper()}</b></div>',
                    unsafe_allow_html=True,
                )

                with st.spinner("Generating voice…"):
                    tts = gTTS(text=translated.text, lang=lang_code)
                    buf = io.BytesIO()
                    tts.write_to_fp(buf)
                    buf.seek(0)
                    audio_bytes = buf.getvalue()

                st.audio(audio_bytes, format="audio/mp3")
                st.download_button("⬇  Download MP3", audio_bytes, "translation.mp3", "audio/mp3")

            except Exception as e:
                st.error(f"Translation failed: {e}")

    st.markdown("</div>", unsafe_allow_html=True)

# Run the UI
if __name__ == "__main__":
    translate_ui()
