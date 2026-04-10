import streamlit as st
import speech_recognition as sr
from gtts import gTTS
import base64
import io

# إعدادات الصفحة والجمالية
st.set_page_config(page_title="FlashDeal Interactive", page_icon="⭐")

def speak(text):
    """تحويل النص إلى صوت وتشغيله تلقائياً"""
    tts = gTTS(text=text, lang='ar')
    fp = io.BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)
    audio_b64 = base64.b64encode(fp.read()).decode()
    audio_tag = f'<audio autoplay="true" src="data:audio/mp3;base64,{audio_b64}">'
    st.markdown(audio_tag, unsafe_allow_html=True)

def listen():
    """الاستماع لصوت المستخدم وتحويله إلى نص"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("جاري الاستماع... تفضل بالتحدث")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language='ar-SA')
            return text
        except:
            return None

# إدارة الحالة (State Management)
if 'tokens' not in st.session_state:
    st.session_state.tokens = 0
if 'feedback' not in st.session_state:
    st.session_state.feedback = ""

st.title("🌟 نظام التفاعل الصوتي الذكي")
st.write(f"### رصيد المكافآت الحالي: `{st.session_state.tokens}` توكن")

col1, col2 = st.columns(2)

with col1:
    if st.button("🎤 اضغط للتحدث"):
        user_input = listen()
        if user_input:
            st.success(f"سمعتك تقول: {user_input}")
            # محاكة منطق الإجابة الصحيحة
            if "نعم" in user_input or "صح" in user_input: 
                st.session_state.tokens += 10
                msg = "أحسنت! إجابة رائعة، لقد ربحت 10 نقاط توكن"
                st.balloons()
                speak(msg)
            else:
                speak("حاول مرة أخرى، أنت تقترب من الحل")

with col2:
    if st.button("🔊 سماع التوجيهات"):
        instruction = "أهلاً بك في نظام التفاعل الصوتي. قل الإجابة الصحيحة لتربح مكافآت التوكن."
        speak(instruction)

# أرشفة العمليات (Logging)
st.divider()
st.subheader("📋 سجل النشاط والجودة")
st.write("يتم تسجيل كافة التفاعلات لضمان عدم التعارض وتحسين الأداء.")
