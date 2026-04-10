import streamlit as st
from streamlit_mic_recorder import speech_to_text
import base64
import io
import random
from datetime import datetime

# استيراد آمن لنظام النطق (سنغيره للإنجليزية)
try:
    from gtts import gTTS
except ImportError:
    import os
    os.system('pip install gTTS')
    from gtts import gTTS

# --- Page Configuration ---
st.set_page_config(page_title="My FlashDeal Star - EN", page_icon="🌟")

# --- English Text-to-Speech System ---
def speak_en(text):
    """Voice output from the smart assistant in English"""
    tts = gTTS(text=text, lang='en')
    fp = io.BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)
    audio_b64 = base64.b64encode(fp.read()).decode()
    st.markdown(f'<audio autoplay="true" src="data:audio/mp3;base64,{audio_b64}">', unsafe_allow_html=True)

# --- Session State Management ---
if 'tokens' not in st.session_state:
    st.session_state.tokens = 0
if 'archive_en' not in st.session_state:
    st.session_state.archive_en = []
if 'n1' not in st.session_state:
    st.session_state.n1 = random.randint(1, 15)
    st.session_state.n2 = random.randint(1, 15)

# --- Main Interface ---
st.title("🌟 My FlashDeal Star")
st.metric(label="Token Balance", value=f"{st.session_state.tokens} ⭐")

st.divider()

# --- Interactive Challenges ---
st.subheader("📝 Quick Brain Challenge")
n1, n2 = st.session_state.n1, st.session_state.n2
st.info(f"What is: {n1} + {n2}?")

# --- Voice Input (Still listening in Arabic!) ---
st.write("🎤 **Speak your answer (in Arabic):**")
# NOTE: We keep language='ar' so it listens to your Arabic speech
text_from_voice = speech_to_text(
    language='ar',
    start_prompt="Press to Speak 🎤",
    stop_prompt="Stop ⏹️",
    key='speech_en'
)

# Display what was heard
if text_from_voice:
    # Use Markdown to label this, even though it shows Arabic
    st.success(f"Voice Heard: {text_from_voice}")

# Text input option
user_typed_answer = st.text_input("Or type answer here:", key="manual_input_en")

# Combine inputs
final_answer = text_from_voice if text_from_voice else user_typed_answer

# --- Validation and Archiving ---
col1, col2 = st.columns(2)

with col1:
    if st.button("Verify Answer ✅"):
        if final_answer:
            try:
                if str(n1 + n2) in final_answer:
                    st.session_state.tokens += 25
                    now = datetime.now().strftime("%H:%M:%S")
                    # Archive entry
                    st.session_state.archive_en.append(f"✔️ {n1} + {n2} = {n1+n2} | 🕒 {now}")
                    st.balloons()
                    # Smart assistant speaks in English!
                    speak_en(f"Excellent! The answer is correct. You earned 25 tokens.")
                    st.success("Correct Answer!")
                else:
                    speak_en("Try again, you can do it!")
                    st.error("Incorrect, try again.")
            except:
                st.warning("Please say the number clearly.")

with col2:
    if st.button("New Challenge ➡️"):
        st.session_state.n1 = random.randint(1, 20)
        st.session_state.n2 = random.randint(1, 20)
        st.rerun()

# --- Archive Section ---
st.divider()
with st.expander("📦 Challenge Archive", expanded=True):
    if st.session_state.archive_en:
        for entry in reversed(st.session_state.archive_en):
            st.write(entry)
    else:
        st.write("Archive is empty. Start solving!")

st.caption("Talk. Pay. Done. | English Interface Secured.")

