# ================================================================
# CodeAlpha Internship - Task 1: Language Translation Tool
# Name: Obosoeye Anthony Peters
# ================================================================

import streamlit as st
from deep_translator import GoogleTranslator

# --- Page Setup ---
st.set_page_config(
    page_title="Language Translator",
    page_icon="🌐",
    layout="centered"
)

# --- Language List ---
LANGUAGES = {
    "Auto Detect": "auto",
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Arabic": "ar",
    "Chinese (Simplified)": "zh-CN",
    "Portuguese": "pt",
    "Russian": "ru",
    "Japanese": "ja",
    "Korean": "ko",
    "Italian": "it",
    "Dutch": "nl",
    "Hindi": "hi",
    "Turkish": "tr",
    "Yoruba": "yo",
    "Hausa": "ha",
    "Igbo": "ig",
    "Swahili": "sw",
}

# --- App Title ---
st.title("🌐 Language Translation Tool")
st.markdown("### Translate text between languages instantly")
st.markdown("---")

# --- Input Section ---
col1, col2 = st.columns(2)

with col1:
    source_lang = st.selectbox(
        "Source Language",
        list(LANGUAGES.keys()),
        index=0
    )

with col2:
    target_options = [l for l in LANGUAGES.keys() if l != "Auto Detect"]
    target_lang = st.selectbox(
        "Target Language",
        target_options,
        index=1
    )

# --- Text Input ---
input_text = st.text_area(
    "Enter text to translate:",
    height=150,
    placeholder="Type or paste your text here..."
)

# --- Translate Button ---
if st.button("🔄 Translate", type="primary"):
    if not input_text.strip():
        st.warning("⚠️ Please enter some text first.")
    else:
        try:
            src_code = LANGUAGES[source_lang]
            tgt_code = LANGUAGES[target_lang]

            translated = GoogleTranslator(
                source=src_code,
                target=tgt_code
            ).translate(input_text)

            st.markdown("### ✅ Translation:")
            st.success(translated)

            st.markdown("**📋 Copy the translation:**")
            st.code(translated, language=None)

        except Exception as e:
            st.error(f"❌ Translation failed: {e}")
            st.info("Please check your internet connection and try again.")

# --- Footer ---
st.markdown("---")
st.caption("Built with Python & Streamlit | CodeAlpha AI Internship | Obosoeye Anthony Peters")