import streamlit as st
import random
from streamlit_mic_recorder import mic_recorder
import datetime

# 1. الإعدادات الأساسية والهوية البصرية
st.set_page_config(page_title="NAVIGAÅ Pro", page_icon="⭐", layout="centered")

# 2. إدارة حالة الجلسة (Session State) لضمان عدم التعارض
if 'tokens' not in st.session_state:
    st.session_state.tokens = 0
if 'history' not in st.session_state:
    st.session_state.history = []
if 'n1' not in st.session_state:
    st.session_state.n1 = random.randint(1, 10)
    st.session_state.n2 = random.randint(1, 10)
    st.session_state.ans = st.session_state.n1 + st.session_state.n2

def generate_new_task():
    st.session_state.n1 = random.randint(1, 10)
    st.session_state.n2 = random.randint(1, 10)
    st.session_state.ans = st.session_state.n1 + st.session_state.n2
    st.session_state.solved_this_turn = False

# 3. واجهة المستخدم (UI)
st.title("NAVIGAÅ: الملاح التربوي الذكي 🎙️")
st.sidebar.metric("رصيد التوكنز 🪙", st.session_state.tokens)
st.sidebar.divider()
st.sidebar.caption("FlashDeal Star: Talk. Pay. Done.")

st.info(f"### 💡 التحدي: كم حاصل جمع {st.session_state.n1} و {st.session_state.n2}؟")

# 4. التفاعل الهجين (صوت + كتابة)
tab1, tab2 = st.tabs(["🎤 الإجابة بالصوت", "⌨️ الإجابة بالكتابة"])

user_input = None

with tab1:
    st.write("اضغط وابدأ التحدث:")
    # تم تدقيق الفواصل البرمجية هنا بعناية فائقة لضمان العمل على المتصفح
    audio_data = mic_recorder(
        start_prompt="ابدأ التسجيل",
        stop_prompt="توقف",
        key='naviga_mic_pro'
    )
    if audio_data and audio_data.get('text'):
        user_input = audio_data['text']
        st.write(f"💬 سمعت: **{user_input}**")

with tab2:
    text_val = st.text_input("أدخل الرقم هنا:", key="manual_text")
    if text_val:
        user_input = text_val

# 5. محرك المعالجة، الاحتفالية، والأرشفة
if st.button("تحقق من الإجابة ✅", use_container_width=True, type="primary"):
    if user_input:
        # استخراج الأرقام فقط لضمان السداد (تجنب الحروف الزائدة)
        clean_ans = "".join(filter(str.isdigit, str(user_input)))
        
        if clean_ans and int(clean_ans) == st.session_state.ans:
            st.balloons()
            st.success(f"🎊 رائع! الإجابة {clean_ans} صحيحة.")
            
            # تحديث المكافأة والأرشفة
            st.session_state.tokens += 10
            st.session_state.history.append({
                "التمرين": f"{st.session_state.n1} + {st.session_state.n2}",
                "النتيجة": clean_ans,
                "التوقيت": datetime.datetime.now().strftime("%H:%M:%S")
            })
            
            # توليد تمرين جديد تلقائياً
            if st.button("انتقل للتمرين التالي ➡️"):
                generate_new_task()
                st.rerun()
        else:
            st.error("❌ محاولة قريبة! حاول مرة أخرى بتركيز.")
    else:
        st.warning("⚠️ يرجى تقديم إجابة أولاً.")

# 6. سجل الملاحة (الأرشيف)
st.divider()
with st.expander("📝 أرشيف التمارين المكتملة"):
    if st.session_state.history:
        for entry in reversed(st.session_state.history):
            st.write(f"✅ {entry['التمرين']} = {entry['النتيجة']} | 🕒 {entry['التوقيت']}")
    else:
        st.caption("لا توجد تمارين مؤرشفة بعد.")

st.caption("نظام NAVIGAÅ - تطوير وتصميم FlashDeal Star")
