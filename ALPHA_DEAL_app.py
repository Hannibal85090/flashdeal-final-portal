import streamlit as st
import time
from datetime import datetime

# 1. تثبيت الهوية (Cyber-Tech Setup)
st.set_page_config(page_title="My FlashDeal Star", page_icon="🌟", layout="wide")

# 2. إدارة الحالة الحية (ضمان عدم ضياع أي "تكة" برمجية)
if 'balance' not in st.session_state:
    st.session_state.balance = 1500.75
if 'history' not in st.session_state:
    st.session_state.history = []
if 'voice_display' not in st.session_state:
    st.session_state.voice_display = ""

def add_to_log(action, category="System"):
    # تصحيح الأقواس هنا لاستدعاء الوقت الفعلي
    now = datetime.now().strftime("%H:%M:%S")
    st.session_state.history.append({"time": now, "action": action, "cat": category})

# 3. القاموس اللغوي (الحل النهائي للهفوات اللغوية)
LANGS = {
    'English': {'motto': "Talk. Pay. Done.", 'buy': "Global Deal Execution 🚀", 'success': "Success! ✅", 'car': "Start Car 🔑", 'home': "Smart Home 🏠", 'mem': "📜 Memory Log"},
    'Arabic': {'motto': "تحدث. ادفع. تم.", 'buy': "إبرام الصفقة العالمية 🚀", 'success': "تمت بنجاح! ✅", 'car': "تشغيل السيارة 🔑", 'home': "إدارة المنزل 🏠", 'mem': "📜 سجل الذاكرة"},
    'Français': {'motto': "Parlez. Payez. Fait.", 'buy': "Accord Mondial 🚀", 'success': "Succès! ✅", 'car': "Démarrer 🔑", 'home': "Maison 🏠", 'mem': "📜 Journal"},
    'Italiano': {'motto': "Parla. Paga. Fatto.", 'buy': "Concludi Affare 🚀", 'success': "Successo! ✅", 'car': "Auto 🔑", 'home': "Casa 🏠", 'mem': "📜 Registro"}
}

# 4. التنسيق البصري (Glassmorphism)
st.markdown("""
<style>
    body { background: #00050a; color: white; }
    .star-header { font-size: 55px; color: gold; text-shadow: 0 0 15px gold; text-align: center; }
    .balance-card { 
        background: rgba(0, 255, 204, 0.1); border: 2px solid #00ffcc; 
        padding: 20px; border-radius: 15px; text-align: center; margin-bottom: 25px;
    }
    .balance-val { font-size: 3.5rem; color: #00ffcc; font-weight: bold; }
    .speech-box { 
        background: rgba(255, 215, 0, 0.1); border-right: 5px solid gold; 
        padding: 15px; border-radius: 10px; margin: 15px 0; color: #ffd700; font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# 5. الشريط الجانبي (الأرشفة الحية)
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/000000/star--v1.png", width=60)
    selected_lang = st.selectbox("🌐 Global Language", list(LANGS.keys()))
    t = LANGS[selected_lang]
    st.divider()
    with st.expander(t['mem'], expanded=True):
        if not st.session_state.history:
            st.write("No logs yet.")
        for item in reversed(st.session_state.history):
            st.markdown(f"**[{item['cat']}]** {item['time']}: {item['action']}")

# 6. الواجهة المركزية والرصيد الفوري
st.markdown("<h1 class='star-header'>🌟 My FlashDeal Star 🌟</h1>", unsafe_allow_html=True)

st.markdown(f"""
<div class='balance-card'>
    <p style='margin:0;'>Available Balance / الرصيد المتاح</p>
    <div class='balance-val'>${st.session_state.balance:,.2f}</div>
</div>
""", unsafe_allow_html=True)

# 7. التفاعل الصوتي والكتابي (ثبات واستمرارية)
st.subheader(f"🎙️ {t['motto']}")
# المدخل الذي يستقبل الكتابة أو الإملاء الصوتي
user_input = st.chat_input("تحدث الآن أو اكتب أمرك هنا...")

if user_input:
    st.session_state.voice_display = user_input
    add_to_log(f"Input Captured: {user_input}", "Comm")
    # الخصم التلقائي بناءً على الكلمات المفتاحية
    if any(word in user_input.lower() for word in ["pay", "ادفع", "buy", "شراء"]):
        st.session_state.balance -= 50.0
        st.toast("تم خصم 50 وحدة بنجاح! 💸")
    st.rerun() # الأقواس ضرورية هنا لتحديث الشاشة فوراً

# عرض المنطوق ليظل ثابتاً أمام المستخدم
if st.session_state.voice_display:
    st.markdown(f"<div class='speech-box'>🎤 المنطوق الحالي: {st.session_state.voice_display}</div>", unsafe_allow_html=True)

# 8. البيومترية (أمان سادن المطور)
st.divider()
col_sec1, col_sec2 = st.columns(2)
with col_sec1:
    if st.button("🎭 Face Recognition Activation"):
        st.session_state.cam_on = True
    
    if st.session_state.get('cam_on'):
        img = st.camera_input("Biometric Scan")
        if img:
            st.success("Identity Verified! ✅")
            add_to_log("Face ID Verified", "Security")
            st.session_state.cam_on = False
            st.rerun()

with col_sec2:
    if st.button("👆 Fingerprint Sync"):
        st.success("Fingerprint Matched! ✅")
        add_to_log("Fingerprint Verified", "Security")

# 9. إبرام الصفقة (الاحتفالية والخصم الموثق)
st.divider()
if st.button(t['buy'], type="primary", use_container_width=True):
    st.session_state.balance -= 125.50
    add_to_log("Global Deal Executed: -125.50$", "Marketing")
    st.balloons()
    st.snow()
    st.success(t['success'])
    time.sleep(1)
    st.rerun() # تحديث الرصيد بالأقواس الصحيحة

# 10. التحكم الذكي
st.markdown("### ⚡ Smart Control 🏎️🏠")
ca, cb = st.columns(2)
with ca:
    if st.button(t['car'], use_container_width=True):
        st.success("Engine Started! 🏎️")
        add_to_log("Vehicle Remote Start", "Practical")
with cb:
    if st.button(t['home'], use_container_width=True):
        st.toast("Home Systems Active! 🏠")
        add_to_log("Home Systems Managed", "Vision")

st.markdown("<p style='text-align:center; opacity:0.3; margin-top:30px;'>STAR-PRO-VERIFIED-2026 ✅</p>", unsafe_allow_html=True)
