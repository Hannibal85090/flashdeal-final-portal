# تم التأكد من جودة الإملاء وقفل الجمل البرمجية
import streamlit as st
import speech_recognition as sr
from gtts import gTTS
import base64
import io

def generate_audio_html(text):
    tts = gTTS(text=text, lang='ar')
    fp = io.BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)
    audio_b64 = base64.b64encode(fp.read()).decode()
    return f'<audio autoplay="true" src="data:audio/mp3;base64,{audio_b64}">'

if 'tokens' not in st.session_state:
    st.session_state.tokens = 0

st.title("My FlashDeal Star 🌟")
st.write(f"رصيد التوكن: **{st.session_state.tokens}**")

if st.button("🎤 ابدأ التفاعل"):
    # منطق الاستماع ومعالجة الجودة
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("استعد... تحدث الآن")
        audio = r.listen(source)
        try:
            phrase = r.recognize_google(audio, language='ar-SA')
            st.info(f"المدخل الصوتي: {phrase}")
            
            # احتفالية النجاح وقفل العملية
            st.session_state.tokens += 10
            st.balloons()
            html_audio = generate_audio_html("عمل متقن! تم إضافة المكافأة إلى حسابك")
            st.markdown(html_audio, unsafe_allow_html=True)
            
        except sr.UnknownValueError:
            st.error("عذراً، لم أستطع تمييز الصوت بوضوح.")
