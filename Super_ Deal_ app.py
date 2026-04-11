import streamlit as st
import time
from datetime import datetime

# 1. التثبت والتحقق (إعدادات الروح للقلب)
st.set_page_config(page_title="My FlashDeal Star", page_icon="🌟", layout="wide")

# 2. إدارة الذاكرة الموحدة (أهمية التوكن والرصيد)
if 'balance' not in st.session_state:
    st.session_state.balance = 1500.75
if 'history' not in st.session_state:
    st.session_state.history = []
if 'voice_display' not in st.session_state:
    st.session_state.voice_display = ""
if 'token_active' not in st.session_state:
    st.session_state.token_active = False

def add_to_log(action, cat="System"):
    t = datetime.now().strftime("%H:%M:%S")
    st.session_state.history.append({"time": t, "action": action, "cat": cat})

# 3. القاموس الكامل (حل مشكلة KeyError نهائياً)
LANGS = {
    'English': {
        'motto': 'Talk. Pay. Done.', 'sync': 'Sync Token 🛡️', 'buy': 'Global Deal Execution 🚀',
        'success': 'Process Completed! ✅', 'car': 'Start Car 🔑', 'home': 'Smart Home 🏠',
        'secure': 'Saden Security: Mutual Token', 'mem': '📜 Unified Memory Log', 'status': 'System Status 📊'
    },
    'Arabic': {
        'motto': 'تحدث. ادفع. تم.', 'sync': 'مزامنة التوكن 🛡️', 'buy': 'إبرام الصفقة العالمية 🚀',
        'success': 'تمت العملية بنجاح! ✅', 'car': 'تشغيل السيارة 🔑', 'home': 'إدارة المنزل 🏠',
        'secure': 'أمان سادن: التوكن المتبادل', 'mem': '📜 سجل الذاكرة الموحد', 'status': 'حالة النظام 📊'
    }
}

# 4. التصميم البصري الاحترافي
st.markdown("""
<style>
    body { background-color: #00050a; color: white; }
    .stApp { background: #00050a; }
    .balance-card { 
        background: rgba(0, 255, 204, 0.1); padding: 15px; border-radius: 12px; 
        border: 1px solid #00ffcc; text-align: center; margin-bottom: 20px;
    }
    .balance-val { font-size: 2.5rem; color: #00ffcc; font-weight: bold; }
    .voice-msg { background: rgba(255, 255, 255, 0.05); padding: 10px; border-radius: 8px; border-left: 4px solid #FFD700; }
</style>
""", unsafe_allow_html=True)

# 5. الشريط الجانبي (الأرشيف الحي)
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/000000/star--v1.png", width=50)
    selected_lang = st.selectbox("🌐 Global Language", list(LANGS.keys()))
    t = LANGS[selected_lang]
    st.divider()
    with st.expander(t['mem'], expanded=True):
        for item in reversed(st.session_state.history):
            st.markdown(f"**[{item['cat']}]** {item['time']}: {item['action']}")

# 6. الواجهة المركزية (الرصيد الحي)
st.markdown("<h1 style='text-align:center;'>🌟 My FlashDeal Star 🌟</h1>", unsafe_allow_html=True)

st.markdown(f"""
<div class='balance-card'>
    <p style='margin:0; font-size: 0.9rem;'>💰 Available Balance / الرصيد المتاح</p>
    <p class='balance-val'>${st.session_state.balance:,.2f}</p>
</div>
""", unsafe_allow_html=True)

# 7. نظام التفاعل الصوتي (ثبات المنطوق)
st.subheader(f"🎙️ {t['motto']}")
v_input = st.chat_input("تحدث الآن... (سيتم أرشفة المنطوق فوراً)")
if v_input:
    st.session_state.voice_display = v_input
    add_to_log(f"Voice Command: {v_input}", "Programming")
    if any(w in v_input.lower() for w in ["pay", "ادفع", "buy"]):
        st.session_state.balance -= 50.0
    st.rerun()

if st.session_state.voice_display:
    st.markdown(f"<div class='voice-msg'>🎤 **Captured Voice:** {st.session_state.voice_display}</div>", unsafe_allow_html=True)

# 8. نظام المصافحة والأمان (الموازي - كما في صورتك الأخيرة)
st.divider()
st.markdown(f"### 🛡️ {t['secure']}")
col_sec1, col_sec2 = st.columns([2, 1])

with col_sec1:
    if st.button("🔴 بدء فحص الهوية والحركة", use_container_width=True):
        st.success("✅ تم التحقق من الهوية ونمط الحركة")
        st.session_state.token_active = True
        add_to_log("Identity & Motion Verified", "Security")
    
    if st.session_state.token_active:
        st.code("Token: fc67f...92ae1f...", language="text")

with col_sec2:
    # حالة النظام الموازي (JSON)
    st.json({
        "Secure_Core": "Active ✅",
        "Motion_Engine": "Ready ⚡",
        "Token_Service": "Online 🔐"
    })

# 9. الأزرار البيومترية والكاميرا
st.divider()
c_bio1, c_bio2 = st.columns(2)
with c_bio1:
    if st.button("🎭 Face ID Scan"):
        st.session_state.open_cam = True
    if st.session_state.get('open_cam'):
        img = st.camera_input("Face Scan")
        if img:
            st.success("Face Verified! ✅")
            add_to_log("Biometric Face Match", "Security")
            st.session_state.open_cam = False

with c_bio2:
    if st.button("👆 Fingerprint Sync"):
        st.success("Fingerprint Confirmed! ✅")
        add_to_log("Fingerprint Verified", "Security")

# 10. إبرام الصفقة والاحتفالية (الخصم الحقيقي)
st.divider()
if st.button(t['buy'], type="primary", use_container_width=True):
    st.session_state.balance -= 125.50
    add_to_log("Deal Concluded: -125.50$", "Marketing")
    st.balloons()
    st.snow()
    st.success(t['success'])
    time.sleep(1)
    st.rerun()

# 11. التحكم الذكي
st.markdown(f"### ⚡ Smart Control 🏎️🏠")
ca, cb = st.columns(2)
with ca:
    if st.button(t['car'], use_container_width=True):
        st.success("Engine Started! 🏎️")
        add_to_log("Car Started", "Practical")
with cb:
    if st.button(t['home'], use_container_width=True):
        st.toast("Home Systems Online! 🏠")
        add_to_log("Home Managed", "Future Vision")

st.markdown("<p style='text-align:center; opacity:0.3; margin-top:30px;'>STAR-PRO-FINAL-2026 ✅</p>", unsafe_allow_html=True)
