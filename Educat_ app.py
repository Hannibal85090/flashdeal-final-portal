import streamlit as st
import random
from streamlit_mic_recorder import mic_recorder

# --- 1. إعدادات الهوية البصرية والاحترافية ---
st.set_page_config(page_title="NAVIGAÅ - FlashDeal", page_icon="🎙️", layout="centered")

# --- 2. تدقيق حالة الجلسة (Session State) لضمان عدم ضياع البيانات ---
if 'tokens' not in st.session_state:
    st.session_state.tokens = 0
if 'current_ans' not in st.session_state:
    n1, n2 = random.randint(1, 10), random.randint(1, 10)
    st.session_state.current_ans = n1 + n2
    st.session_state.current_prob = f"كم حاصل جمع {n1} و {n2}؟"

# دالة لتحديث المسألة بعد الإجابة الصحيحة
def refresh_problem():
    n1, n2 = random.randint(1, 10), random.randint(1, 10)
    st.session_state.current_ans = n1 + n2
    st.session_state.current_prob = f"كم حاصل جمع {n1} و {n2}؟"

# --- 3. واجهة المستخدم (UI) ---
st.title("NAVIGAÅ: الملاح التربوي الذكي 🚀")
st.sidebar.metric("رصيد التوكنز 🪙", st.session_state.tokens)
st.sidebar.divider()
st.sidebar.info("مشروع: FlashDeal\n\nالشعار: Talk. Pay. Done.")

st.markdown(f"### {st.session_state.current_prob}")
st.write("---")

# --- 4. التفاعل الصوتي (The Voice Engine) ---
st.write("🌟 **تفضل بالإجابة صوتياً:**")
audio_data = mic_recorder(
    start_prompt="🎤 ابدأ التحدث",
    stop_prompt="⏹️ توقف"، # تم تصحيح الفاصلة هنا برمجياً
    key='naviga_voice_recorder'
)

# --- 5. منطق المعالجة والتدقيق (The Logic) ---
if audio_data and audio_data.get('text'):
    spoken_text = audio_output = audio_data['text'].strip()
    
    # استخراج الأرقام فقط من النص المنطوق (سواء كان بالعربي أو الإنجليزي)
    # ملاحظة: بعض المحركات تحول "خمسة" إلى "5" تلقائياً
    numbers_only = ''.join(filter(str.isdigit, spoken_text))
    
    if numbers_only:
        user_val = int(numbers_only)
        st.info(f"سمعتك تقول: **{user_val}**")
        
        if user_val == st.session_state.current_ans:
            st.balloons()
            st.success("✅ رائع! إجابة صحيحة، أحسنت يا ملاح.")
            st.session_state.tokens += 10
            # تحديث المسألة وتنبيه المستخدم
            if st.button("انتقل للمسألة التالية ➡️"):
                refresh_problem()
                st.rerun()
        else:
            st.error(f"❌ الإجابة {user_val} غير دقيقة. حاول مرة أخرى!")
    else:
        st.warning("⚠️ لم أتمكن من تمييز رقم في إجابتك. حاول قول الرقم فقط بوضوح.")

# --- 6. التذييل (Footer) ---
st.divider()
st.caption("تم التطوير بواسطة ذكاء FlashDeal الاصطناعي - NAVIGAÅ")
