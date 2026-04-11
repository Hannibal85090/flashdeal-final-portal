import streamlit as st
import time
from gtts import gTTS
import io, base64

# إعداد الصفحة
st.set_page_config(page_title="My FlashDeal Star", page_icon="🌟", layout="wide")

# الذاكرة الموحدة
if 'history' not in st.session_state:
    st.session_state.history = []

def add_to_memory(action):
    timestamp = time.strftime("%H:%M:%S")
    st.session_state.history.append(f"[{timestamp}] - {action}")

# دوال الأوامر الأمنية
def trigger_emergency_protocol():
    st.error("🚨 SOS: Emergency Protocol Activated!")
    add_to_memory("SOS Triggered - Alerts sent to Master Alpha Hub")
    with st.status("Verifying Security Links..."):
        time.sleep(1)
        st.warning("All Smart Links: IMMOBILIZED 🔒")

def handle_sign():
    st.info("✋ Sign command triggered")
    st.success("Gesture recognized successfully!")
    add_to_memory("Sign Triggered")

def handle_lock():
    st.warning("🔒 Lock engaged")
    st.success("Security protocol activated!")
    add_to_memory("Lock Triggered")

def handle_face():
    st.info("👤 Face recognition triggered")
    st.success("Identity verified!")
    add_to_memory("Face Triggered")

def handle_key():
    st.info("🔑 Key command triggered")
    st.success("Access granted!")
    add_to_memory("Key Triggered")

# دالة الصوت
def speak_answer(answer_text, lang="ar"):
    tts = gTTS(answer_text, lang=lang)
    audio_bytes = io.BytesIO()
    tts.write_to_fp(audio_bytes)
    audio_bytes.seek(0)
    audio_base64 = base64.b64encode(audio_bytes.read()).decode()
    st.markdown(f"""
        <audio autoplay>
            <source src="data:audio/mp3;base64,{audio_base64}" type="audio/mp3">
        </audio>
    """, unsafe_allow_html=True)

# تنسيق الواجهة
st.markdown("""
<style>
body{background:linear-gradient(135deg,#00050a 0%,#011627 100%);color:#ffffff;}
.star{font-size:120px;color:gold;text-shadow:0 0 20px #ffd700,0 0 40px #ffcc00;text-align:center;margin:40px 0;}
.icon-circle{display:inline-block;margin:20px;font-size:40px;color:#ffcc00;border:2px solid #ffcc00;border-radius:50%;padding:20px;}
.glass-card{padding:25px;border-radius:20px;background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.1);backdrop-filter:blur(15px);margin-bottom:20px;}
.log-text{font-size:0.85rem;color:#4facfe;font-family:'Courier New',monospace;}
</style>
""", unsafe_allow_html=True)

# القاموس متعدد اللغات
LANG_DICT = {
'English':{'motto':"Talk. Pay. Done.",'saden':"Saden Security: Mutual Token",'home_car':"Smart Control 🏠🚗",'buy':"Global Deal Execution 🚀",'success':"Process Completed Successfully!",'sync':"Sync Token 🛡️",'car':"Start Car 🔑",'home':"Manage Home 🏠",'sos':"Activate SOS Mode 🔔",'mem':"📜 Unified Memory Log"},
'Français':{'motto':"Parlez. Payez. Fait.",'saden':"Sécurité Saden: Token Mutuel",'home_car':"Contrôle Maison & Voiture 🏠🚗",'buy':"Conclure l'Accord 🚀",'success':"Opération terminée!",'sync':"Synchroniser 🛡️",'car':"Démarrer 🔑",'home':"Gérer Maison 🏠",'sos':"Activer SOS 🔔",'mem':"📜 Journal de Mémoire"},
'Italiano':{'motto':"Parla. Paga. Fatto.",'saden':"Sicurezza Saden: Token Reciproco",'home_car':"Controllo Casa e Auto 🏠🚗",'buy':"Concludi l'Affare 🚀",'success':"Operazione riuscita!",'sync':"Sincronizza 🛡️",'car':"Avvia Auto 🔑",'home':"Gestisci Casa 🏠",'sos':"Attiva SOS 🔔",'mem':"📜 Registro di Memoria"},
'Arabic':{'motto':"تحدث. ادفع. تم.",'saden':"أمان سادن: التوكن المتبادل",'home_car':"التحكم الذكي 🏠🚗",'buy':"إبرام الصفقة العالمية 🚀",'success':"تمت العملية بنجاح!",'sync':"مزامنة التوكن 🛡️",'car':"تشغيل السيارة 🔑",'home':"إدارة المنزل 🏠",'sos':"تفعيل وضع الطوارئ 🔔",'mem':"📜 سجل الذاكرة الموحد"}}

# الشريط الجانبي
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/000000/star--v1.png", width=60)
    selected_lang = st.selectbox("🌐 Global Language", list(LANG_DICT.keys()))
    t = LANG_DICT[selected_lang]
    st.divider()
    if st.button(t['sos'], type="secondary"): trigger_emergency_protocol()
    st.divider()
    with st.expander(t['mem'], expanded=True):
        if not st.session_state.history: st.write("No active logs.")
        else:
            for item in reversed(st.session_state.history):
                st.markdown(f"<p class='log-text'>{item}</p>", unsafe_allow_html=True)
    st.divider()
    acc = st.radio("Access Level", ["Standard", "Master Alpha 🔓"])

# العنوان والتوقيت
current_time = time.strftime("%d/%m/%Y - %H:%M:%S")
st.markdown("<h1 style='text-align:center;color:#000000;text-shadow:0 0 10px #444444;'>🌟 My FlashDeal Star 🌟</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align:center;color:#4facfe;'>🕒 Current Time: {current_time}</p>", unsafe_allow_html=True)
st.markdown('<div class="star">★</div>', unsafe_allow_html=True)

# الأزرار الرئيسية
cols = st.columns(4)
if cols[0].button("✋ Hand / Sign"): handle_sign()
if cols[1].button("🔒 Lock / Sync"): handle_lock()
if cols[2].button("👤 Face / Voice"): handle_face()
if cols[3].button("🔑 Key / Car"): handle_key()

# التوكن الأمني
st.markdown(f'<div class="glass-card"><h3>🔒 {t["saden"]}</h3>', unsafe_allow_html=True)
c1, c2 = st.columns([3,1])
with c1: st.text_input("Token ID", type="password", label_visibility="collapsed", key="token_main")
with c2:
    if st.button(t['sync']):
        st.success("Linked! ✅")
        add_to_memory(f"Token Synced: {selected_lang}")
st.markdown('</div>', unsafe_allow_html=True)

# التبويبات (صوت / إشارة / نص)
tab1, tab2, tab3 = st.tabs(["🎙️ Voice","👋 Sign","⌨️ Text"])
with tab1:
    if st.button(f"{t['motto']} (Mic Active)"):
        answer = "سعر المنتج ESP32-S3 هو 15 دولار."
        st.write(answer)
        speak_answer(answer, lang="ar")
        add_to_memory("Voice command engaged with audio response")
with tab3:
    chat_val = st.chat_input("Sony-Agent...")
    if chat_val:
        add_to_memory(f"Chat: {chat_val}")
        st.write(f"Agent Reply: {chat_val}")
        speak_answer(f"تم استلام طلبك: {chat_val}", lang="ar")

# التحكم الذكي
st.markdown(f"### {t['home_car']}")
ca, cb = st.columns(2)
with ca:
    if st.button(t['car']):
        with st.status("Linking..."):
            time.sleep(1)
            st.success("🚗 Engine On!")
        add_to_memory("Car Started")
with cb:
    if st.button(t['home']):
        st.toast("🏠 Welcome Home Mode Active")
        add_to_memory("Home Managed")

# السعر والمواصفات
st.divider()
colA, colB = st.columns([1,2])
with colA:
    st.metric("Price", "$99.99")
    st.metric("System Stability", "100%", "Secure")
    st.write("Rating:")
    st.markdown("<span style='color:green;'>★ ★ ★ ★ ☆</span>", unsafe_allow_html=True)
with colB:
    if st.button(t['buy'], type="primary", use_container_width=True):
        st.progress(100)
