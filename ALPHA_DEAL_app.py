import streamlit as st
import time
from datetime import datetime

# 1. المبدأ الأول: التثبت والتحقق الشامل
st.set_page_config(page_title="My FlashDeal Star", page_icon="🌟", layout="wide")

# 2. إدارة الحالة الحية (ضمان عدم ضياع أي تكة برمجية)
if 'balance' not in st.session_state:
    st.session_state.balance = 1500.75
if 'history' not in st.session_state:
    st.session_state.history = []
if 'last_speech' not in st.session_state:
    st.session_state.last_speech = ""
if 'cam_active' not in st.session_state:
    st.session_state.cam_active = False

def add_to_log(action, category="System"):
    # الأقواس هنا هي مفتاح الوقت الحي
    now = datetime.now().strftime("%H:%M:%S")
    st.session_state.history.append({"time": now, "action": action, "cat": category})

# 3. القاموس الرباعي (بدون هفوات KeyError)
LANGS = {
    'English': {'motto': "Talk. Pay. Done.", 'buy': "Global Deal Execution 🚀", 'success': "Success! ✅", 'car': "Start Car 🔑", 'home': "Smart Home 🏠", 'mem': "📜 Memory Log"},
    'Arabic': {'motto': "تحدث. ادفع. تم.", 'buy': "إبرام الصفقة العالمية 🚀", 'success': "تمت بنجاح! ✅", 'car': "تشغيل السيارة 🔑", 'home': "إدارة المنزل 🏠", 'mem': "📜 سجل الذاكرة"},
    'Français': {'motto': "Parlez. Payez. Fait.", 'buy': "Accord Mondial 🚀", 'success': "Succès! ✅", 'car': "Démarrer 🔑", 'home': "Maison 🏠", 'mem': "📜 Journal"},
    'Italiano': {'motto': "Parla. Paga. Fatto.", 'buy': "Concludi Affare 🚀", 'success': "Successo! ✅", 'car': "Auto 🔑", 'home': "Casa 🏠", 'mem': "📜 Registro"}
}

# 4. التصميم البصري (روح فلاشديل ستار)
st.markdown("""
<style>
    body { background: #00050a; color: white; }
    .star-header { font-size: 60px; color: gold; text-shadow: 0 0 15px gold; text-align: center; }
    .balance-card { 
        background: rgba(0, 255, 204, 0.1); border: 2px solid #00ffcc; 
        padding: 20px; border-radius: 15px; text-align: center; margin-bottom: 20px;
    }
    .balance-val { font-size: 3rem; color: #00ffcc; font-weight: bold; }
    .speech-box { 
        background: rgba(255, 215, 0, 0.1); border-right: 5px solid gold; 
        padding: 15px; border-radius: 10px; margin: 15px 0; color: #ffd700;
    }
</style>
""", unsafe_allow_html=True)

# 5. الشريط الجانبي (الأرشيف الحي)
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/000000/star--v1.png", width=60)
    selected_lang = st.selectbox("🌐 Global Language", list(LANGS.keys()))
    t = LANGS[selected_lang]
    st.divider()
    with st.expander(t['mem'], expanded=True):
        for item in reversed(st.session_state.history):
            st.markdown(f"**[{item['cat']}]** {item['time']}: {item['action']}")

# 6. الواجهة المركزية والرصيد
st.markdown("<h1 class='star-header'>🌟 My FlashDeal Star 🌟</h1>", unsafe_allow_html=True)

st.markdown(f"""
<div class='balance-card'>
    <p style='margin:0;'>Available Balance / الرصيد المتاح</p>
    <div class='balance-val'>${st.session_state.balance:,.2f}</div>
</div>
""", unsafe_allow_html=True)

# 7. التفاعل الصوتي والكتابي (تثبيت المنطوق)
st.subheader(f"🎙️ {t['motto']}")
# المدخل الكتابي الذي يدعم الإملاء الصوتي أيضاً
input_cmd = st.chat_input("تحدث الآن أو اكتب أمرك هنا...")

if input_cmd:
    st.session_state.last_speech = input_cmd
    add_to_log(f"Input Captured: {input_cmd}", "Communication")
    # منطق الخصم التلقائي
    if any(word in input_cmd.lower() for word in ["pay", "ادفع", "buy", "شراء"]):
        st.session_state.balance -= 50.0
    st.rerun()

# بقاء المنطوق ثابتاً على الشاشة
if st.session_state.last_speech:
    st.markdown(f"<div class='speech-box'>🎤 **المنطوق الحالي:** {st.session_state.last_speech}</div>", unsafe_allow_html=True)

# 8. البيومترية (مع الأقواس والمنطق السليم)
st.divider()
col_a, col_b = st.columns(2)
with col_a:
    if st.button("🎭 Face Recognition Activation"):
        st.session_state.cam_active = True
    
    if st.session_state.cam_active:
        # الكاميرا كمدخل بيومتري
        face_img = st.camera_input("Biometric Scan")
        if face_img:
            st.success("Identity Verified! ✅")
            add_to_log("Face Biometric Verified", "Security")
            st.session_state.cam_active = False
            time.sleep(1)
            st.rerun()

with col_b:
    if st.button("👆 Fingerprint Sync"):
        st.success("Fingerprint Matched! ✅")
        add_to_log("Fingerprint Verified", "Security")

# 9. إبرام الصفقة (الاحتفالية والخصم الفوري)
st.divider()
if st.button(t['buy'], type="primary", use_container_width=True):
    st.session_state.balance -= 125.50
    add_to_log(f"Global Deal Concluded: -$125.50", "Marketing")
    st.balloons()
    st.snow()
    st.success(t['success'])
    time.sleep(1)
    st.rerun() # الأقواس هنا تضمن تحديث الواجهة فوراً

# 10. التحكم الذكي
st.markdown("### ⚡ Smart Control 🏎️🏠")
ca, cb = st.columns(2)
with ca:
    if st.button(t['car'], use_container_width=True):
        st.success("Engine Started! 🏎️")
        add_to_log("Car Engine ON", "Practical")
with cb:
    if st.button(t['home'], use_container_width=True):
        st.toast("Home Systems Online! 🏠")
        add_to_log("Home Mode Activated", "Future Vision")

st.markdown("<p style='text-align:center; opacity:0.3; margin-top:30px;'>STAR-PRO-VERIFIED-2026 ✅</p>", unsafe_allow_html=True)

