import streamlit as st
import time

# --- إعدادات الصفحة الأساسية ---
st.set_page_config(page_title="My FlashDeal Star", page_icon="🌟", layout="wide")

# تخصيص المظهر بالكامل (الخلفية الزرقاء الداكنة وتنسيق النجوم)
st.markdown("""
<style>
    /* الخلفية الزرقاء الداكنة (من الصورة 2) */
    .stApp {
        background-color: #001a33;
        background-image: linear-gradient(180deg, #001a33 0%, #003366 100%);
        color: white;
    }
    /* تنسيق العنوان الرئيسي والنجوم الملتصقة (النقطة 1، 2) */
    .header-container { text-align: center; margin-bottom: 0px; }
    .main-title { color: white; font-size: 50px; font-weight: bold; display: inline-block; vertical-align: middle; }
    .star-side { color: gold; font-size: 45px; vertical-align: middle; margin: 0 10px; }
    
    /* النجمة الثالثة الكبرى تحت العنوان (النقطة 3) */
    .center-star { text-align: center; color: gold; font-size: 80px; margin-top: -20px; text-shadow: 0 0 20px gold; }
    
    /* الشعار بخلفية بيضاء (النقطة 4) */
    .motto-box {
        background-color: white; color: black; font-weight: bold; padding: 10px 30px;
        border-radius: 10px; border: 2px solid gold; width: fit-content; margin: 0 auto; font-size: 24px;
    }
    
    /* التوقيت بلون سيان (النقطة 5) */
    .time-display { text-align: center; color: #00ffff; font-family: monospace; font-size: 18px; margin-top: 10px; }

    /* تنسيق الحاويات (سادن والتحكم) */
    .content-box { background: white; color: black; padding: 15px; border-radius: 10px; border: 2px solid gold; margin-bottom: 10px; }
    .box-title { font-weight: bold; font-size: 20px; border-bottom: 2px solid black; margin-bottom: 10px; }
</style>
""", unsafe_allow_html=True)

# --- الجانب الأيسر (المنيو) ---
with st.sidebar:
    st.markdown("### 🌐 Languages / اللغات")
    lang = st.selectbox("", ["Arabic", "English", "Italiano", "Français"], label_visibility="collapsed")
    
    st.markdown("### 🔑 System Access")
    access = st.radio("", ["Standard", "Master Alpha 🔓"], label_visibility="collapsed")
    if access == "Master Alpha 🔓":
        st.success("Master Alpha: Active")
    
    st.markdown("### 📜 سجل الذاكرة / Memory Log")
    if 'history' not in st.session_state: st.session_state.history = ["[12:54:00] System Ready"]
    for entry in reversed(st.session_state.history): st.write(entry)

# --- 1-5: رأس الصفحة (العنوان، النجوم، الشعار، الوقت) ---
st.markdown('<div class="header-container"><span class="star-side">✨</span><div class="main-title">My FlashDeal Star</div><span class="star-side">✨</span></div>', unsafe_allow_html=True)
st.markdown('<div class="center-star">★</div>', unsafe_allow_html=True)
st.markdown('<div class="motto-box">. تكلم ، ادفع ، تم .</div>', unsafe_allow_html=True)
st.markdown(f'<div class="time-display">{time.strftime("24/03/2026 - %H:%M:%S")}</div>', unsafe_allow_html=True)

st.divider()

# --- 6: الأزرار الخماسية ---
c1, c2, c3, c4, c5 = st.columns(5)
with c1: st.button("👤 Face ID", use_container_width=True)
with c2: st.button("🔑 Key", use_container_width=True)
with c3: st.button("✋ Hand", use_container_width=True)
with c4: st.button("🔒 Lock", use_container_width=True)
with c5: st.button("💎 Jewel", use_container_width=True)

st.divider()

# --- 7-11: سادن والتحكم والكاميرا ---
col_left, col_right = st.columns(2)

with col_left:
    st.markdown('<div class="content-box"><div class="box-title">🛡️ أمان سادن</div></div>', unsafe_allow_html=True)
    st.camera_input("Take Photo", key="cam")
    st.text_input("Token ID (Saden)", type="password")
    st.text_input("Mutual Token 👁️", type="password")

with col_right:
    st.markdown('<div class="content-box"><div class="box-title">🏠 التحكم في الأصول</div></div>', unsafe_allow_html=True)
    st.button("🚗 Start Engine", use_container_width=True)
    st.button("🏠 Home Security", use_container_width=True)
    st.info("نظام التحكم في الأصول جاهز")

st.divider()

# --- 12-16: الوكيل والمنتج والشهادة ---
bot_l, bot_r = st.columns([2, 1])

with bot_l:
    st.markdown("### 🤝 Sony Agent")
    context = st.text_area("وصف الصفقة / Deal Description:", placeholder="e.g. Buying materials...")
    if st.button("إبرام الصفقة 🤝", type="primary", use_container_width=True):
        st.balloons()
        st.success("Deal Executed Successfully! ✅")
        # 14: إصدار الشهادة
        st.markdown(f"""
        <div style="border: 4px double gold; padding: 20px; background: rgba(0,0,0,0.5); text-align: center;">
            <h2>📜 شهادة إتمام الصفقة</h2>
            <p>تم التوثيق بواسطة نظام <b>Master Alpha</b></p>
            <p>التوقيت: {time.strftime('%H:%M:%S')}</p>
        </div>
        """, unsafe_allow_html=True)
        st.session_state.history.append(f"[{time.strftime('%H:%M:%S')}] - Deal Finalized")

with bot_r:
    # 15: السماعات والثمن في مربع معقول
    st.markdown(f"""
    <div style="border: 2px solid #00ffcc; border-radius: 15px; padding: 15px; text-align: center; background: rgba(255,255,255,0.1);">
        <h4 style="color: #00ffcc;">سماعات كوفيه ستار</h4>
        <h3 style="color: white;">99.99 $</h3>
        <div style="font-size: 50px;">🎧</div>
        <small style="color: #ccc;">Innovation Team Edition 2026</small>
    </div>
    """, unsafe_allow_html=True)

# 16: خانة التفاعل مع صوني في الأسفل
st.chat_input("...أنا في انتظار أوامرك غداً :Sony-Agent")
