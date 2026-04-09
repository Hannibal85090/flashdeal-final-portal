import streamlit as st
import random
from streamlit_mic_recorder import mic_recorder

# --- 1. إعدادات الهوية ---
st.set_page_config(page_title="NAVIGAÅ - FlashDeal Star", page_icon="⭐")

# --- 2. إدارة الجلسة (الحفاظ على الاستمرارية) ---
if 'tokens' not in st.session_state:
    st.session_state.tokens = 0
if 'ans' not in st.session_state:
    n1, n2 = random.randint(1, 10), random.randint(1, 10)
    st.session_state.ans = n1 + n2
    st.session_state.prob = f"كم حاصل جمع {n1} و {n2}؟"

def next_level():
    n1, n2 = random.randint(1, 10), random.randint(1, 10)
    st.session_state.ans = n1 + n2
    st.session_state.prob = f"كم حاصل جمع {n1} و {n2}؟"
    st.rerun()

# --- 3. الواجهة الذكية ---
st.title("NAVIGAÅ: الملاح التربوي 🎙️")
st.sidebar.metric("رصيد التوكنز 🪙", st.session_state.tokens)

# عرض السؤال بشكل جذاب
st.markdown(f"### 💡 {st.session_state.prob}")

# --- 4. التفاعل الصوتي الفوري ---
st.write("---")
st.write("🌟 **تحدث الآن بالإجابة:**")

# ملاحظة: تم ضبط المفتاح (key) ليكون فريداً لضمان التحديث التلقائي
audio_output = mic_recorder(
    start_prompt="🎤 اضغط وابدأ الكلام",
    stop_prompt="⏹️ توقف عند الانتهاء",
    key='naviga_active_mic'
)

# --- 5. المعالجة التفاعلية (بدون أزرار إضافية) ---
if audio_output and audio_output.get('text'):
    spoken_text = audio_output['text'].strip()
    st.info(f"سمعتك تقول: {spoken_text}")
    
    # استخراج الأرقام بذكاء
    digits = "".join(filter(str.isdigit, spoken_text))
    
    if digits:
        user_val = int(digits)
        if user_val == st.session_state.ans:
            st.balloons()
            st.success(f"✅ مذهل! {user_val} إجابة صحيحة.")
            st.session_state.tokens += 10
            # زر انتقال سريع للسؤال التالي لزيادة التفاعلية
            if st.button("أريد تحدياً جديداً! 🚀"):
                next_level()
        else:
            st.error(f"❌ الإجابة {user_val} ليست صحيحة، حاول قول الرقم مرة أخرى.")
    else:
        st.warning("⚠️ لم أميز رقماً في كلامك، حاول تقريب الميكروفون.")

# --- 6. بديل الكتابة (لحالات الطوارئ) ---
with st.expander("⌨️ هل تفضل الكتابة؟"):
    manual_in = st.text_input("اكتب إجابتك هنا:")
    if manual_in:
        clean_manual = "".join(filter(str.isdigit, manual_in))
        if clean_manual and int(clean_manual) == st.session_state.ans:
            st.success("✅ صحيح!")
            if st.button("سؤال جديد"): next_level()

st.divider()
st.caption("Talk. Learn. Done - FlashDeal Star")

