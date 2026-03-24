import streamlit as st
import time

# --- 1. إعدادات المنصة السيادية ---
st.set_page_config(page_title="FlashDeal Star | Alpha Edition", page_icon="🌟", layout="wide")

if 'history' not in st.session_state:
    st.session_state.history = []

def add_to_memory(action):
    timestamp = time.strftime("%H:%M:%S")
    st.session_state.history.append(f"[{timestamp}] - {action}")

# --- 2. الهندسة البصرية (خلفية الصنوبر والجماليات) ---
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #001a33 0%, #003366 100%);
    background-image: url("https://www.transparenttextures.com/patterns/pinetree.png");
    background-blend-mode: overlay;
}
.main-header {text-align:center; margin-top:-50px;}
.title-text {color:white; font-size:3.5rem; font-weight:bold; text-shadow:0 0 15px gold;}
.star-unit {color:gold; font-size:3rem; vertical-align:middle;}
.big-star {text-align:center; font-size:90px; color:gold; text-shadow:0 0 30px gold; margin:-15px 0;}
.motto-banner {text-align:center; color:#000; font-size:26px; font-weight:bold; background:#fff; border:3px solid gold; border-radius:15px; padding:10px 50px; width:fit-content; margin:10px auto;}
.clock-text {text-align:center; color:#00ffff; font-size:20px; font-weight:bold; font-family:monospace; margin-bottom:20px;}
.white-box {background:#fff; border-radius:15px; padding:20px; border:2px solid gold; margin-bottom:15px;}
.dark-label {color:#000 !important; font-weight:900; font-size:22px; margin-bottom:10px; border-bottom:2px solid #000;}
.cert-card {border:4px double gold; padding:20px; background:#000; color:gold; text-align:center; border-radius:15px; margin-top:15px;}
</style>
""", unsafe_allow_html=True)

# --- 3. القاموس اللغوي الشامل (النقاط 17) ---
LANG_DICT = {
    'Arabic': {'motto':"تكلم ، ادفع ، تم .", 'saden':"🛡️ أمان سادن", 'infra':"🏠 التحكم في الأصول", 'exec':"إبرام الصفقة 🚀", 'prod':"سماعات كوفيه ستار", 'price':"99.99 $"},
    'English': {'motto':"TALK , PAY , DONE .", 'saden':"🛡️ Saden Security", 'infra':"🏠 Asset Control", 'exec':"Execute Deal 🚀", 'prod':"Cuffie Star Headphones", 'price':"$99.99"},
    'Italiano': {'motto':"PARLA , PAGA , FATTO .", 'saden':"🛡️ Sicurezza Saden", 'infra':"🏠 Controllo Asset", 'exec':"Concludi Affare 🚀", 'prod':"Cuffie Star", 'price':"99.99 $"},
    'Français': {'motto':"PARLE , PAIE , TERMINÉ .", 'saden':"🛡️ Sécurité Saden", 'infra':"🏠 Contrôle d'Actifs", 'exec':"Conclure l'Accord 🚀", 'prod':"Casque Cuffie Star", 'price':"99.99 €"}
}

# --- 4. الشريط الجانبي (اللغات، الأنماط، الذاكرة) ---
with st.sidebar:
    st.markdown("### 🌐 Languages / اللغات")
    sel_lang = st.selectbox("", list(LANG_DICT.keys()), label_visibility="collapsed")
    L = LANG_DICT[sel_lang]
    
    st.divider()
    st.markdown("### 🔑 System Access")
    mode = st.radio("", ["Standard", "Master Alpha 🔓"], label_visibility="collapsed")
    if mode == "Master Alpha 🔓": st.success("Master Alpha: Active")
    
    st.divider()
    with st.expander("📜 سجل الذاكرة / Memory Log", expanded=True):
        for item in reversed(st.session_state.history): st.write(item)

# --- 5. الهيكل البصري الرئيسي (النقاط 1-5) ---
st.markdown(f'<div class="main-header"><span class="star-unit">✨</span><span class="title-text">My FlashDeal Star</span><span class="star-unit">✨</span></div>', unsafe_allow_html=True)
st.markdown('<div class="big-star">★</div>', unsafe_allow_html=True)
st.markdown(f'<div class="motto-banner">{L["motto"]}</div>', unsafe_allow_html=True)
st.markdown(f'<div class="clock-text">{time.strftime("%d/%M/%Y - %H:%M:%S")}</div>', unsafe_allow_html=True)

# --- 6. الأزرار الخماسية (النقاط 6) ---
c1, c2, c3, c4, c5 = st.columns(5)
with c1: st.button("👤 Face")
with c2: st.button("🔑 Key")
with c3: st.button("✋ Hand")
with c4: st.button("🔒 Lock")
with c5: st.button("💎 Jewel")

st.divider()

# --- 7. سادن والتحكم (النقاط 7-11) ---
col_saden, col_infra = st.columns(2)

with col_saden:
    st.markdown(f'<div class="white-box"><div class="dark-label">{L["saden"]}</div></div>', unsafe_allow_html=True)
    st.camera_input("Scan", key="cam", label_visibility="collapsed")
    st.text_input("Token ID", type="password", help="انقر على العين للإظهار")
    st.text_input("Mutual Token", type="password", help="التوكن المتبادل")

with col_infra:
    st.markdown(f'<div class="white-box"><div class="dark-label">{L["infra"]}</div></div>', unsafe_allow_html=True)
    st.button("🚗 Start Engine", use_container_width=True)
    st.button("🏠 Home Security", use_container_width=True)
    st.info("نظام التحكم في الأصول جاهز")

st.divider()

# --- 8. الوكيل صوني وإبرام الصفقة (النقاط 12-16) ---
col_agent, col_prod = st.columns([1.5, 1])

with col_agent:
    st.subheader("🤝 Sony Agent")
    # مستطيل التفاعل بالكتابة
    user_input = st.text_area("⌨️ اكتب أمرك أو تفاصيل الصفقة:", placeholder="Scrivi il tuo comando...")
    
    if st.button(f"🤝 {L['exec']}", type="primary", use_container_width=True):
        st.balloons()
        st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3", autoplay=True)
        add_to_memory(f"Deal: {user_input}")
        # إصدار الشهادة (النقطة 14)
        st.markdown(f"""
        <div class="cert-card">
            <h3>📜 CERTIFICATE OF COMPLETION</h3>
            <p>تم إتمام الصفقة بنجاح تحت إشراف Alpha Master</p>
            <p><b>{user_input if user_input else "Smart Transaction"}</b></p>
            <small>{time.strftime('%Y-%m-%d %H:%M')}</small>
        </div>
        """, unsafe_allow_html=True)

with col_prod:
    # سماعات الأذنين (النقطة 15)
    st.markdown(f"""
    <div style="border:2px solid gold; padding:20px; border-radius:15px; text-align:center; background:rgba(255,255,255,0.1);">
        <h4 style="color:#00ffcc;">🎧 {L['prod']}</h4>
        <h2 style="color:white;">{L['price']}</h2>
        <div style="font-size:60px;">🎧</div>
    </div>
    """, unsafe_allow_html=True)

# شريط التفاعل السفلي (صوني)
st.chat_input("Sony-Agent: أنا في انتظار أوامرك...")
