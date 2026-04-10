import streamlit as st
import base64
import io
import random

# استيراد آمن للمكتبات
try:
    from gtts import gTTS
except ImportError:
    import os
    os.system('pip install gTTS')
    from gtts import gTTS

# --- إعدادات الصفحة ---
st.set_page_config(page_title="FlashDeal Star - التمارين الذكية", page_icon="🌟")

def speak(text):
    tts = gTTS(text=text, lang='ar')
    fp = io.BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)
    audio_b64 = base64.b64encode(fp.read()).decode()
    st.markdown(f'<audio autoplay="true" src="data:audio/mp3;base64,{audio_b64}">', unsafe_allow_html=True)

# --- إدارة حالة النظام ---
if 'tokens' not in st.session_state:
    st.session_state.tokens = 0
if 'num1' not in st.session_state:
    st.session_state.num1 = random.randint(1, 10)
    st.session_state.num2 = random.randint(1, 10)

# --- الواجهة الرئيسية ---
st.title("🌟 My FlashDeal Star")
st.write(f"رصيد التوكن الحالي: **{st.session_state.tokens}** ⭐")

st.divider()

# --- قسم التمارين (الرياضيات الذهنية كمثال) ---
st.subheader("📝 تحدي الذكاء السريع")
n1, n2 = st.session_state.num1, st.session_state.num2
st.info(f"كم حاصل جمع: {n1} + {n2} ؟")

user_answer = st.text_input("قل إجابتك هنا (أو اكتبها):", key="answer_input")

if st.button("تأكيد الإجابة 🎤"):
    try:
        if int(user_answer) == (n1 + n2):
            # احتفالية النجاح
            st.session_state.tokens += 20
            st.balloons()
            speak(f"أحسنت يا بطل! الإجابة {user_answer} صحيحة، ربحت 20 توكن")
            st.success("إجابة صحيحة ومتقنة!")
            
            # توليد تمرين جديد
            st.session_state.num1 = random.randint(1, 15)
            st.session_state.num2 = random.randint(1, 15)
            st.button("انتقل للتمرين التالي ➡️")
        else:
            speak("حاول مرة أخرى، أنت ذكي وستعرف الحل")
            st.error("الإجابة غير صحيحة، حاول مجدداً!")
    except ValueError:
        st.warning("الرجاء إدخال رقم الإجابة")

st.divider()
st.caption("تم دمج التمارين ونظام المكافآت الصوتي بنجاح تام.")
