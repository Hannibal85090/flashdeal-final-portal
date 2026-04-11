import streamlit as st
import time
from datetime import datetime

# 1. تثبيت القاعدة (الأقواس هي السيادة)
st.set_page_config(page_title="My FlashDeal Star", page_icon="🌟", layout="wide")

# 2. إدارة الحالة الحية
if 'balance' not in st.session_state:
    st.session_state.balance = 1500.75
if 'history' not in st.session_state:
    st.session_state.history = []
if 'voice_display' not in st.session_state:
    st.session_state.voice_display = ""

def add_to_log(action):
    # الأقواس () هنا تجلب الوقت فوراً
    now = datetime.now().strftime("%H:%M:%S")
    st.session_state.history.append(f"[{now}] - {action}")

# 3. القاموس اللغوي المنضبط
LANGS = {
    'English': {'motto': "Talk. Pay. Done.", 'buy': "Global Deal 🚀", 'car': "Start Car 🔑", 'home': "Home 🏠", 'mem': "📜 Log", 'success': "Success! ✅"},
    'Arabic': {'motto': "تحدث. ادفع. تم.", 'buy': "إبرام الصفقة 🚀", 'car': "تشغيل السيارة 🔑", 'home': "إدارة المنزل 🏠", 'mem': "📜 السجل", 'success': "تمت بنجاح! ✅"},
    'Français': {'motto': "Parlez. Payez. Fait.", 'buy': "Accord 🚀", 'car': "Démarrer 🔑", 'home': "Maison 🏠", 'mem': "📜 Journal", 'success': "Succès! ✅"},
    'Italiano': {'motto': "Parla. Paga. Fatto.", 'buy': "Affare 🚀", 'car': "Auto 🔑", 'home': "Casa 🏠", 'mem': "📜 Registro", 'success': "Successo! ✅"}
}

# 4. التنسيق البصري (Cyber-Glass)
st.markdown("""
<style>
    body { background: #00050a; color: white; }
    .star-header { font-size: 50px; color: gold; text-shadow: 0 0 15px gold; text-align: center; }
    .balance-card { 
        background: rgba(0, 255, 204, 0.1); border: 2px solid #00ffcc; 
        padding: 20px; border-radius: 15px; text-align: center; margin-bottom: 20px;
    }
    .balance-val { font-size: 3rem; color: #00ffcc; font-weight: bold; }
    .speech-box { 
        background: rgba(255, 215, 0, 0.1); border-right: 5px solid gold; 
        padding: 15px; border-radius: 10px; margin: 15px 0; color: #ffd700; font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# 5. الشريط الجانبي ( Sidebar() - مع الأقواس المنضبطة )
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/000000/star--v1.png", width=60)
    # استخدام list() و keys() بالأقواس لاستخراج اللغات من القاموس
    available_langs = list(LANGS.keys())
    lang_choice = st.selectbox("🌐 Global Language", available_langs)
    t = LANGS[lang_choice]
    st.divider()
    # دالة التوسيع بالأقواس ()
    with st.expander(t['mem'], expanded=True):
        if not st.session_state.history:
            st.write("No active logs.")
        for item in reversed(st.session_state.history):
            st.markdown(f"<small style='color:#4facfe;'>{item}</small>", unsafe_allow_html=True)

# 6. الواجهة المركزية والرصيد الفوري (مع الأقواس)
st.markdown("<h1 class='star-header'>🌟 My FlashDeal Star 🌟</h1>", unsafe_allow_html=True)

st.markdown(f"""
<div class='balance-card'>
    <p style='margin:0;'>Available Balance / الرصيد المتاح</p>
    <div class='balance-val'>${st.session_state.balance:,.2f}</div>
</div>
""", unsafe_allow_html=True)

# 7. التفاعل ومنطق الخصم الفوري ( rerun() بالأقواس )
st.divider()
st.subheader(f"🎙️ {t['motto']}")
# دالة الإدخال بالأقواس ()
user_input = st.chat_input("تحدث أو اكتب أمرك هنا...")

if user_input:
    st.session_state.voice_display = user_input
    add_to_log(f"Input: {user_input}")
    
    # تنفيذ الخصم التلقائي
    if any(word in user_input.lower() for word in ["pay", "ادفع", "buy", "شراء"]):
        st.session_state.balance -= 50.0
        st.toast("تم الخصم فورا! 💸")
    
    # القوسان هنا () هما ما يضمن تحديث الرصيد على الشاشة فورا
    st.rerun()

# تثبيت عرض المنطوق (الصندوق الذهبي)
if st.session_state.voice_display:
    st.markdown(f"<div class='speech-box'>🎤 المنطوق الحالي: {st.session_state.voice_display}</div>", unsafe_allow_html=True)

# 8. التحكم الذاتي (أقواس أزرار الأفعال)
st.divider()
st.subheader("⚡ Smart Control")
ca, cb = st.columns(2)
with ca:
    # الأقواس () هنا هي التي تجعل الزر يستجيب للضغطة
    if st.button(t['car'], use_container_width=True):
        st.success("Vehicle Started! 🏎️")
        add_to_log("Car ON")
with cb:
    if st.button(t['home'], use_container_width=True):
        st.toast("Home Systems Online! 🏠")
        add_to_log("Home Managed")

# 9. إبرام الصفقة والاحتفالية (أقواس التنفيذ النهائي)
st.divider()
# دالة الزر بالأقواس ()
if st.button(t['buy'], type="primary", use_container_width=True):
    st.session_state.balance -= 125.50
    add_to_log("Global Deal Executed")
    # إطلاق المؤثرات بالأقواس () لتعمل فعليا
    st.balloons()
    st.snow()
    st.success(t['success'])
    time.sleep(1) # دالة الانتظار بالأقواس ()
    st.rerun()    # تحديث نهائي بالأقواس () لخصم المبلغ من الشاشة فورا

st.markdown("<p style='text-align:center; opacity:0.3; margin-top:30px;'>STAR-PRO-VERIFIED ✅</p>", unsafe_allow_html=True)
