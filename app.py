import streamlit as st
import time

# --- [1. محرك اللغات الديناميكي] ---
if 'lang' not in st.session_state:
    st.session_state.lang = "Arabic"

translations = {
    "Arabic": {
        "motto": ". تكلم ، ادفع ، تم .", "saden": "🛡️ أمان سادن", "assets": "🏠 التحكم في الأصول",
        "car": "🚗 تشغيل السيارة", "home": "🏠 أمن المنزل", "deal": "🤝 إبرام الصفقة",
        "sony": "🤝 الوكيل صوني", "log": "سجل الذاكرة", "sys_ready": "النظام جاهز للسيادة"
    },
    "English": {
        "motto": ". Speak , Pay , Done .", "saden": "🛡️ Saden Security", "assets": "🏠 Asset Control",
        "car": "🚗 Start Engine", "home": "🏠 Home Security", "deal": "🤝 Finalize Deal",
        "sony": "🤝 Sony Agent", "log": "Memory Log", "sys_ready": "System Ready"
    },
    "Italiano": {
        "motto": ". Parla , Paga , Fatto .", "saden": "🛡️ Sicurezza Saden", "assets": "🏠 Controllo Asset",
        "car": "🚗 Avvia Motore", "home": "🏠 Sicurezza Casa", "deal": "🤝 Concludi Affare",
        "sony": "🤝 Agente Sony", "log": "Registro", "sys_ready": "Sistema Pronto"
    }
}

# --- [2. الواجهة البصرية (CSS)] ---
st.markdown("""
<style>
    .stApp { background: linear-gradient(180deg, #001a33 0%, #003366 100%); color: white; }
    .header-box { text-align: center; margin-top: -60px; }
    .main-title { color: white; font-size: 50px; font-weight: bold; text-shadow: 0 0 20px #fff; }
    .star-side { color: gold; font-size: 40px; margin: 0 15px; vertical-align: middle; }
    .star-mega { text-align: center; font-size: 80px; color: gold; text-shadow: 0 0 30px gold; margin-top: -25px; }
    .motto-bar { background: white; color: black; font-size: 24px; font-weight: bold; padding: 8px 45px; border-radius: 12px; border: 3px solid gold; width: fit-content; margin: 10px auto; }
</style>
""", unsafe_allow_html=True)

# --- [3. التحكم الجانبي] ---
with st.sidebar:
    st.session_state.lang = st.selectbox("🌐 Languages / اللغات", ["Arabic", "English", "Italiano"], index=0)
    t = translations[st.session_state.lang] # تفعيل الترجمة المختارة فوراً
    st.divider()
    with st.expander(f"📜 {t['log']}", expanded=True):
        st.write(f"[{time.strftime('%H:%M')}] {t['sys_ready']}")

# --- [4. العرض الرئيسي المتجاوب] ---
st.markdown(f'<div class="header-box"><span class="star-side">✨</span><span class="main-title">My FlashDeal Star</span><span class="star-side">✨</span></div>', unsafe_allow_html=True)
st.markdown('<div class="star-mega">★</div>', unsafe_allow_html=True)
st.markdown(f'<div class="motto-bar">{t["motto"]}</div>', unsafe_allow_html=True)
st.markdown(f'<div style="text-align:center; color:#00ffff;">{time.strftime("%d/%m/%Y - %H:%M:%S")}</div>', unsafe_allow_html=True)

# 6. الأزرار الخماسية
cols = st.columns(5)
btn_labels = ["👤 Face ID", "🔑 Key", "✋ Hand", "🔒 Lock", "💎 Jewel"]
for i, col in enumerate(cols): col.button(btn_labels[i], use_container_width=True)

st.divider()

# 7-11. الأمان والأصول (مترجمة)
c_left, c_right = st.columns(2)
with c_left:
    st.markdown(f'<div style="background:white; border-radius:10px; padding:10px; border:2px solid gold;"><b style="color:black; font-size:20px;">{t["saden"]}</b></div>', unsafe_allow_html=True)
    st.camera_input("Scan", key="cam", label_visibility="collapsed")
    st.text_input("Token", type="password")

with c_right:
    st.markdown(f'<div style="background:white; border-radius:10px; padding:10px; border:2px solid gold;"><b style="color:black; font-size:20px;">{t["assets"]}</b></div>', unsafe_allow_html=True)
    st.button(t["car"], use_container_width=True)
    st.button(t["home"], use_container_width=True)

st.divider()

# 12-16. صوني وإبرام الصفقة
col_deal, col_prod = st.columns([2, 1])
with col_deal:
    st.subheader(t["sony"])
    st.text_area("...", placeholder="Write commands...", label_visibility="collapsed")
    if st.button(t["deal"], type="primary", use_container_width=True):
        st.balloons()
        st.success("Transaction Confirmed!")

with col_prod:
    # 15. المنتج الثابت
    st.markdown('<div style="border:2px solid #00ffcc; padding:15px; text-align:center; border-radius:15px;"><h4>سماعات كوفيه ستار</h4><h2>99.99 $</h2><div style="font-size:60px;">🎧</div></div>', unsafe_allow_html=True)

st.chat_input(f"Sony Agent: {st.session_state.lang} Active...")
