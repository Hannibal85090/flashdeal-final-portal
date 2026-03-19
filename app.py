import streamlit as st
from streamlit_option_menu import option_menu

# Page Config
st.set_page_config(page_title="FlashDeal - Innovation Portal", layout="wide")

# Custom CSS for Professional Look
st.markdown(""" <style> .main { background-color: #f5f7f9; } </style> """, unsafe_allow_html=True)

# 🌍 Navigation Menu (English & Arabic)
selected = option_menu(
    menu_title="FlashDeal Evolution Hub",
    options=["Overview | نظرة عامة", "Transaction & Transparency | الصفقات والشفافية", "Global Communication | التواصل العالمي"],
    icons=["info-circle", "shield-check", "translate"],
    orientation="horizontal",
    styles={
        "nav-link-selected": {"background-color": "#1f77b4"},
    }
)

# --- Tab 1: Overview ---
if "Overview" in selected:
    st.header("📖 Development Journey | قصة التطور المنهجي")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Our Philosophy")
        st.write("Bridging the gap between financial complexity and human interaction through AI.")
    with col2:
        st.subheader("رؤيتنا")
        st.write("سد الفجوة بين التعقيد المالي والتفاعل البشري عبر الذكاء الاصطناعي.")
    
    st.info("💡 **Note for Judges:** This portal demonstrates modular features to ensure high performance and stability.")

# --- Tab 2: Transaction & Transparency ---
elif "Transaction" in selected:
    st.header("💎 Transaction Core & Transparency | جوهر الصفقات والشفافية")
    st.success("Focus: Secure financial cycles and visual data tracking.")
    
    st.link_button("🚀 Enter Live Demo (Transaction Version)", "ضع_رابط_واجهة_الصفقات_هنا")
    
    st.markdown("---")
    st.write("**Key Features:** 1. Real-time Smart Contracts | 2. Motion-based Approval.")

# --- Tab 3: Global Communication ---
elif "Communication" in selected:
    st.header("🌍 Global Communication & NLP | التواصل العالمي واللغات")
    st.warning("Focus: Real-time contract translation and multilingual support.")
    
    st.link_button("📢 Enter Live Demo (Multilingual Version)", "ضع_رابط_واجهة_الترجمة_هنا")
