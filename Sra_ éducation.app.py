import streamlit as st
import random

# إعدادات بسيطة وسريعة
if 'tokens' not in st.session_state: st.session_state.tokens = 0
if 'ans' not in st.session_state: 
    n1, n2 = random.randint(1,10), random.randint(1,10)
    st.session_state.ans = n1 + n2
    st.session_state.prob = f"كم حاصل جمع {n1} و {n2}؟"

st.title("NAVIGAÅ: الملاح التربوي")
st.sidebar.metric("التوكنز 🪙", st.session_state.tokens)

st.write(f"### {st.session_state.prob}")
user_in = st.text_input("اكتب إجابتك هنا مؤقتاً:")

if st.button("تحقق"):
    if user_in and int(user_in) == st.session_state.ans:
        st.success("إجابة صحيحة!")
        st.session_state.tokens += 10
        # إعادة تعيين للمسألة القادمة
        n1, n2 = random.randint(1,10), random.randint(1,10)
        st.session_state.ans = n1 + n2
        st.session_state.prob = f"كم حاصل جمع {n1} و {n2}؟"
        st.rerun()
