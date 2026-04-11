import streamlit as st
import time
from datetime import datetime

# 1. إعدادات المشروع (The Final Masterpiece)
st.set_page_config(page_title="My FlashDeal Star", page_icon="🌟", layout="wide")

# 2. إدارة الحالة الحية (ضمان الثبات)
if 'balance' not in st.session_state:
    st.session_state.balance = 1500.75
if 'history' not in st.session_state:
    st.session_state.history = []
if 'voice_display' not in st.session_state:
    st.session_state.voice_display = ""

def add_to_memory(action, category="General"):
    # إضافة الأقواس للدالة لضمان استخراج الوقت فوراً
    timestamp = datetime.now().strftime("%H:%M:%S") 
    st.session_state.history.append({"time": timestamp, "action": action, "cat": category})

# 3. القاموس اللغوي الرباعي
LANGS = {
    'English': {'motto': "Talk. Pay. Done.", 'buy': "Global Deal Execution 🚀", 'success': "Success! ✅", 'car': "Start Car 🔑", 'home': "Smart Home 🏠", 'mem': "📜 Memory Log"},
    'Arabic': {'motto': "تحدث. ادفع. تم.", 'buy': "إبرام الصفقة العالمية 🚀", 'success': "تمت بنجاح! ✅", 'car': "تشغيل السيارة 🔑", 'home': "إدارة المنزل 🏠", 'mem': "📜 سجل الذاكرة"},
    'Français': {'motto': "Parlez. Payez. Fait.", 'buy': "Accord Mondial 🚀", 'success': "Succès! ✅", 'car': "Démarrer 🔑", 'home': "Maison 🏠", 'mem': "📜 Journal"},
    'Italiano': {'motto': "Parla. Paga. Fatto.", 'buy': "Concludi Affare 🚀", 'success': "Successo! ✅", 'car': "Auto 🔑", 'home': "Casa 🏠", 'mem': "📜 Registro"}
}

# 4. التنسيق البصري (Cyber-Glass)
st.markdown("""
<style>
    body { background: linear-gradient(135deg, #00050a 0%, #011627 100%); color: white; }
    .star { font-size: 70px; color: gold; text-shadow: 0 0 20px gold; text-align: center; }
    .glass-card { padding: 20px; border-radius: 15px; background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); backdrop-filter: blur(10px); margin-bottom: 15px; }
    .balance-card { background: rgba(0, 255, 204, 0.1); border: 1px solid #00ffcc; padding: 15px; border-radius: 12px; text-align: center; }
    .speech-box { background: rgba(255, 215, 0, 0.1); border-right: 5px solid gold; padding: 12px; border-radius: 8px; color: gold; font-weight: bold; }
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

# 6. الواجهة المركزية
st.markdown("<h1 style='text-align:center;'>🌟 My FlashDeal Star 🌟</h1>", unsafe_allow_html=True)
st.markdown('<div class="star">★</div>', unsafe_allow_html=True)

st.markdown(f"""
<div class='balance-card'>
    <p style='margin:0; font-size: 0.9rem;'>Available Balance / الرصيد المتاح</p>
    <h2 style='color:#00ffcc; margin:0;'>${st.session_state.balance:,.2f}</h2>
</div>
""", unsafe_allow_html=True)

# 7. التفاعل الصوتي والكتابي
st.divider()
st.subheader(f"🎙️ {t['motto']}")
user_input = st.chat_input("تحدث أو اكتب أمرك هنا...")

if user_input:
    st.session_state.voice_display = user_input
    add_to_memory(f"Input: {user_input}", "Programming")
    if any(word in user_input.lower() for word in ["pay", "ادفع", "buy", "شراء"]):
        st.session_state.balance -= 50.0
        st.toast("تم الخصم بنجاح! 💸")
    st.rerun()

if st.session_state.voice_display:
    st.markdown(f"<div class='speech-box'>🎤 **المنطوق:** {st.session_state.voice_display}</div>", unsafe_allow_html=True)

# 8. البيومترية (تم إضافة الأقواس وتصحيح المنطق)
st.divider()
col_a, col_b = st.columns(2)
with col_a:
    # استخدام الأقواس في الشروط والأوامر لضمان الدقة
    if st.button("🎭 Face Recognition Activation"):
        st.session_state.cam_on = True
    
    if st.session_state.get('cam_on'):
        img = st.camera_input("Biometric Scan")
        if img:
            st.success("Identity Verified! ✅")
            add_to_memory("Face ID Verified", "Security")
            st.session_state.cam_on = False

with col_b:
    if st.button("👆 Fingerprint Sync"):
        st.success("Fingerprint Matched! ✅")
        add_to_memory("Fingerprint Verified", "Security")

# 9. إبرام الصفقة (الاحتفالية والخصم الحي)
st.divider()
if st.button(t['buy'], type="primary", use_container_width=True):
    st.session_state.balance -= 125.50
    add_to_memory("Deal Concluded", "Marketing")
    st.balloons()
    st.snow()
    st.success(t['success'])
    time.sleep(1)
    st.rerun() # إعادة التشغيل بالأقواس لتحديث الرصيد

# 10. التحكم الذكي
st.markdown("### ⚡ Smart Control 🏎️🏠")
ca, cb = st.columns(2)
with ca:
    if st.button(t['car'], use_container_width=True):
        st.success("Vehicle Started! 🏎️")
        add_to_memory("Car Started", "Practical")
with cb:
    if st.button(t['home'], use_container_width=True):
        st.toast("Home Systems Online! 🏠")
        add_to_memory("Home Managed", "Future Vision")

st.markdown("<p style='text-align:center; opacity:0.3; margin-top:30px;'>STAR-PRO-VERIFIED-2026 ✅</p>", unsafe_allow_html=True)

