import streamlit as st
import time
from datetime import datetime

# 1. الإعدادات الأساسية (كما في الصور)
st.set_page_config(page_title="My FlashDeal Star", page_icon="🌟", layout="wide")

if 'history' not in st.session_state:
    st.session_state.history = []
if 'balance' not in st.session_state:
    st.session_state.balance = 1500.75

def add_to_memory(action):
    timestamp = datetime.now().strftime("%H:%M:%S")
    st.session_state.history.append(f"[{timestamp}] - {action}")

# 2. القاموس اللغوي الكامل (اللغات الأربع)
LANG_DICT = {
    'English': {'motto': 'Talk. Pay. Done.', 'saden': 'Saden Security: Mutual Token', 'home_car': 'Smart Control 🏠🚗', 'buy': 'Global Deal', 'success': 'Process Completed Successfully!', 'sync': 'Sync Token 🛡️', 'car': 'Start Car 🔑', 'home': 'Manage Home 🏠', 'sos': 'Activate SOS Mode 🔔', 'mem': '📜 Unified Memory Log'},
    'Français': {'motto': 'Parlez. Payez. Fait.', 'saden': 'Sécurité Saden: Token Mutuel', 'home_car': 'Contrôle Maison & Voiture 🏠🚗', 'buy': 'Conclure l\'Accord 🚀', 'success': 'Opération terminée! ✅', 'sync': 'Synchroniser 🛡️', 'car': 'Démarrer 🔑', 'home': 'Gérer Maison 🏠', 'sos': 'Activer SOS 🔔', 'mem': '📜 Journal de Mémoire'},
    'Italiano': {'motto': 'Parla. Paga. Fatto.', 'saden': 'Sicurezza Saden: Token Reciproco', 'home_car': 'Controllo Casa e Auto 🏠🚗', 'buy': 'Concludi l\'Affare 🚀', 'success': 'Operazione riuscita! ✅', 'sync': 'Sincronizza 🛡️', 'car': 'Avvia Auto 🔑', 'home': 'Gestisci Casa 🏠', 'sos': 'Attiva SOS 🔔', 'mem': '📜 Registro di Memoria'},
    'Arabic': {'motto': 'تحدث. ادفع. تم.', 'saden': 'أمان سادن: التوكن المتبادل', 'home_car': 'التحكم الذكي 🏠🚗', 'buy': 'إبرام الصفقة العالمية 🚀', 'success': 'تمت العملية بنجاح! ✅', 'sync': 'مزامنة التوكن 🛡️', 'car': 'تشغيل السيارة 🔑', 'home': 'إدارة المنزل 🏠', 'sos': 'تفعيل وضع الطوارئ 🔔', 'mem': '📜 سجل الذاكرة الموحد'}
}

# 3. التصميم البصري (Cyber-Tech)
st.markdown("""
<style>
    body { background: linear-gradient(135deg, #00050a 0%, #011627 100%); color: #ffffff; }
    .glass-card { padding: 25px; border-radius: 20px; background: rgba(255, 255, 255, 0.05); border: 1px solid rgba(255,255,255,0.1); backdrop-filter: blur(15px); }
    .log-text { font-size: 0.85rem; color: #4facfe; font-family: 'Courier New', monospace; }
</style>
""", unsafe_allow_html=True)

# 4. الشريط الجانبي (الأرشيف واللغات)
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/000000/star--v1.png", width=60)
    selected_lang = st.selectbox("🌐 Global Language", list(LANG_DICT.keys()))
    t = LANG_DICT[selected_lang]
    st.divider()
    if st.button(t['sos'], type="secondary"):
        st.error(t['sos'])
        add_to_memory("SOS Triggered")
    st.divider()
    with st.expander(t['mem'], expanded=True):
        if not st.session_state.history: st.write("No active logs.")
        else:
            for item in reversed(st.session_state.history):
                st.markdown(f"<p class='log-text'>{item}</p>", unsafe_allow_html=True)

# 5. الواجهة الرئيسية
st.markdown(f"<h1 style='text-align:center;'>🌟 My FlashDeal Star 🌟</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align:center;'>💰 {st.session_state.balance:,.2f} USD</p>", unsafe_allow_html=True)

# التفاعل الصوتي (يكتب النص ويؤرشفه)
voice_val = st.chat_input("تحدث الآن... (Talk. Pay. Done.)")
if voice_val:
    st.write(f"🎤 {voice_val}")
    add_to_memory(f"Voice Command: {voice_val}")

# أزرار التحكم الفوري
cols = st.columns(4)
with cols[0]:
    if st.button("👆 Fingerprint"): add_to_memory("Fingerprint Verified")
with cols[1]:
    if st.button("🎭 Face ID"):
        img = st.camera_input("Face Scan")
        if img: add_to_memory("Face Captured")
with cols[2]:
    if st.button("🎙️ Voice Cmd"): add_to_memory("Voice Session Active")
with cols[3]:
    if st.button("🔑 Key Sync"): add_to_memory("Key Synchronized")

# إبرام الصفقة والاحتفالية
st.markdown("---")
if st.button(t['buy'], type="primary", use_container_width=True):
    st.balloons()
    st.snow()
    st.success(t['success'])
    add_to_memory(f"Deal Concluded: {selected_lang}")
    st.session_state.balance -= 100
    time.sleep(1)
    st.rerun()

# أزرار المنزل والسيارة (الطاعة للصور)
c1, c2 = st.columns(2)
with c1:
    if st.button(t['car']):
        with st.status("Linking..."):
            time.sleep(1)
            st.success("Engine On! 🏎️")
            add_to_memory("Car Started")
with c2:
    if st.button(t['home']):
        st.toast(t['home'])
        add_to_memory("Home Managed")
