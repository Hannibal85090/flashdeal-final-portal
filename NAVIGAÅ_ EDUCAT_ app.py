import streamlit as st
import random
from streamlit_mic_recorder import mic_recorder
import datetime

# --- 1. الإعدادات العليا والهوية ---
st.set_page_config(page_title="NAVIGAÅ Ultimate", page_icon="⭐", layout="centered")

# --- 2. محرك الحالة (Session State) - لضمان عدم التعارض ---
if 'tokens' not in st.session_state:
    st.session_state.tokens = 0
if 'history' not in st.session_state:
    st.session_state.history = []
if 'refresh_needed' not in st.session_state:
    st.session_state.refresh_needed = True

# وظيفة توليد التحديات المتجددة
if st.session_state.refresh_needed:
    st.session_state.n1 = random.randint(1, 10)
    st.session_state.n2 = random.randint(1, 10)
    st.session_state.correct_ans = st.session_state.n1 + st.session_state.n2
    st.session_state.refresh_needed = False
    st.session_state.user_feedback = ""

# --- 3. الواجهة الرسومية الاحترافية ---
st.title("NAVIGAÅ: الملاح التربوي 🎙️")
st.sidebar.metric("رصيد التوكنز 🪙", st.session_state.tokens)
st.sidebar.divider()
st.sidebar.caption("FlashDeal Star: Talk. Learn. Done.")

# عرض السؤال الحالي بشكل بارز
st.info(f"### 💡 التحدي الذكي: كم حاصل جمع {st.session_state.n1} و {st.session_state.n2}؟")

# --- 4. محرك التفاعل الصوتي (بدون فواصل عربية قاتلة) ---
st.write("---")
st.subheader("🎤 تفاعل بصوتك الآن:")

audio_result = mic_recorder(
    start_prompt="إضغط للتحدث 🎙️",
    stop_prompt="توقف ⏹️",
    key='naviga_final_mic'
)

# --- 5. منطق المعالجة والسداد التفاعلي ---
detected_answer = None

# معالجة الصوت فورياً (التفاعلية الحية)
if audio_result and audio_result.get('text'):
    spoken_text = audio_result['text'].strip()
    st.session_state.user_feedback = f"🔍 سمعت: '{spoken_text}'"
    # استخراج الأرقام فقط
    clean_digits = "".join(filter(str.isdigit, spoken_text))
    if clean_digits:
        detected_answer = int(clean_digits)

# بديل الكتابة (لضمان عدم التوقف)
with st.expander("⌨️ أو اكتب هنا"):
    manual_in = st.text_input("أدخل الرقم:", key="manual_box")
    if manual_in and not detected_answer:
        manual_digits = "".join(filter(str.isdigit, manual_in))
        if manual_digits:
            detected_answer = int(manual_digits)

# إظهار ما سمعه النظام (لتحقيق التفاعل)
if st.session_state.user_feedback:
    st.write(st.session_state.user_feedback)

# التحقق النهائي والمكافأة
if detected_answer is not None:
    if detected_answer == st.session_state.correct_ans:
        st.balloons()
        st.success(f"✅ إجابة صحيحة! {detected_answer} تمنحك 10 توكنز.")
        
        # الأرشفة وتحديث الحالة (مرة واحدة)
        if not any(h['task'] == f"{st.session_state.n1}+{st.session_state.n2}" and h['res'] == detected_answer for h in st.session_state.history):
            st.session_state.tokens += 10
            st.session_state.history.append({
                "task": f"{st.session_state.n1} + {st.session_state.n2}",
                "res": detected_answer,
                "time": datetime.datetime.now().strftime("%H:%M:%S")
            })
        
        # زر التجديد التلقائي
        if st.button("انتقل للتمرين التالي ➡️", use_container_width=True):
            st.session_state.refresh_needed = True
            st.rerun()
    else:
        st.error(f"❌ '{detected_answer}' غير صحيحة، ركز وحاول مجدداً!")

# --- 6. الأرشفة الذكية (سجل الملاحة) ---
st.divider()
with st.expander("📝 سجل الإنجازات المتجدد"):
    if st.session_state.history:
        for entry in reversed(st.session_state.history):
            st.write(f"⭐ {entry['task']} = {entry['res']} | 🕒 {entry['time']}")
    else:
        st.caption("أرشيفك فارغ، ابدأ التحدي الآن!")

st.caption("نظام NAVIGAÅ - تطوير FlashDeal Star 2026")
