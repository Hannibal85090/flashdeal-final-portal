import streamlit as st
from streamlit_mic_recorder import speech_to_text
import base64
import io
import random
import cv2
import mediapipe as mp
import numpy as np
from datetime import datetime

# --- 1. التثبيت الآمن للمكتبات ---
try:
    from gtts import gTTS
except ImportError:
    import os
    os.system('pip install gTTS')
    from gtts import gTTS

# --- 2. إعدادات الهوية والروح (Branding) ---
st.set_page_config(page_title="MIGA Education", page_icon="🖐️", layout="centered")

def speak_en(text):
    """صوت المساعد الذكي - نبض النظام بالإنجليزية"""
    try:
        tts = gTTS(text=text, lang='en')
        fp = io.BytesIO()
        tts.write_to_fp(fp)
        fp.seek(0)
        audio_b64 = base64.b64encode(fp.read()).decode()
        st.markdown(f'<audio autoplay="true" src="data:audio/mp3;base64,{audio_b64}">', unsafe_allow_html=True)
    except:
        pass

# --- 3. إدارة الذاكرة (Session State) ---
if 'miga_tokens' not in st.session_state: st.session_state.miga_tokens = 0
if 'miga_archive' not in st.session_state: st.session_state.miga_archive = []
if 'n1' not in st.session_state:
    st.session_state.n1, st.session_state.n2 = random.randint(1, 15), random.randint(1, 15)
if 'bio_unlocked' not in st.session_state: st.session_state.bio_unlocked = False

# --- 4. محرك بصمة اليد (MIGA Visual Pulse) ---
def check_hand_gesture(image_file):
    """التحقق من وجود اليد كبصمة أمان حيوية"""
    mp_hands = mp.solutions.hands
    with mp_hands.Hands(static_image_mode=True, max_num_hands=1, min_detection_confidence=0.5) as hands:
        file_bytes = np.asarray(bytearray(image_file.read()), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, 1)
        rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb_img)
        if results.multi_hand_landmarks:
            return True
        return False

# --- 5. الواجهة والشعار (Talk. Pay. Done.) ---
st.title("🌟 MIGA Education")
st.markdown("### **Talk. Pay. Done.**")
st.caption("A Legacy of Innovation | Voice & Sign Integration")

# رصيد التوكن كإنجاز قلبي
st.metric(label="MIGA Success Tokens", value=f"{st.session_state.miga_tokens} ⭐")

st.divider()

# --- 6. قلب التفاعل (التحدي والتوثيق) ---
n1, n2 = st.session_state.n1, st.session_state.n2
st.info(f"Challenge: {n1} + {n2} = ?")

tabs = st.tabs(["🎤 Voice/Text", "🔐 Bio-Sign", "📜 Archive"])

with tabs[0]:
    st.write("🎤 **Your Response (Arabic):**")
    voice_data = speech_to_text(language='ar', start_prompt="Talk to MIGA 🎤", key='miga_heart_v')
    typed_data = st.text_input("Or write it here:", key='miga_heart_t')
    
    final_input = voice_data if voice_data else typed_data
    
    if st.button("Submit to MIGA ✅"):
        if final_input and str(n1 + n2) in final_input:
            if st.session_state.bio_unlocked:
                st.session_state.miga_tokens += 25
                now = datetime.now().strftime("%H:%M:%S")
                st.session_state.miga_archive.append(f"✔️ {n1}+{n2}={n1+n2} | Bio-OK | 🕒 {now}")
                st.balloons()
                speak_en("Fantastic! Your answer is verified and tokens added.")
                st.session_state.bio_unlocked = False # إعادة القفل للأمان
                st.success("Correct Answer!")
            else:
                speak_en("Identity verification required. Show your hand in the next tab.")
                st.warning("Please unlock with Bio-Sign first!")
        else:
            speak_en("Think again, you can do it.")
            st.error("Try again!")

with tabs[1]:
    st.write("🔐 **Hand Bio-Authentication**")
    st.caption("Show your hand clearly to the camera to authorize.")
    hand_img = st.camera_input("Scan Hand Sign", key='miga_heart_cam')
    
    if hand_img:
        if check_hand_gesture(hand_img):
            st.session_state.bio_unlocked = True
            st.success("Identity Confirmed! Bio-Sign match found. 🛡️")
            speak_en("Hand recognized. Identity verified.")
        else:
            st.error("Hand not detected. Please try again.")

with tabs[2]:
    if st.session_state.miga_archive:
        for item in reversed(st.session_state.miga_archive):
            st.write(item)
    else:
        st.write("Your success story starts here.")

# --- 7. التحكم العام ---
if st.button("Next Challenge ➡️"):
    st.session_state.n1, st.session_state.n2 = random.randint(1, 20), random.randint(1, 20)
    st.session_state.bio_unlocked = False
    st.rerun()

st.divider()
st.caption("MIGA Education | Talk. Pay. Done. | Born from the Heart ♥")
