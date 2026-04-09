import streamlit as st
import random
from streamlit_mic_recorder import mic_recorder
import datetime

# 1. الإعدادات الأساسية
st.set_page_config(page_title="NAVIGAÅ Pro", page_icon="⭐")

# 2. إدارة الجلسة (Session State) - ضمان استقرار التوكنز والأرشفة
if 'tokens' not in st.session_state:
    st.session_state.tokens = 0
if 'history' not in st.session_state:
    st.session_state.history = []
if 'ans' not in st.session_state:
    n1, n2 = random.randint(1, 10), random.randint(1, 10)
    st.session_state.n1 = n1
    st.session_state.n2 = n2
    st.session_state.ans = n1 + n2

def next_question():
    n1, n2 = random.randint(1, 10), random.randint(1, 10)
    st.session_state.n1 = n1
    st.session_state.n2 = n2
    st.session_state.ans = n1 + n2
    st.session_state.processed = False

# 3. الواجهة الرسومية
st.title("NAVIGAÅ: الملاح التربوي 🎙️")
st.sidebar.metric("رصيد التوكنز 🪙", st.session_state.tokens)

st.info(f"🚀 **كم حاصل جمع {st.session_state.n1} و {st.session_state.n2}؟**")

# 4. التفاعل الصوتي (تم تنظيف الكود من أي فاصلة عربية)
st.write("---")
audio_data = mic_recorder(
    start_prompt="🎤 ابدأ التحدث بالإجابة",
    stop_prompt="⏹️ توقف",
    key='naviga_mic_final'
)

# 5. التفاعل النصي (خيار إضافي لضمان التفاعلية)
text_in = st.text_input("⌨️ أو اكتب إجابتك هنا واضغط Enter:")

# 6. محرك المعالجة والاحتفالية
user_val = None

# استخلاص الرقم من الصوت
if audio_data and audio_data.get('text'):
    spoken = audio_data['text']
    digits = "".join(filter(str.isdigit, spoken))
    if digits:
        user_val = int(digits)
        st.write(f"💬 سمعتك تقول: {user_val}")

# استخلاص الرقم من الكتابة (إذا لم يوجد صوت)
if text_in and not user_val:
    digits = "".join(filter(str.isdigit, text_in))
    if digits:
        user_val = int(digits)

# التحقق النهائي والمكافأة
if user_val is not None:
    if user_val == st.session_state.ans:
        st.balloons()
        st.success(f"✅ مذهل! إجابة صحيحة. (+10 توكنز)")
        
        # الأرشفة وتحديث النقاط (مرة واحدة فقط لكل سؤال)
        if 'last_solved' not in st.session_state or st.session_state.last_solved != st.session_state.ans:
            st.session_state.tokens += 10
            st.session_state.history.append({
                "سؤال": f"{st.session_state.n1}+{st.session_state.n2}",
                "إجابة": user_val,
                "وقت": datetime.datetime.now().strftime("%H:%M:%S")
            })
            st.session_state.last_solved = st.session_state.ans
        
        if st.button("تحدٍ جديد ➡️"):
            next_question()
            st.rerun()
    else:
        st.error(f"❌ الإجابة {user_val} خاطئة. حاول مجدداً!")

# 7. سجل الأرشفة
st.divider()
with st.expander("📝 سجل الملاحة (الأرشيف)"):
    if st.session_state.history:
        for item in reversed(st.session_state.history):
            st.write(f"🔹 {item['سؤال']} = {item['إجابة']} (توقيت: {item['وقت']})")
    else:
        st.write("ابدأ الحل لبناء أرشيفك!")

st.caption("FlashDeal Star - التقنية في خدمة التربية")
