import streamlit as st
from streamlit_option_menu import option_menu

# --- 1. إعدادات الصفحة (Mobile Responsive) ---
st.set_page_config(
    page_title="FlashDeal Master Portal",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="collapsed" # أفضل للهاتف لتقليل الزحام
)

# --- 2. نظام التخزين المؤقت (Performance Boost) ---
@st.cache_data
def load_vision_data():
    return {
        "title": "FlashDeal Master Portal",
        "vision_ar": "بناء جسور من الثقة والشفافية في عالم الصفقات الرقمية بنسبة استقرار 100%.",
        "vision_en": "Building bridges of trust and transparency in the digital deals world with 100% stability."
    }

# --- 3. القائمة الجانبية (Navigation) ---
with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options=["Overview", "Deals", "Global", "Analytics"],
        icons=["house", "currency-dollar", "globe", "graph-up"],
        menu_icon="cast",
        default_index=0,
    )

# --- 4. محتوى الأقسام ---
data = load_vision_data()

if selected == "Overview":
    st.title(f"🌐 {data['title']}")
    
    # تنسيق البطاقات (Cards) بدلاً من النصوص العادية لجمالية الهاتف
    st.info("### 🎯 الرؤية الاستراتيجية | Strategic Vision")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"**بالعربية:**\n\n{data['vision_ar']}")
    with col2:
        st.markdown(f"**English:**\n\n{data['vision_en']}")
    
    st.divider()
    st.success("✅ النظام يعمل الآن بكفاءة عالية وفق المعايير العالمية.")

elif selected == "Deals":
    st.header("💰 قسم الصفقات الذكية")
    st.write("هنا سيتم عرض جدول الصفقات التفاعلي في التحديث القادم.")
    # (سنضيف كود الجداول لاحقاً هنا)

# (باقي الأقسام تتبع نفس النمط...)
