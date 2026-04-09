import streamlit as st
import random
from streamlit_mic_recorder import mic_recorder
import datetime

# --- 1. الإعدادات والجماليات ---
st.set_page_config(page_title="NAVIGAÅ Smart", page_icon="🎙️")

# --- 2. إدارة الجلسة (الذاكرة النشطة) ---
if 'tokens' not in st.session_state:
    st.session_state.tokens = 0
if 'history' not in st.session_state:
    st.session_state.history = []
if 'need_new_task' not in st.session_state:
    st.session_state.need_new_task = True

# دالة توليد المسائل المتجددة
if st.session_state.need_new_task:
    st.session_state.n1 = random.randint(1, 10)
    st.session_state.n2 = random.randint(1, 10)
    st.session_state.ans = st.session_state.n1 + st.session_state.n2
    st.session_state.need_new_task = False

# --- 3. الواجهة الذكية ---
st.title("NAVIGAÅ: الملاح التربوي التفاعلي 🚀")
st.sidebar.metric("رصيد التوكنز 🪙", st.session_state.tokens)
st.sidebar.caption("Talk. Learn. Done.")

# عرض التحدي الحالي
st.info(f"### 💡 التحدي الجديد: كم حاصل جمع {st.session_state.n1} و {st.session_state.n2}؟")

# --- 4. محرك التفاعل الصوتي الحي ---
st.write("---")
st.subheader("🎤 أجب بصوتك:")
audio_data = mic_recorder(
    start_prompt="ابدأ التحدث (قل الرقم)",
    stop_prompt="انتهيت",
    key='naviga_active_voice'
)

# معالجة الصوت التفاعلية
user_val = None
if audio_data and audio_data.get('text'):
    spoken_text = audio_data['text']
    # إظهار النص المسموع فوراً لتحقيق التفاعلية
    st.write(f"💬 النظام سمعك تقول: **{spoken_text}**")
    
    digits = "".join(filter(str.isdigit, spoken_text))
    if digits:
        user_val = int(digits)

# خيار الكتابة كدعم إضافي
with st.expander("⌨️ أو اكتب الإجابة هنا"):
    text_in = st.text_input("أدخل الرقم:", key="manual_entry")
    if text_in and not user_val:
        user_val = int("".join(filter(str.isdigit, text_in)))

# --- 5. منطق "السداد" والاحتفالية والتجديد ---
if user_val is not None:
    if user_val == st.session_state.ans:
        st.balloons()
        st.success(f"✅ أحسنت! {user_val} إجابة صحيحة تماماً.")
        
        # إضافة المكافأة والأرشفة
        st.session_state.tokens += 10
        st.session_state.history.append({
            "task": f"{st.session_state.n1} + {st.session_state.n2}",
            "res": user_val,
            "time": datetime.datetime.now().strftime("%H:%M:%S")
        })
        
        # تفعيل التجديد الفوري للمسألة التالية
        st.session_state.need_new_task = True
        if st.button("اضغط للمسألة التالية ➡️"):
            st.rerun()
    else:
        st.error(f"❌ الإجابة {user_val} غير دقيقة، حاول مرة أخرى!")

# --- 6. الأرشفة الذكية ---
st.divider()
with st.expander("📜 أرشيف التحديات المتجددة"):
    if st.session_state.history:
        for item in reversed(st.session_state.history):
            st.write(f"✔️ {item['task']} = {item['res']} | 🕒 {item['time']}")
