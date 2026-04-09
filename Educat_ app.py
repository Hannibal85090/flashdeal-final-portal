import streamlit as st
import random
from streamlit_mic_recorder import mic_recorder

# --- 1. الإعدادات الاحترافية وهيكلة الصفحة ---
st.set_page_config(page_title="NAVIGAÅ - FlashDeal Star", page_icon="⭐", layout="centered")

# --- 2. إدارة الذاكرة (Session State) لضمان الاستقرار ---
if 'tokens' not in st.session_state:
    st.session_state.tokens = 0
if 'current_ans' not in st.session_state:
    n1, n2 = random.randint(1, 10), random.randint(1, 10)
    st.session_state.current_ans = n1 + n2
    st.session_state.current_prob = f"كم حاصل جمع {n1} و {n2}؟"

def refresh_question():
    n1, n2 = random.randint(1, 10), random.randint(1, 10)
    st.session_state.current_ans = n1 + n2
    st.session_state.current_prob = f"كم حاصل جمع {n1} و {n2}؟"

# --- 3. تصميم الواجهة (UI/UX) بنظام التبويبات الهجين ---
st.title("NAVIGAÅ: الملاح التربوي الذكي 🎙️")
st.sidebar.markdown(f"### رصيد التوكنز: `{st.session_state.tokens}` 🪙")
st.sidebar.divider()
st.sidebar.caption("FlashDeal Star: Talk. Learn. Done.")

# عرض التحدي الحالي بشكل بارز
st.info(f"🚀 **التحدي الحالي:** {st.session_state.current_prob}")
st.divider()

# إنشاء تبويبات لضمان عدم التعارض بين الميكروفون ولوحة المفاتيح
tab1, tab2 = st.tabs(["🎤 الإجابة بالصوت", "⌨️ الإجابة بالكتابة"])

user_input = None

with tab1:
    st.write("اضغط وابدأ التحدث بوضوح:")
    # تم تطهير الفواصل تماماً لضمان عدم حدوث SyntaxError
    audio_data = mic_recorder(
        start_prompt="بدء التسجيل",
        stop_prompt="توقف",
        key='naviga_voice_pro'
    )
    if audio_data and audio_data.get('text'):
        user_input = audio_data['text']
        st.success(f"تم سماعك: {user_input}")

with tab2:
    text_answer = st.text_input("أدخل رقم الإجابة هنا:", key="nav_text_pro")
    if text_answer:
        user_input = text_answer

# --- 4. محرك التحقق والسداد المنطقي ---
st.write("") # مساحة جمالية
if st.button("تأكيد الإجابة النهائية 🏁", use_container_width=True, type="primary"):
    if user_input:
        # استخراج الأرقام فقط وتجاوز أي حروف زائدة (دعم كامل للعربية والإنجليزية)
        clean_ans = "".join(filter(str.isdigit, str(user_input)))
        
        if clean_ans:
            final_val = int(clean_ans)
            if final_val == st.session_state.current_ans:
                st.balloons()
                st.success(f"✅ أحسنت يا بطل! الإجابة {final_val} صحيحة.")
                st.session_state.tokens += 10
                # التحضير للسؤال التالي
                refresh_question()
                st.button("انتقل للمسألة التالية ➡️", on_click=st.rerun)
            else:
                st.error(f"❌ الإجابة {final_val} غير صحيحة. حاول مجدداً!")
        else:
            st.warning("⚠️ لم أتمكن من تمييز رقم في إجابتك. حاول قول الرقم فقط.")
    else:
        st.info("💡 بانتظار إجابتك الصوية أو النصية للتحقق.")

# --- 5. التذييل ---
st.divider()
st.caption("نظام NAVIGAÅ التفاعلي - أحد حلول FlashDeal الذكية")
