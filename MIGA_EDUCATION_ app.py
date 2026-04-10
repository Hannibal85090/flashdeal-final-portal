import streamlit as st
from streamlit_mic_recorder import speech_to_text
import base64
import io
import random
from datetime import datetime

# استيراد آمن لنظام النطق
try:
    from gtts import gTTS
except ImportError:
    import os
    os.system('pip install gTTS')
    from gtts import gTTS

# --- Configuration with the NEW NAME ---
st.set_page_config(page_title="MIGA Education", page_icon="🌟")

def speak_en(text):
    """Smart Assistant English Voice"""
    try:
        tts = gTTS(text=text, lang='en')
        fp = io.BytesIO()
        tts.write_to_fp(fp)
        fp.seek(0)
        audio_b64 = base64.b64encode(fp.read()).decode()
        st.markdown(f'<audio autoplay="true" src="data:audio/mp3;base64,{audio_b64}">', unsafe_allow_html=True)
    except: pass

# --- State Management ---
if 'tokens' not in st.session_state: st.session_state.tokens = 0
if 'archive_en' not in st.session_state: st.session_state.archive_en = []
if 'n1' not in st.session_state:
    st.session_state.n1, st.session_state.n2 = random.randint(1, 15), random.randint(1, 15)

# --- Header & Branding ---
st.title("🌟 MIGA Education")
st.markdown("### **Talk. Pay. Done.**")
st.caption("Empowering all children through Voice, Signs, and AI 🖐️🌍")

st.metric(label="MIGA Tokens Rewards", value=f"{st.session_state.tokens} ⭐")

st.divider()

# --- Educational Challenge ---
n1, n2 = st.session_state.n1, st.session_state.n2
st.info(f"MIGA Challenge: What is {n1} + {n2}?")

# --- Inclusive Input Tabs ---
tab1, tab2 = st.tabs(["🎤 Voice & Text", "📷 Sign Language (AI)"])

with tab1:
    st.write("🎤 **Talk to MIGA (in Arabic):**")
    text_from_voice = speech_to_text(language='ar', start_prompt="Talk to MIGA 🎤", key='miga_v')
    if text_from_voice:
        st.success(f"MIGA heard: {text_from_voice}")
    
    user_typed = st.text_input("Or write the answer:", key="miga_t")
    final_answer = text_from_voice if text_from_voice else user_typed

    if st.button("Verify with MIGA ✅"):
        if final_answer and str(n1 + n2) in final_answer:
            st.session_state.tokens += 25
            now = datetime.now().strftime("%H:%M:%S")
            st.session_state.archive_en.append(f"✔️ {n1} + {n2} = {n1+n2} | 🕒 {now}")
            st.balloons()
            speak_en(f"Well done! MIGA is proud of you. 25 tokens added!")
            st.success("MIGA says: Correct!")
        elif final_answer:
            speak_en("MIGA says: Close! Try one more time.")
            st.error("Incorrect, keep trying!")

with tab2:
    st.write("📷 **MIGA Visual Recognition:**")
    st.camera_input("Show MIGA your sign 🖐️")

# --- Control ---
if st.button("Next MIGA Challenge ➡️"):
    st.session_state.n1, st.session_state.n2 = random.randint(1, 20), random.randint(1, 20)
    st.rerun()

# --- Success Archive ---
st.divider()
with st.expander("📦 MIGA Success Archive", expanded=True):
    if st.session_state.archive_en:
        for entry in reversed(st.session_state.archive_en):
            st.write(entry)

st.caption("MIGA Education | Talk. Pay. Done. | Dedicated to Universal Learning")
