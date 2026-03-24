import streamlit as st
import time

# --- [1. إعدادات النظام والبيانات] ---
st.set_page_config(page_title="FlashDeal Star", page_icon="⭐", layout="wide")

# قاموس اللغات (المحرك الديناميكي)
translations = {
    "Arabic": {
        "title": "My FlashDeal Star", "motto": ". تكلم ، ادفع ، تم .", "saden": "🛡️ أمان سادن",
        "assets": "🏠 التحكم في الأصول", "deal": "🤝 إبرام الصفقة", "sony": "🤝 الوكيل صوني",
        "car": "🚗 تشغيل السيارة", "home": "🏠 أمن المنزل", "token": "رمز التوكن",
        "mutual": "التوكن المتبادل 👁️", "cert": "📜 شهادة إتمام الصفقة", "master": "تم التوثيق بواسطة ماستر ألفا"
    },
    "English": {
        "title": "My FlashDeal Star", "motto": ". Speak , Pay , Done .", "saden": "🛡️ Saden Security",
        "assets": "🏠 Asset Control", "deal": "🤝 Finalize Deal", "sony": "🤝 Sony Agent",
        "car": "🚗 Start Car Engine", "home": "🏠 Home Security", "token": "Token ID",
        "mutual": "Mutual Token 👁️", "cert": "📜 Deal Certificate", "master": "Verified by Master Alpha"
    },
    "Italiano": {
        "title": "My FlashDeal Star", "motto": ". Parla , Paga , Fatto .", "saden": "🛡️ Sicurezza Saden",
        "assets": "🏠 Controllo Asset", "deal": "🤝 Concludi Affare", "sony": "🤝 Agente Sony",
        "car": "🚗 Avvia Motore", "home": "🏠 Sicurezza Casa", "token": "ID Token",
        "mutual": "Token Mutuo 👁️", "cert": "📜 Certificato Affare", "master": "Verificato da Master Alpha"
    },
    "Français": {
        "title": "My FlashDeal Star", "motto": ". Parle , Paye , Terminé .", "saden": "🛡️ Sécurité Saden",
        "assets": "🏠 Contrôle des Biens", "deal": "🤝 Conclure l'Accord", "sony": "🤝 Agent Sony",
        "car": "🚗 Démarrer Voiture", "home": "🏠 Sécurité Maison", "token": "ID Jeton",
        "mutual": "Jeton Mutuel 👁️", "cert": "📜 Certificat d'Accord", "master": "Vérifié par Master Alpha"
    }
}

# --- [2. الهندسة البصرية المصفاة] ---
st.markdown("""
<style>
    .stApp { background: linear-gradient(180deg, #001a33 0%, #003366 100%); color: white; }
    .header-box { text-align: center; margin-top: -60px; }
    .main-title { color: white; font-size: 50px; font-weight: bold; text-shadow: 0 0 20px #fff; display: inline-block; }
    .star-side { color: gold; font-size: 40px; margin: 0 15px; vertical-align: middle; }
    .star-mega { text-align: center; font-size: 80px; color: gold; text-shadow: 0 0 30px gold; margin-top: -25px; }
    .motto-bar { background: white; color: black; font-size: 24px; font-weight: bold; padding: 8px 40px; border-radius: 12px; border: 3px solid gold; width: fit-content; margin: 10px auto; }
    .info-card { background: white; border-radius: 12px; padding: 12px; border: 2px solid gold; margin-bottom: 10px; }
    .card-text { color: black !important; font-weight: 900; font-size: 20px; border-bottom: 2px solid #ccc; }
</style>
""", unsafe_allow_html=True)

# --- [3. الشريط الجانبي - التحكم باللغة والوصول] ---
with st.sidebar:
    st.markdown("### 🌐 Selection")
    lang = st.selectbox("Language", ["Arabic", "English", "Italiano", "Français"], key="L1")
    t = translations[lang] # جلب نصوص اللغة المختارة
    st.divider()
    access = st.radio("Access Mode", ["Standard", "Master Alpha 🔓"], key="A1")
    st.divider()
    with st.expander("📜 Memory Log"):
        st.write(f"[{time.strftime('%H:%M')}] System Active ({lang})")

# --- [4. العرض الرئيسي الديناميكي] ---
st.markdown(f'<div class="header-box"><span class="star-side">✨</span><div class="main-title">{t["title"]}</div><span class="star-side">✨</span><div class="star-mega">★</div></div>', unsafe_allow_html=True)
st.markdown(f'<div class="motto-bar">{t["motto"]}</div>', unsafe_allow_html=True)
st.markdown(f'<div style="text-align:center; color:#00ffff;">{time.strftime("%d/%m/%Y - %H:%M:%S")}</div>', unsafe_allow_html=True)

# 6. الأزرار الخماسية
c1, c2, c3, c4, c5 = st.columns(5)
with c1: st.button("👤 Face ID")
with c2: st.button("🔑 Key")
with c3: st.button("✋ Hand")
with c4: st.button("🔒 Lock")
with c5: st.button("💎 Jewel")

st.divider()

# 7-11. الأمان والأصول
col1, col2 = st.columns(2)
with col1:
    st.markdown(f'<div class="info-card"><div class="card-text">{t["saden"]}</div></div>', unsafe_allow_html=True)
    st.camera_input("Scan", key="C1", label_visibility="collapsed")
    st.text_input(t["token"], type="password", key="I1")
    st.text_input(t["mutual"], type="password", key="I2")

with col2:
    st.markdown(f'<div class="info-card"><div class="card-text">{t["assets"]}</div></div>', unsafe_allow_html=True)
    st.button(t["car"], use_container_width=True)
    st.button(t["home"], use_container_width=True)

st.divider()

# 12-16. صوني والصفقة
b1, b2 = st.columns([2, 1])
with b1:
    st.subheader(t["sony"])
    msg = st.text_area("Context:", key="M1")
    if st.button(t["deal"], type="primary", use_container_width=True):
        st.balloons()
        st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
        st.markdown(f'<div style="border:4px double gold; padding:15px; text-align:center; border-radius:10px;"><h3>{t["cert"]}</h3><p>{t["master"]}</p></div>', unsafe_allow_html=True)

with b2:
    # 15. المنتج
    st.markdown('<div style="border:2px solid #00ffcc; padding:15px; text-align:center; border-radius:15px;"><h4>سماعات كوفيه</h4><h2>99.99 $</h2><div style="font-size:50px;">🎧</div></div>', unsafe_allow_html=True)

st.chat_input(f"Sony Agent: {lang} mode active...")
