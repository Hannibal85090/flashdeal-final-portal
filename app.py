import streamlit as st
from streamlit_option_menu import option_menu

# إعدادات الصفحة الاحترافية - تم التدقيق
st.set_page_config(
    page_title="FlashDeal Master Portal",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# القائمة العلوية - تم مطابقة الخيارات مع الأيقونات بدقة
selected = option_menu(
    menu_title="FlashDeal Innovation Hub 2026",
    options=["Overview | نظرة عامة", "Deals | الصفقات", "Global | العالمية"],
    icons=["info-circle", "shield-check", "translate"],
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#f0f2f6"},
        "icon": {"color": "#ff4b4b", "font-size": "18px"}, 
        "nav-link": {"font-size": "16px", "text-align": "center"},
        "nav-link-selected": {"background-color": "#1f77b4"},
    }
)

st.markdown("---")

# القسم الأول: نظرة عامة
if "Overview" in selected:
    st.header("📖 Evolution Journey | قصة التطور")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🇬🇧 The Vision")
        st.write("Bridging financial complexity and human-centric AI interaction.")
    with col2:
        st.subheader("🇸🇦 الرؤية")
        st.write("ربط التعقيد المالي بالتفاعل البشري المدعوم بالذكاء الاصطناعي.")
    st.info("💡 Modular design ensures 100% system stability and high performance.")

# القسم الثاني: جناح الصفقات (انسخ الرابط الحقيقي هنا)
elif "Deals" in selected:
    st.header("💎 Transaction & Transparency | الشفافية")
    st.success("Target: Secure and transparent financial cycles.")
    
    # تنبيه: استبدل الرابط أدناه برابط تطبيق الصفقات الخاص بك
    st.link_button("🚀 Launch Transaction Module | دخول لجناح الصفقات", "https://share.streamlit.io/HANNIBAL85090/...")
    
    st.markdown("---")
    st.write("**Key Focus:** Smart Contracts & Visual Auditing.")

# القسم الثالث: جناح العالمية (انسخ الرابط الحقيقي هنا)
elif "Global" in selected:
    st.header("🌍 Global Access & NLP | التواصل العالمي")
    st.warning("Target: Real-time multilingual contract processing.")
    
    # تنبيه: استبدل الرابط أدناه برابط تطبيق اللغات الخاص بك
    st.link_button("📢 Launch Language Module | دخول لجناح اللغات", "https://share.streamlit.io/HANNIBAL85090/...")
    
    st.markdown("---")
    st.write("**Key Focus:** Real-time Translation & Multi-language Support.")
