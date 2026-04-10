import streamlit as st
from streamlit_mic_recorder import mic_recorder
import speech_recognition as sr
from gtts import gTTS
import base64
import io
import random
from pydub import AudioSegment # لتحويل صيغة الصوت

# --- نظام النطق ---
def speak(text):
    tts = gTTS(text=text, lang='ar')
    fp = io.BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)
    audio_b64 = base64.b64encode(fp.read()).decode()
    st.markdown(f'<audio autoplay="true" src="data:audio/mp3;base64,{audio_b64}">', unsafe_allow_html=True)

# --- إدارة الحالة ---
if 'tokens' not in st.session_state:
    st.session_state.tokens = 0
if 'num1' not in st.session_state:
    st.session_state.num1 = random.randint(1, 10)
    st.session_state.num2 = random.randint(1, 10)

st.title("🌟 My FlashDeal Star: النسخة المتقنة")
st.metric("رصيد التوكن ⭐", st.session_state.tokens)

# --- التمرين ---
n1, n2 = st.session_state.num1, st.session_state.num2
st.info(f"تحدي اليوم: كم حاصل {n1} + {n2} ؟")

# --- معالجة الصوت الذكية ---
st.write("🎤 **سجل إجابتك بصوتك:**")
audio_data = mic_recorder(start_prompt="ابدأ التسجيل 🎤", stop_prompt="إيقاف ⏹️", key='recorder')

final_text_answer = ""

if audio_data:
    try:
        # تحويل بيانات الصوت من أي صيغة إلى WAV لتقبلها مكتبة SpeechRecognition
        audio_bytes = io.BytesIO(audio_data['bytes'])
        audio_segment = AudioSegment.from_file(audio_bytes)
        
        wav_io = io.BytesIO()
        audio_segment.export(wav_io, format="wav")
        wav_io.seek(0)
        
        r = sr.Recognizer()
        with sr.AudioFile(wav_io) as source:
            audio = r.record(source)
            final_text_answer = r.recognize_google(audio, language='ar-SA')
            st.success(f"سمعتك تقول: {final_text_answer}")
    except Exception as e:
        st.error(f"خطأ في معالجة الصوت: حاول التحدث بوضوح أكثر.")

# --- التحقق والنتائج ---
user_typed = st.text_input("أو اكتب هنا:", key="manual")
final_input = final_text_answer if final_text_answer else user_typed

col1, col2 = st.columns(2)

with col1:
    if st.button("تحقق من الإجابة ✅"):
        if final_input:
            if str(n1 + n2) in final_input:
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
st.caption("تم حل مشكلة صيغة الملف الصوتي لضمان استمرارية الإبداع.")

