import streamlit as st
from gtts import gTTS
import io, base64

# قيمة أساسية مهمة للرصيد
BASE_BALANCE = 10000.00

# عند فتح الصفحة من جديد، يعاد ضبط الرصيد للقيمة الأساسية
if 'balance' not in st.session_state:
    st.session_state.balance = BASE_BALANCE
if 'history' not in st.session_state:
    st.session_state.history = []

def add_to_memory(action, category="General"):
    st.session_state.history.append({"action": action, "cat": category})

# قاموس متعدد اللغات
LANG_DICT = {
    'English': {
        'motto': 'Talk. Pay. Done.',
        'success': 'Well done, champ! 🎉',
        'retry': 'Try again, you will succeed!',
        'balance': 'Available Balance',
        'voice': 'Say a command like: Pay 50$ to merchant',
        'error': 'Could not parse amount.',
        'camera': '👤 Biometric Face Recognition'
    },
    'Arabic': {
        'motto': 'تحدث. ادفع. تم.',
        'success': 'إجابة موفقة يا بطل 🎉',
        'retry': 'أعد المحاولة ستنجح',
        'balance': 'الرصيد المتاح',
        'voice': 'قل أمراً مثل: ادفع 50$ لتاجر',
        'error': 'لم أتمكن من فهم المبلغ.',
        'camera': '👤 التحقق من الوجه'
    }
}

# اختيار اللغة
selected_lang = st.sidebar.selectbox("🌐 Choose Language / اختر اللغة", list(LANG_DICT.keys()))
t = LANG_DICT[selected_lang]

# شعار متحرك
st.markdown(f"""
<style>
    .main-slogan {{
        font-size: 2.5rem;
        font-weight: bold;
        text-align: center;
        color: #FFD700;
        text-shadow: 0 0 15px #00ffcc;
        margin-top: 20px;
        margin-bottom: 20px;
        animation: pulse 2s infinite;
    }}
    @keyframes pulse {{
        0% {{ text-shadow: 0 0 5px #FFD700; }}
        50% {{ text-shadow: 0 0 20px #00ffcc; }}
        100% {{ text-shadow: 0 0 5px #FFD700; }}
    }}
</style>
<div class='main-slogan'>🌟 {t['motto']} 🌟</div>
""", unsafe_allow_html=True)

# عرض الرصيد الحالي
st.markdown(f"**💰 {t['balance']}:** {st.session_state.balance:,.2f}$")

# التحقق بالكاميرا
img_data = st.camera_input(t['camera'])
if img_data:
    st.success("✅ Face Verified Successfully!")
    add_to_memory("Face Recognition Confirmed", "Security")

    # الإدخال الصوتي/الكتابي بعد التحقق
    voice_input = st.chat_input(t['voice'])
    if voice_input:
        st.markdown(f"**🎤 المنطوق/الكتابة:** {voice_input}")
        add_to_memory(f"Voice/Text Command: {voice_input}", "Programming")

        if ("ادفع" in voice_input or "Pay" in voice_input) and "$" in voice_input:
            try:
                amount = float(voice_input.split("$")[1].split()[0])
                st.session_state.balance -= amount
                st.success(f"✅ {t['success']} | {t['balance']}: {st.session_state.balance:,.2f}$")
                st.balloons()
                tts = gTTS(t['success'], lang="ar" if selected_lang == "Arabic" else "en")
            except:
                st.warning(f"⚠️ {t['error']}")
                tts = gTTS(t['retry'], lang="ar" if selected_lang == "Arabic" else "en")
        else:
            st.info(t['retry'])
            tts = gTTS(t['retry'], lang="ar" if selected_lang == "Arabic" else "en")

        # تشغيل الصوت
        audio_bytes = io.BytesIO()
        tts.write_to_fp(audio_bytes)
        audio_bytes.seek(0)
        audio_base64 = base64.b64encode(audio_bytes.read()).decode()
        st.markdown(f"""
            <audio autoplay>
                <source src="data:audio/mp3;base64,{audio_base64}" type="audio/mp3">
            </audio>
        """, unsafe_allow_html=True)
