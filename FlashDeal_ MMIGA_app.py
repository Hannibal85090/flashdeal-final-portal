import streamlit as st
import time
from datetime import datetime

# إعدادات الصفحة الأساسية
st.set_page_config(page_title="My FlashDeal Star", page_icon="🌟", layout="wide")

# تهيئة الذاكرة الموحدة (Unified Memory Log) والرصيد
if 'history' not in st.session_state:
    st.session_state.history = []
if 'balance' not in st.session_state:
    st.session_state.balance = 1500.75  # رصيد افتراضي للبداية

def add_to_memory(action):
    timestamp = datetime.now().strftime("%H:%M:%S")
    st.session_state.history.append(f"[{timestamp}] - {action}")

# بروتوكولات الأمان والطوارئ
def trigger_emergency_protocol():
    st.error("🚨 SOS: Emergency Protocol Activated!")
    add_to_memory("SOS Triggered - Alerts sent to Master Alpha Hub")
    with st.status("Verifying Security Links..."):
        time.sleep(1)
        st.warning("All Smart Links: IMMOBILIZED 🔒")

# وظائف التعرف والتحكم
def handle_fingerprint():
    with st.spinner("Scanning Fingerprint..."):
        time.sleep(1.5)
        st.success("Fingerprint Matched: Identity Verified! 🛡️")
        add_to_memory("Biometric Fingerprint Access Granted")

def handle_voice_interaction():
    st.info("🎙️ Listening for Voice Command...")
    # محاكاة التفاعل الصوتي الاحترافي
    time.sleep(1)
    st.write("✨ Processing Voice Nuances...")
    add_to_memory("Voice Command Captured Successfully")

# التصميم البصري (CSS) - Cyber-Tech Style
st.markdown("""
<style>
    body { background: linear-gradient(135deg, #00050a 0%, #011627 100%); color: #ffffff; }
    .star-font { size: 120px; color: gold; text-shadow: 0 0 20px #ffd700; text-align: center; margin: 40px 0; }
    .glass-card { 
        padding: 25px; border-radius: 20px; background: rgba(255, 255, 255, 0.05); 
        border: 1px solid rgba(255, 255, 255, 0.1); backdrop-filter: blur(15px); margin-bottom: 20px; 
    }
    .log-text { font-size: 0.85rem; color: #4facfe; font-family: 'Courier New', monospace; }
    .balance-text { font-size: 1.5rem; color: #00ffcc; font-weight: bold; text-align: center; }
</style>
""", unsafe_allow_html=True)

# القاموس اللغوي (LANG_DICT) كما في الصور
LANG_DICT = {
    'English': {'motto': 'Talk. Pay. Done.', 'saden': 'Saden Security: Mutual Token', 'home_car': 'Smart Control 🏠🚗', 'buy': 'Global Deal', 'success': 'Process Completed!'},
    'Arabic': {'motto': 'تحدث. ادفع. تم.', 'saden': 'أمان سادن: التوكن المتبادل', 'home_car': 'التحكم الذكي 🏠🚗', 'buy': 'إبرام الصفقة العالمية', 'success': 'تمت العملية بنجاح!'}
}

# الشريط الجانبي (Sidebar)
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/000000/star--v1.png", width=60)
    selected_lang = st.selectbox("🌐 Global Language", list(LANG_DICT.keys()))
    t = LANG_DICT[selected_lang]
    st.divider()
    if st.button(f"🚨 SOS", type="secondary"):
        trigger_emergency_protocol()
    st.divider()
    with st.expander("📜 Unified Memory Log", expanded=True):
        if not st.session_state.history:
            st.write("No active logs.")
        else:
            for item in reversed(st.session_state.history):
                st.markdown(f"<p class='log-text'>{item}</p>", unsafe_allow_html=True)

# الواجهة الرئيسية
current_time = datetime.now().strftime("%d/%m/%Y - %H:%M:%S")
st.markdown(f"<h1 style='text-align:center;'>🌟 My FlashDeal Star 🌟</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align:center; color:#4facfe;'>🕒 Current Time: {current_time}</p>", unsafe_allow_html=True)

# الرصيد والمحفظة (إضافة جديدة)
st.markdown(f"""
<div class='glass-card'>
    <p style='text-align:center; margin:0;'>💰 Available Balance / الرصيد المتاح</p>
    <p class='balance-text'>${st.session_state.balance:,.2f}</p>
</div>
""", unsafe_allow_html=True)

# صف الأزرار التفاعلية (البصمة، الوجه، الصوت، المفتاح)
cols = st.columns(4)
with cols[0]:
    if st.button("👆 Fingerprint"): handle_fingerprint()
with cols[1]:
    if st.button("🎭 Face ID"): add_to_memory("Face ID Triggered")
with cols[2]:
    if st.button("🎙️ Voice Cmd"): handle_voice_interaction()
with cols[3]:
    if st.button("🔑 Key Sync"): add_to_memory("Key Access Granted")

# منطقة العمليات (Saden Security)
st.markdown(f"<div class='glass-card'><h3>🛡️ {t['saden']}</h3>", unsafe_allow_html=True)
c1, c2 = st.columns([3, 1])
with c1:
    token_input = st.text_input("Token ID", type="password", label_visibility="collapsed", placeholder="Enter Mutual Token...")
with c2:
    if st.button("🔗 Sync"):
        st.success("Linked! ✅")
        add_to_memory(f"Token Synced: {selected_lang}")
st.markdown("</div>", unsafe_allow_html=True)

# التحكم في المنزل والسيارة
st.markdown(f"### ⚡ {t['home_car']}")
ca, cb = st.columns(2)
with ca:
    if st.button("🚗 Start Car"):
        with st.status("Linking..."):
            time.sleep(1)
            st.success("🏎️ Engine On!")
            add_to_memory("Car Started")
with cb:
    if st.button("🏠 Manage Home"):
        st.toast("🏠 Welcome Home Mode Active!")
        add_to_memory("Home Managed")

# زر إتمام الصفقة (Global Deal)
if st.button(t['buy'], type="primary", use_container_width=True):
    st.balloons()
    st.snow()
    st.success(f"🎊 {t['success']}")
    add_to_memory("Global Deal Concluded Successfully")
    # محاكاة خصم بسيط من الرصيد عند إتمام صفقة
    st.session_state.balance -= 50.0 
    st.rerun()

