import streamlit as st
import time
from datetime import datetime

# 1. إعدادات المنظومة (Cyber-Tech)
st.set_page_config(page_title="My FlashDeal Star", page_icon="🌟", layout="wide")

# 2. إدارة الحالة الحية (هنا يكمن سر بقاء الرصيد والأرشفة)
if 'balance' not in st.session_state:
    st.session_state.balance = 1500.75
if 'history' not in st.session_state:
    st.session_state.history = []
if 'voice_log' not in st.session_state:
    st.session_state.voice_log = ""

def add_to_memory(action, category="General"):
    timestamp = datetime.now().strftime("%H:%M:%S")
    st.session_state.history.append({"time": timestamp, "action": action, "cat": category})

# 3. القاموس اللغوي (اللغات الأربع)
LANG_DICT = {
    'English': {'motto': 'Talk. Pay. Done.', 'buy': 'Global Deal 🚀', 'success': 'Success!', 'car': 'Start Car 🔑', 'mem': '📜 Memory'},
    'Arabic': {'motto': 'تحدث. ادفع. تم.', 'buy': 'إبرام الصفقة العالمية 🚀', 'success': 'تمت بنجاح! ✅', 'car': 'تشغيل السيارة 🔑', 'mem': '📜 السجل'}
}

# 4. التنسيق البصري
st.markdown("""
<style>
    body { background-color: #00050a; color: white; }
    .balance-card { 
        background: rgba(0, 255, 204, 0.1); padding: 15px; border-radius: 15px; 
        border: 2px solid #00ffcc; text-align: center; margin-bottom: 20px;
    }
    .balance-val { font-size: 2.5rem; color: #00ffcc; font-weight: bold; }
    .voice-box { background: rgba(255, 255, 255, 0.05); padding: 10px; border-radius: 10px; border-left: 5px solid gold; }
</style>
""", unsafe_allow_html=True)

# 5. الشريط الجانبي (الأرشيف الحي)
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/000000/star--v1.png", width=50)
    lang = st.selectbox("Language", list(LANG_DICT.keys()))
    t = LANG_DICT[lang]
    st.divider()
    with st.expander(t['mem'], expanded=True):
        for item in reversed(st.session_state.history):
            st.markdown(f"**[{item['cat']}]** {item['time']}: {item['action']}")

# 6. الواجهة المركزية (الرصيد الحي)
st.markdown("<h1 style='text-align:center;'>🌟 My FlashDeal Star 🌟</h1>", unsafe_allow_html=True)

st.markdown(f"""
<div class='balance-card'>
    <p style='margin:0;'>💰 Available Balance / الرصيد المتاح</p>
    <p class='balance-val'>${st.session_state.balance:,.2f}</p>
</div>
""", unsafe_allow_html=True)

# 7. التفاعل الصوتي (الحل النهائي لبقاء الكتابة)
st.subheader(f"🎙️ {t['motto']}")
voice_input = st.chat_input("تحدث الآن أو اكتب أمرك هنا...")

if voice_input:
    st.session_state.voice_log = voice_input
    add_to_memory(f"المنطوق: {voice_input}", "Voice")
    # إذا تضمن الأمر كلمة "دفع" أو "pay" يخصم تلقائياً
    if any(word in voice_input.lower() for word in ["pay", "ادفع", "شراء", "buy"]):
        st.session_state.balance -= 50.0
        st.toast("تم الخصم الصوتي بنجاح! 💸")
    st.rerun()

if st.session_state.voice_log:
    st.markdown(f"<div class='voice-box'>🎤 **آخر أمر تم التقاطه:** {st.session_state.voice_log}</div>", unsafe_allow_html=True)

# 8. الكاميرا والتحقق البيومتري
st.divider()
col1, col2 = st.columns(2)
with col1:
    if st.button("🎭 Face ID Activation"):
        st.session_state.cam_on = True
    if st.session_state.get('cam_on'):
        img = st.camera_input("Biometric Scan")
        if img:
            st.success("Identity Verified! ✅")
            add_to_memory("Face ID Verified", "Security")
            st.session_state.cam_on = False # إغلاق الكاميرا بعد النجاح

with col2:
    if st.button("👆 Fingerprint Sync"):
        st.success("Fingerprint Matched! ✅")
        add_to_memory("Fingerprint Verification", "Security")

# 9. إبرام الصفقة (الخصم الحقيقي والاحتفالية)
st.divider()
if st.button(t['buy'], type="primary", use_container_width=True):
    st.session_state.balance -= 125.50  # خصم المبلغ الحقيقي
    add_to_memory(f"Deal Concluded: -125.50$", "Marketing")
    st.balloons()
    st.snow()
    st.success(t['success'])
    time.sleep(1)
    st.rerun() # تحديث الصفحة فوراً لرؤية الرصيد الجديد

# 10. التحكم في السيارة والمنزل
c_a, c_b = st.columns(2)
with c_a:
    if st.button(t['car'], use_container_width=True):
        st.success("Engine Started! 🏎️")
        add_to_memory("Vehicle Engine ON", "Practical")
with c_b:
    if st.button("🏠 Smart Home", use_container_width=True):
        st.toast("Home Online! 🏠")
        add_to_memory("Home Managed", "Future Vision")

st.markdown(f"<p style='text-align:center; opacity:0.3; margin-top:50px;'>STAR-PRO-VERIFIED-2026 ✅</p>", unsafe_allow_html=True)

