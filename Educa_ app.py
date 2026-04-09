import streamlit as st
import random
from streamlit_mic_recorder import mic_recorder

# 1. Config
st.set_page_config(page_title="NAVIGAÅ Edu", page_icon="⭐")

# 2. Session State
if 'tokens' not in st.session_state:
    st.session_state.tokens = 0
if 'current_ans' not in st.session_state:
    n1, n2 = random.randint(1, 10), random.randint(1, 10)
    st.session_state.current_ans = n1 + n2
    st.session_state.current_prob = f"كم حاصل جمع {n1} و {n2}؟"

def reset_question():
    n1, n2 = random.randint(1, 10), random.randint(1, 10)
    st.session_state.current_ans = n1 + n2
    st.session_state.current_prob = f"كم حاصل جمع {n1} و {n2}؟"

# 3. UI
st.title("NAVIGAÅ: الملاح التربوي 🎙️")
st.sidebar.metric("رصيد التوكنز 🪙", st.session_state.tokens)

st.write(f"### {st.session_state.current_prob}")
st.divider()

# 4. Voice Input
st.write("🌟 **تحدث الآن بالإجابة:**")
audio_data = mic_recorder(
    start_prompt="🎤 ابدأ التحدث",
    stop_prompt="⏹️ توقف",
    key='naviga_mic_recorder'
)

# 5. Processing
if audio_data and audio_data.get('text'):
    spoken_text = audio_data['text'].strip()
    st.info(f"سمعتك تقول: {spoken_text}")
    
    digits = ''.join(filter(str.isdigit, spoken_text))
    
    if digits:
        user_val = int(digits)
        if user_val == st.session_state.current_ans:
            st.balloons()
            st.success("✅ إجابة صحيحة! أحسنت يا بطل.")
            st.session_state.tokens += 10
            if st.button("المسألة التالية"):
                reset_question()
                st.rerun()
        else:
            st.error(f"❌ خطأ، الإجابة ليست {user_val}. حاول مرة أخرى!")
    else:
        st.warning("⚠️ يرجى قول الرقم بوضوح.")

st.divider()
st.caption("FlashDeal Star - التقنية في خدمة التربية")

