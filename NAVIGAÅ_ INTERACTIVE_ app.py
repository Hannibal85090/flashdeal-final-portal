import streamlit as st
from streamlit_mic_recorder import mic_recorder
import speech_recognition as sr
from gtts import gTTS
import base64
import io
import random

# --- نظام النطق (Text-to-Speech) ---
def speak(text):
    tts = gTTS(text=text, lang='ar')
    fp = io.BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)
    audio_b64 = base64.b64encode(fp.read()).decode()
    st.markdown(f'<audio autoplay="true" src="data:audio/mp3;base64,{audio_b64}">', unsafe_allow_html=True)

# --- إدارة حالة النظام والتوكن ---
if 'tokens' not in st.session_state:
    st.session_state.tokens = 0
if 'num1' not in st.session_state:
    st.session_state.num1 = random.randint(1, 10)
    st.session_state.num2 = random.randint(1, 10)

st.title("🌟 My FlashDeal Star: النسخة المتكاملة")
st.metric("رصيد التوكن ⭐", st.session_state.tokens)

st.divider()

# --- قسم التمرين التفاعلي ---
n1, n2 = st.session_state.num1, st.session_state.num2
st.info(f"تحدي اليوم: كم حاصل {n1} + {n2} ؟")

# --- دمج التقنيات: تسجيل الصوت ومعالجته بـ SpeechRecognition ---
st.write("🎤 **اضغط وسجل إجابتك بصوتك:**")
audio_data = mic_recorder(start_prompt="بدء التسجيل 🎤", stop_prompt="إيقاف ⏹️", key='recorder')

final_text_answer = ""

if audio_data:
    # هنا يحدث السحر: تحويل البيانات من المسجل إلى SpeechRecognition
    r = sr.Recognizer()
    audio_file = io.BytesIO(audio_data['bytes'])
    with sr.AudioFile(audio_file) as source:
        audio = r.record(source)
    try:
        # استخدام SpeechRecognition لتحويل الصوت لنص
        final_text_answer = r.recognize_google(audio, language='ar-SA')
        st.success(f"التحليل الذكي للصوت: {final_text_answer}")
    except:
        st.error("عذراً، لم أستطع تحليل الصوت بدقة، حاول مرة أخرى.")

# إدخال كتابي احتياطي لضمان "فراق الصعوبات"
typed_answer = st.text_input("أو اكتب هنا:", key="manual")
final_input = final_text_answer if final_text_answer else typed_answer

# --- منطق التحقق والأرشفة ---
col1, col2 = st.columns(2)

with col1:
    if st.button("تحقق من الإجابة ✅"):
        if final_input:
            if str(n1 + n2) in final_input: # التحقق من وجود الرقم داخل النص
                st.session_state.tokens += 25
                st.balloons()
                speak(f"إجابة عبقرية! لقد حصلت على 25 توكن")
                st.success("إجابة صحيحة!")
            else:
                speak("الإجابة غير دقيقة، حاول مجدداً")
                st.error("خطأ، حاول مرة أخرى.")

with col2:
    if st.button("تمرين جديد ➡️"):
        st.session_state.num1 = random.randint(1, 20)
        st.session_state.num2 = random.randint(1, 20)
        st.rerun()

st.divider()
st.caption("تم الدمج بين جودة التسجيل وقوة التحليل الصوتي بنجاح.")
