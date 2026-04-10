import streamlit as st
import base64
import io
import random

# محاولة استيراد المكتبات الأساسية
try:
    from gtts import gTTS
except ImportError:
    import os
    os.system('pip install gTTS')
    from gtts import gTTS

# --- إعدادات الصفحة والجمالية ---
st.set_page_config(page_title="FlashDeal Star - التفاعل المتكامل", page_icon="🌟")

# دالة النطق (الرد الصوتي من النظام)
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
    st.session_state.num2 = random.randint(2, 10)

# --- الواجهة الرئيسية ---
st.title("🌟 My FlashDeal Star")
st.write(f"رصيد التوكن: **{st.session_state.tokens}** ⭐")
st.divider()

# --- قسم التمرين الحالي ---
st.subheader("📝 تمرين الذكاء السريع")
n1, n2 = st.session_state.num1, st.session_state.num2
st.info(f"كم حاصل ضرب: {n1} × {n2} ؟")

# --- ميزة الإدخال المزدوج (صوت وكتابة) ---
tab1, tab2 = st.tabs(["🎤 إجابة صوتية", "⌨️ إجابة كتابية"])

with tab1:
    st.write("اضغط على زر التسجيل أدناه للإجابة بصوتك:")
    # نستخدم هنا مكون جافا سكريبت بسيط لمحاكاة تسجيل الصوت في المتصفح
    # ملاحظة: في النسخة الاحترافية يتم ربطها بـ streamlit-mic-recorder
    st.warning("تنبيه: ميزة الميكروفون تتطلب منح إذن الوصول للمتصفح.")
    voice_placeholder = st.button("🎤 ابدأ التسجيل الصوتي")
    if voice_placeholder:
        st.write("جاري معالجة الصوت... (تخيل أنني أسمعك الآن)")
        # محاكاة بسيطة للتعرف على الصوت (سيتم استبدالها بـ API الصوت الفعلي)
        st.info("تم تفعيل لاقط الصوت، قل الإجابة بوضوح.")

with tab2:
    user_answer = st.text_input("اكتب إجابتك هنا:", key="text_ans")

# زر التأكيد الموحد
if st.button("تأكيد الإجابة والتحقق ✅"):
    correct_ans = n1 * n2
    if user_answer and int(user_answer) == correct_ans:
        st.session_state.tokens += 30
        st.balloons()
        speak(f"مذهل! الإجابة {user_answer} صحيحة تماماً. لقد نلت ثلاثين توكن كجائزة على براعتك")
        st.success("إجابة عبقرية!")
        # تحديث التمرين
        st.session_state.num1 = random.randint(2, 10)
        st.session_state.num2 = random.randint(2, 10)
    else:
        speak("الإجابة تحتاج إلى مراجعة، حاول مرة أخرى يا بطل")
        st.error("حاول مجدداً، الحل قريب جداً!")

st.divider()
st.caption("Talk. Pay. Done. | نظام متكامل يجمع بين الصوت والكتابة والمكافآت.")
