import streamlit as st
from streamlit_mic_recorder import speech_to_text
import base64
import io
import random

# استيراد آمن لنظام النطق
try:
    from gtts import gTTS
except ImportError:
    import os
    os.system('pip install gTTS')
    from gtts import gTTS

# --- إعدادات الواجهة والجودة ---
st.set_page_config(page_title="My FlashDeal Star", page_icon="🌟")

def speak(text):
    """نظام الرد الصوتي للمساعد الذكي"""
    tts = gTTS(text=text, lang='ar')
    fp = io.BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)
    audio_b64 = base64.b64encode(fp.read()).decode()
    st.markdown(f'<audio autoplay="true" src="data:audio/mp3;base64,{audio_b64}">', unsafe_allow_html=True)

# --- إدارة حالة النظام (Session State) ---
if 'tokens' not in st.session_state:
    st.session_state.tokens = 0
if 'num1' not in st.session_state:
    st.session_state.num1 = random.randint(1, 10)
    st.session_state.num2 = random.randint(1, 10)

# --- الواجهة الرئيسية ---
st.title("🌟 My FlashDeal Star")
st.metric(label="رصيد التوكن الحالي", value=f"{st.session_state.tokens} ⭐")

st.divider()

# --- قسم التمارين التفاعلية ---
st.subheader("📝 تحدي الذكاء السريع")
n1, n2 = st.session_state.num1, st.session_state.num2
st.info(f"كم حاصل جمع: {n1} + {n2} ؟")

# --- جوهر المشروع: الإدخال الصوتي (تحويل الكلام إلى نص) ---
st.write("🎤 **تحدث الآن للإجابة بصوتك:**")
text_from_voice = speech_to_text(
    language='ar',
    start_prompt="اضغط هنا للتحدث 🎤",
    stop_prompt="جاري المعالجة... ✅",
    key='speech'
)

# عرض ما تم تسجيله صوتياً
if text_from_voice:
    st.success(f"سمعتك تقول: {text_from_voice}")

# خيار الإدخال الكتابي كبديل
user_typed_answer = st.text_input("أو اكتب إجابتك هنا:", key="manual_input")

# دمج المدخلين (الصوتي أو الكتابي)
final_answer = text_from_voice if text_from_voice else user_typed_answer

# --- منطق التحقق والنتائج ---
col1, col2 = st.columns(2)

with col1:
    if st.button("تأكيد الإجابة ⚡"):
        if final_answer:
            try:
                if int(final_answer) == (n1 + n2):
                    st.session_state.tokens += 20
                    st.balloons()
                    speak(f"أحسنت يا عبقري! الإجابة {final_answer} صحيحة، ربحت عشرين توكن")
                    st.success("إجابة صحيحة! تم تحديث الرصيد.")
                else:
                    speak("حاول مرة أخرى، أنت تقترب من الحل")
                    st.error("الإجابة غير صحيحة.")
            except ValueError:
                st.warning("الرجاء ذكر الرقم فقط.")

with col2:
    if st.button("عملية أخرى ➡️"):
        st.session_state.num1 = random.randint(1, 15)
        st.session_state.num2 = random.randint(1, 15)
        st.rerun()

st.divider()
st.caption("Talk. Pay. Done. | نظام الإدخال الصوتي المتطور مفعل الآن.")
