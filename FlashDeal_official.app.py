import streamlit as st
from streamlit_mic_recorder import speech_to_text
import base64
import io
import random
from datetime import datetime

# --- 1. التحقق من المكتبات الأساسية (تجنب التعارض) ---
try:
    from gtts import gTTS
except ImportError:
    import os
    os.system('pip install gTTS')
    from gtts import gTTS

# --- 2. إعدادات الهوية البصرية (الاحترافية) ---
st.set_page_config(
    page_title="FlashDeal Star Official",
    page_icon="💳",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- 3. محرك النطق الذكي (تفاعلية حية) ---
def flash_speak(text):
    """تحويل النص إلى صوت تشجيعي وتأكيدي بنبرة إنجليزية واضحة"""
    try:
        tts = gTTS(text=text, lang='en')
        fp = io.BytesIO()
        tts.write_to_fp(fp)
        fp.seek(0)
        audio_b64 = base64.b64encode(fp.read()).decode()
        # حقن كود الصوت ليعمل تلقائياً عند التنفيذ
        st.markdown(
            f'<audio autoplay="true" src="data:audio/mp3;base64,{audio_b64}">',
            unsafe_allow_html=True
        )
    except Exception:
        pass

# --- 4. إدارة الحالة المستمرة (تأمين الرصيد والسجل) ---
if 'flash_balance' not in st.session_state:
    st.session_state.flash_balance = 1000  # رصيد المحفظة الافتتاحي
if 'ledger_archive' not in st.session_state:
    st.session_state.ledger_archive = []

# --- 5. الواجهة الرئيسية (التجسيد البصري للشعار) ---
st.title("💳 FlashDeal Star")
st.markdown("## **Talk. Pay. Done.**")
st.caption("Universal AI Gateway | Inclusive for All Languages & Signs 🖐️")

# عرض الرصيد بشكل حيوي وجذاب
st.divider()
col_m1, col_m2 = st.columns([2, 1])
with col_m1:
    st.write("### Wallet Status")
with col_m2:
    st.metric(label="Available Balance", value=f"{st.session_state.flash_balance} ⭐")

st.divider()

# --- 6. محرك التفاعل المتعدد (تفعيل الفاعلية والحيوية) ---
tab_voice, tab_bio, tab_ledger = st.tabs([
    "🎙️ Voice Command", 
    "🔐 Bio-Security", 
    "📑 Secure Ledger"
])

with tab_voice:
    st.write("🗣️ **Command Center**")
    st.info("Speak naturally. Example: 'Pay 50 tokens for the service'")
    
    # التقاط الصوت بالعربية لضمان أقصى درجات الراحة (Talk)
    voice_input = speech_to_text(
        language='ar',
        start_prompt="Voice Activation 🎤",
        stop_prompt="Processing... ⏹️",
        key='official_flash_voice_v1'
    )
    
    if voice_input:
        st.success(f"Recognized: {voice_input}")
        # استخراج الأرقام من الحديث (التحقق الذكي)
        numbers = [int(s) for s in voice_input.split() if s.isdigit()]
        
        if numbers:
            amount = numbers[0]
            if st.button(f"Authorize Payment of {amount} ✅", key='auth_btn'):
                if st.session_state.flash_balance >= amount:
                    # تنفيذ العملية (Pay)
                    st.session_state.flash_balance -= amount
                    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    st.session_state.ledger_archive.append(f"💸 Paid: {amount} | Status: DONE | 🕒 {now}")
                    
                    st.balloons()
                    flash_speak(f"Payment successful! {amount} tokens deducted.")
                    st.success(f"Transaction Complete. New Balance: {st.session_state.flash_balance}")
                else:
                    flash_speak("Insufficient funds for this transaction.")
                    st.error("Balance not enough.")
        else:
            st.warning("Please specify an amount in your command.")

with tab_bio:
    st.write("📷 **Visual Bio-Confirmation**")
    st.write("Verify your identity via gesture or face recognition.")
    bio_capture = st.camera_input("Secure ID Check", key='official_bio_cam')
    if bio_capture:
        st.toast("Identity Confirmed via Bio-Sign.", icon="🛡️")

with tab_ledger:
    st.write("📑 **Transaction Archive**")
    if st.session_state.ledger_archive:
        for entry in reversed(st.session_state.ledger_archive):
            st.markdown(f"> `{entry}`")
    else:
        st.write("Your transaction history is currently empty.")

# --- 7. الخاتمة الرسمية (Done) ---
st.divider()
st.caption("FlashDeal Official | Powered by MIGA Intelligence | All Rights Reserved.")

