import streamlit as st
import random
from streamlit_mic_recorder import mic_recorder
import datetime

# --- 1. إعدادات الهوية والاحترافية ---
st.set_page_config(page_title="NAVIGAÅ Pro - FlashDeal", page_icon="⭐", layout="centered")

# --- 2. إدارة الجلسة المحكمة (Session State) - لضمان ثبات البيانات ---
# نظام المكافأة (التوكنز)
if 'tokens' not in st.session_state:
    st.session_state.tokens = 0
# المسألة الحالية
if 'prob_data' not in st.session_state:
    n1, n2 = random.randint(1, 10), random.randint(1, 10)
    st.session_state.prob_data = {'n1': n1, 'n2': n2, 'ans': n1 + n2, 'id': str(datetime.datetime.now())}
# الأرشفة (تسجيل المسائل)
if 'history' not in st.session_state:
    st.session_state.history = []
# تتبع حالة الرد
if 'current_response' not in st.session_state:
    st.session_state.current_response = None
if 'answered_correctly' not in st.session_state:
    st.session_state.answered_correctly = False

def get_new_challenge():
    """وظيفة عبقرية لتوليد تحدٍ جديد وإعادة تعيين الحالة"""
    n1, n2 = random.randint(1, 10), random.randint(1, 10)
    st.session_state.prob_data = {'n1': n1, 'n2': n2, 'ans': n1 + n2, 'id': str(datetime.datetime.now())}
    st.session_state.current_response = None
    st.session_state.answered_correctly = False

# --- 3. الواجهة الذكية (UI) ---
st.title("NAVIGAÅ Pro: الملاح التربوي 🎙️")
st.sidebar.metric("رصيد التوكنز 🪙", st.session_state.tokens)
st.sidebar.divider()
st.sidebar.markdown(f"**المسألة الحالية:** {st.session_state.prob_data['n1']} + {st.session_state.prob_data['n2']}")

# عرض التحدي الحالي بشكل بارز
st.write(f"### 💡 كم حاصل جمع **{st.session_state.prob_data['n1']}** و **{st.session_state.prob_data['n2']}**؟")
st.divider()

# --- 4. التفاعل الهجين (صوت + كتابة) ---
tab1, tab2 = st.tabs(["🎤 التفاعل الصوتي الفوري", "⌨️ الكتابة النصية"])

# المتغير الذي سيحمل الإجابة النهائية للمعالجة
user_input_to_check = None

with tab1:
    st.write("اضغط للتحدث بوضوح:")
    # تم تدقيق المفتاح (key) لضمان عدم التعارض عند التحديث
    audio_output = mic_recorder(
        start_prompt="🎤 ابدأ الكلام",
        stop_prompt="⏹️ توقف"، # تم تصحيح الفاصلة في الكود الأصلي
        key='naviga_mic_prod'
    )
    # المعالجة الفورية للصوت (التفاعلية)
    if audio_output and audio_output.get('text') and not st.session_state.answered_correctly:
        spoken_text = audio_output['text'].strip()
        # محاولة ذكية لاستخراج الأرقام فقط
        digits = "".join(filter(str.isdigit, spoken_text))
        if digits:
            user_input_to_check = digits
            #st.session_state.current_response = f"سمعتك تقول: {spoken_text}" # اختيارية، تم حذفها لتقليل الازدحام

with tab2:
    manual_input = st.text_input("إذا كان المكان صاخباً، اكتب إجابتك هنا:", key="nav_text_prod", placeholder="مثال: 15")
    # معالجة الكتابة الفورية
    if manual_input and not st.session_state.answered_correctly:
        manual_digits = "".join(filter(str.isdigit, manual_input))
        if manual_digits:
            user_input_to_check = manual_digits

# --- 5. محرك التحقق والاحتفالية والمكافأة (The Master Engine) ---
if user_input_to_check is not None:
    # التأكد من عدم تكرار المعالجة إذا تمت الإجابة
    if not st.session_state.answered_correctly:
        val = int(user_input_to_check)
        if val == st.session_state.prob_data['ans']:
            # 1. الاحتفالية الفورية
            st.balloons()
            # 2. المكافأة (التوكنز)
            st.session_state.tokens += 10
            # 3. التأكيد البصري
            st.success(f"✅ مذهل! إجابة صحيحة ({val}). حصلت على 10 توكنز.")
            # 4. الأرشفة
            st.session_state.history.append({
                'time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
                'problem': f"{st.session_state.prob_data['n1']}+{st.session_state.prob_data['n2']}",
                'answer': val,
                'status': 'صحيح'
            })
            st.session_state.answered_correctly = True
        else:
            st.error(f"❌ أوه! {val} غير صحيحة. حاول مرة أخرى.")

# --- 6. زر "تجديد التمرين" (الذكي) ---
# زر "تمرين آخر" هو تحسين جيد في نسختك، لكنه الآن لا يضيع المكافأة!
if st.button("تحدٍ جديد ➡️", use_container_width=True, type="primary"):
    # إذا تمت الإجابة بشكل صحيح، فالزر يقوم فقط بالانتقال للسؤال التالي
    if st.session_state.answered_correctly:
        get_new_challenge()
        st.rerun()
    # إذا لم تتم الإجابة، فالزر يعتبر كـ "تجاوز" ولا يمنح مكافأة
    else:
        st.warning("⚠️ التجاوز لا يمنح توكنز! لنأرشف هذه المسألة كـ 'تجاوز'..")
        st.session_state.history.append({
                'time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
                'problem': f"{st.session_state.prob_data['n1']}+{st.session_state.prob_data['n2']}",
                'answer': '---',
                'status': 'تجاوز'
            })
        get_new_challenge()
        st.rerun()

# --- 7. الأرشفة الذكية (سجل التفاعل) ---
st.divider()
with st.expander("📝 سجل الملاحة التربوية (الأرشيف)"):
    if st.session_state.history:
        for item in reversed(st.session_state.history):
            st.write(f"- `{item['time']}`: {item['problem']} = **{item['answer']}** [{item['status']}]")
    else:
        st.caption("يبدأ الأرشيف عند أول إجابة صحيحة.")

st.caption("NAVIGAÅ Pro يعمل بتقنية FlashDeal Star التفاعلية")
