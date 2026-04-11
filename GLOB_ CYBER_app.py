import streamlit as st
import time
from datetime import datetime

# 1. الإعدادات الأساسية وتنسيق واجهة Cyber-Tech
st.set_page_config(page_title="My FlashDeal Star", page_icon="🌟", layout="wide")

# 2. إدارة الحالة (الرصيد، الأرشيف، النجوم)
if 'balance' not in st.session_state:
    st.session_state.balance = 1500.75
if 'history' not in st.session_state:
    st.session_state.history = []
if 'stars' not in st.session_state:
    st.session_state.stars = 5

def add_to_memory(action, category="General"):
    timestamp = datetime.now().strftime("%H:%M:%S")
    st.session_state.history.append({"time": timestamp, "action": action, "cat": category})

# 3. القاموس اللغوي (تم إصلاح كافة المفاتيح لتجنب KeyError)
LANG_DICT = {
    'English': {
        'motto': 'Talk. Pay. Done.', 
        'saden': 'Saden Security: Mutual Token', 
        'sync': 'Sync Token 🛡️', 
        'buy': 'Global Deal Execution 🚀', 
        'success': 'Process Completed Successfully!', 
        'car': 'Start Car 🔑', 
        'home': 'Manage Home 🏠', 
        'mem': '📜 Unified Memory Log',
        'sos': 'Activate SOS Mode 🔔'
    },
    'Arabic': {
        'motto': 'تحدث. ادفع. تم.', 
        'saden': 'أمان سادن: التوكن المتبادل', 
        'sync': 'مزامنة التوكن 🛡️', 
        'buy': 'إبرام الصفقة العالمية 🚀', 
        'success': 'تمت العملية بنجاح! ✅', 
        'car': 'تشغيل السيارة 🔑', 
        'home': 'إدارة المنزل 🏠', 
        'mem': '📜 سجل الذاكرة الموحد',
        'sos': 'تفعيل وضع الطوارئ 🔔'
    }
}

# 4. التنسيق البصري الاحترافي
st.markdown("""
<style>
    body { background-color: #00050a; color: white; }
    .main-header { font-size: 3rem; color: #FFD700; text-align: center; text-shadow: 0 0 15px #FFD700; }
    .balance-card { 
        background: rgba(0, 255, 204, 0.1); padding: 15px; border-radius: 15px; 
        border: 2px solid #00ffcc; text-align: center; margin-bottom: 20px;
    }
    .balance-val { font-size: 2.2rem; color: #00ffcc; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# 5. القائمة الجانبية (اللغات، SOS، السجل)
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/000000/star--v1.png", width=60)
    selected_lang = st.selectbox("🌐 Global Language", list(LANG_DICT.keys()))
    t = LANG_DICT[selected_lang]
    
    if st.button(t['sos'], type="secondary"):
        st.error(f"🚨 {t['sos']} Triggered!")
        add_to_memory("SOS Activated", "Security")
    
    st.divider()
    acc_level = st.radio("Access Level", ["Standard", "Master Alpha 🔐"])
    
    st.divider()
    with st.expander(t['mem'], expanded=True):
        if not st.session_state.history:
            st.write("No active logs.")
        else:
            for item in reversed(st.session_state.history):
                st.markdown(f"**[{item['time']}]** - {item['action']}")

# 6. الواجهة المركزية (الرصيد والبيومتري)
st.markdown(f"<h1 class='main-header'>🌟 My FlashDeal Star 🌟</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align:center;'>🕒 Current Time: {datetime.now().strftime('%d/%m/%Y - %H:%M:%S')}</p>", unsafe_allow_html=True)

# عرض الرصيد المتاح (الذي طلبته)
st.markdown(f"""
<div class='balance-card'>
    <p style='margin:0;'>💰 Available Balance / الرصيد المتاح</p>
    <p class='balance-val'>${st.session_state.balance:,.2f} USD</p>
</div>
""", unsafe_allow_html=True)

# صف الأزرار البيومترية
cols = st.columns(4)
with cols[0]:
    if st.button("👆 Fingerprint"):
        st.success("Fingerprint Matched!")
        add_to_memory("Fingerprint Verified", "Security")
with cols[1]:
    if st.button("🎭 Face ID"):
        add_to_memory("Face Scan Initiated", "Security")
with cols[2]:
    if st.button("🎙️ Voice Cmd"):
        st.info("Mic Active...")
        add_to_memory("Voice Session Active", "Programming")
with cols[3]:
    if st.button("🔑 Key Sync"):
        st.success("Access Granted!")
        add_to_memory("Key Synchronized", "Practical Steps")

# 7. أمان سادن والتوكن (تم إصلاح خطأ KeyError هنا)
st.markdown(f"### 🛡️ {t['saden']}")
c_tok1, c_tok2 = st.columns([4, 1])
with c_tok1:
    token_input = st.text_input("Enter Mutual Token...", type="password", label_visibility="collapsed")
with c_tok2:
    if st.button(t['sync']): # تم التأكد من وجود مفتاح 'sync' في القاموس
        st.success("Linked! ✅")
        add_to_memory("Token Synced", "Security")

# 8. التحكم الذكي والصفقة العالمية
st.markdown(f"### ⚡ Smart Control 🏠🏎️")
ca, cb = st.columns(2)
with ca:
    if st.button(t['car']):
        with st.status("Linking..."):
            time.sleep(1)
            st.success("Engine On! 🏎️")
            add_to_memory("Car Started", "Practical Steps")
with cb:
    if st.button(t['home']):
        st.toast("Welcome Home!")
        add_to_memory("Home Managed", "Future Vision")

# زر الصفقة الكبرى مع الاحتفالية وخصم الرصيد
if st.button(t['buy'], type="primary", use_container_width=True):
    st.session_state.balance -= 99.99
    st.progress(100)
    st.balloons()
    st.snow()
    st.success(t['success'])
    add_to_memory("Global Deal Concluded", "Marketing")
    time.sleep(1)
    st.rerun()

# 9. التفاعل الصوتي (المنطوق)
voice_val = st.chat_input(f"({t['motto']}) ...تحدث الآن")
if voice_val:
    st.write(f"🎤 **Captured:** {voice_val}")
    add_to_memory(f"Voice Capture: {voice_val}", "Programming")

# 10. تذييل الصفحة وتوثيق الكود
st.divider()
st.markdown(f"<p style='text-align:center; opacity:0.5;'>Certificate Code: STAR-UNIV-2026-FINAL | Status: Validated ✅</p>", unsafe_allow_html=True)
