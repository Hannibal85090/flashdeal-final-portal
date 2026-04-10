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

# --- إعدادات الواجهة ---
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
if 'archive' not in st.session_state:
    st.session_state.archive = []
if 'num1' not in st.session_state:
    st.session_state.num1 = random.randint(1, 15)
    st.session_state.num2 = random.randint(1, 15)

# --- الواجهة الرئيسية ---
st.title("🌟 My FlashDeal Star")
st.metric(label="رصيد التوكن الحالي", value=f"{st.session_state.tokens} ⭐")

st.divider()

# --- قسم التمارين التفاعلية ---
st.subheader("📝 تحدي الذكاء السريع")
n1, n2 = st.session_state.num1, st.session_state.num2
st.info(f"كم حاصل جمع: {n1} + {n2} ؟")

# --- الإدخال الصوتي (تحويل الكلام إلى نص مباشرة) ---
st.write("🎤 **تحدث بصوتك للإجابة:**")
text_from_voice = speech_to_text(
    language='ar',
    start_prompt="اضغط للتحدث 🎤",
    stop_prompt="إيقاف ⏹️",
    key='speech'
)

# عرض العدد المنطوق فوراً كما كان في النسخة الناجحة
if text_from_voice:
    st.success(f"سمعتك تقول: {text_from_voice}")

# خيار الإدخال الكتابي
user_typed_answer = st.text_input("أو اكتب هنا:", key="manual_input")

# دمج المدخلين
final_answer = text_from_voice if text_from_voice else user_typed_answer

# --- التحقق والأرشفة ---
col1, col2 = st.columns(2)

with col1:
    if st.button("تحقق من الإجابة ✅"):
        if final_answer:
            try:
                if str(n1 + n2) in final_answer:
                    st.session_state.tokens += 25
                    now = datetime.now().strftime("%H:%M:%S")
                    # إضافة العملية للأرشيف
                    st.session_state.archive.append(f"✔️ {n1} + {n2} = {n1+n2} | 🕒 {now}")
                    st.balloons()
                    speak(f"أحسنت! الإجابة {n1 + n2} صحيحة. ربحت 25 توكن")
                    st.success("إجابة موفقة!")
                else:
                    speak("حاول مرة أخرى يا بطل")
                    st.error("الإجابة غير دقيقة.")
            except:
                st.warning("الرجاء ذكر الرقم بوضوح.")

with col2:
    if st.button("تمرين جديد ➡️"):
        st.session_state.num1 = random.randint(1, 20)
        st.session_state.num2 = random.randint(1, 20)
        st.rerun()

# --- قسم الأرشيف المضاف ---
st.divider()
with st.expander("📦 أرشيف التحديات المنجزة", expanded=True):
    if st.session_state.archive:
        for entry in reversed(st.session_state.archive):
            st.write(entry)
    else:
        st.write("الأرشيف فارغ حالياً، ابدأ الحل!")

st.caption("Talk. Pay. Done. | النسخة الأصلية مع الأرشيف.")
