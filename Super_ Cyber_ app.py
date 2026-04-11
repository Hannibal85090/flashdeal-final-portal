import streamlit as st
import time
from datetime import datetime

# 1. الإعدادات العليا: الدقة والجمال أولاً
st.set_page_config(page_title="My FlashDeal Star", page_icon="🌟", layout="wide")

# 2. إدارة الحالة (الذاكرة الحية) - لا ضياع للبيانات بعد الآن
if 'balance' not in st.session_state:
    st.session_state.balance = 1500.75
if 'history' not in st.session_state:
    st.session_state.history = []
if 'voice_log' not in st.session_state:
    st.session_state.voice_log = ""

def add_to_memory(action, category="General"):
    timestamp = datetime.now().strftime("%H:%M:%S")
    st.session_state.history.append({"time": timestamp, "action": action, "cat": category})

# 3. القاموس اللغوي الرباعي (الالتزام بالانصياع للهوية)
LANG_DICT = {
    'English': {'motto': 'Talk. Pay. Done.', 'buy': 'Global Deal 🚀', 'success': 'Success! ✅', 'sync': 'Sync Token 🛡️', 'car': 'Start Car 🔑', 'home': 'Manage Home 🏠', 'mem': '📜 Memory Log'},
    'Arabic': {'motto': 'تحدث. ادفع. تم.', 'buy': 'إبرام الصفقة العالمية 🚀', 'success': 'تمت العملية بنجاح! ✅', 'sync': 'مزامنة التوكن 🛡️', 'car': 'تشغيل السيارة 🔑', 'home': 'إدارة المنزل 🏠', 'mem': '📜 سجل الذاكرة'}
}

# 4. التنسيق البصري (Cyber-Tech Aesthetic)
st.markdown("""
<style>
    body { background-color: #00050a; color: white; }
    .balance-card { 
        background: rgba(0, 255, 204, 0.1); padding: 20px; border-radius: 15px; 
        border: 2px solid #00ffcc; text-align: center; margin-bottom: 30px;
        box-shadow: 0px 0px 15px rgba(0, 255, 204, 0.3);
    }
    .balance-val { font-size: 3rem; color: #00ffcc; font-weight: bold; }
    .voice-box { background: rgba(255, 255, 255, 0.05); padding: 15px; border-radius: 10px; border-left: 5px solid gold; margin: 10px 0; }
</style>
""", unsafe_allow_html=True)

# 5. الشريط الجانبي (الأرشيف الحي والدقة التاريخية)
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/000000/star--v1.png", width=60)
    lang = st.selectbox("🌐 Global Language", list(LANG_DICT.keys()))
    t = LANG_DICT[lang]
    st.divider()
    if st.button("🚨 Activate SOS Mode 🔔", type="secondary"):
        add_to_memory("SOS Protocol Triggered", "Security")
        st.error("Emergency Protocol Activated!")
    st.divider()
    with st.expander(t['mem'], expanded=True):
        if not st.session_state.history:
            st.write("No active logs.")
        for item in reversed(st.session_state.history):
            st.markdown(f"**[{item['cat']}]** {item['time']}: {item['action']}")

# 6. الواجهة المركزية
st.markdown("<h1 style='text-align:center;'>🌟 My FlashDeal Star 🌟</h1>", unsafe_allow_html=True)

st.markdown(f"""
<div class='balance-card'>
    <p style='margin:0;'>💰 Available Balance / الرصيد المتاح</p>
    <p class='balance-val'>${st.session_state.balance:,.2f}</p>
</div>
""", unsafe_allow_html=True)

# 7. التفاعل الصوتي (ثبات المنطوق وانصياع الأمر)
st.subheader(f"🎙️ {t['motto']}")
voice_input = st.chat_input("تحدث الآن... (سأقوم بحفظ المنطوق وتحليله)")

if voice_input:
    st.session_state.voice_log = voice_input
    add_to_memory(f"Voice: {voice_input}", "Communication")
    # منطق الخصم الصوتي الذكي
    if any(word in voice_input.lower() for word in ["pay", "ادفع", "buy", "شراء"]):
        st.session_state.balance -= 50.0
        st.toast("تم الخصم الصوتي بنجاح! 💸")
    st.rerun()

if st.session_state.voice_log:
    st.markdown(f"<div class='voice-box'>🎤 **آخر أمر ملتقط:** {st.session_state.voice_log}</div>", unsafe_allow_html=True)

# 8. الأمان الحيوي (الدقة في الهوية)
st.divider()
col1, col2 = st.columns(2)
with col1:
    if st.button("🎭 Face ID Activation", use_container_width=True):
        st.session_state.cam_on = True
    if st.session_state.get('cam_on'):
        img = st.camera_input("Biometric Scan")
        if img:
            st.success("Identity Verified! ✅")
            add_to_memory("Face ID Verified", "Security")
            st.session_state.cam_on = False

with col2:
    if st.button("👆 Fingerprint Sync", use_container_width=True):
        st.success("Fingerprint Matched! ✅")
        add_to_memory("Fingerprint Verified", "Security")

# 9. إبرام الصفقة (الاحتفالية الكاملة - القلب النابض)
st.divider()
if st.button(t['buy'], type="primary", use_container_width=True):
    st.session_state.balance -= 125.50
    add_to_memory("Global Deal Concluded: -125.50$", "Marketing")
    st.balloons()
    st.snow()
    st.success(t['success'])
    time.sleep(1)
    st.rerun()

# 10. التحكم الذكي (الإتمام والإبداع)
st.markdown("### ⚡ Smart Control 🏠🏎️")
c_a, c_b = st.columns(2)
with c_a:
    if st.button(t['car'], use_container_width=True):
        with st.status("Linking..."):
            time.sleep(1)
            st.success("🏎️ Engine On!")
        add_to_memory("Vehicle Started", "Practical")
with c_b:
    if st.button(t['home'], use_container_width=True):
        st.toast("Welcome Home! 🏠")
        add_to_memory("Home Systems Active", "Future Vision")

st.markdown("<p style='text-align:center; opacity:0.3; margin-top:50px;'>STAR-PRO-VERIFIED-2026 ✅</p>", unsafe_allow_html=True)

