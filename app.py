import streamlit as st

# 1. إعدادات الصفحة لتناسب الهاتف (Mobile-Friendly)
st.set_page_config(page_title="FlashDeal Master Portal", layout="wide")

# 2. وظيفة التخزين المؤقت لتسريع الأداء (Performance Boost)
@st.cache_data
def get_vision_content():
    return {
        "ar": "رؤيتنا: بناء جسور من الثقة والشفافية في عالم الصفقات الرقمية.",
        "en": "Our Vision: Building bridges of trust and transparency in the digital deals world."
    }

# 3. واجهة الاستقبال (Overview Section)
def show_overview():
    st.title("🌐 FlashDeal Master Portal")
    
    content = get_vision_content()
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🎯 الرؤية الاستراتيجية")
        st.write(content["ar"])
        
    with col2:
        st.subheader("🎯 Strategic Vision")
        st.write(content["en"])
    
    st.divider()
    
    # زر إقناع تفاعلي (Call to Action)
    if st.button("🚀 انتقل إلى الصفقات الآن | Go to Deals Now"):
        st.balloons() # لمسة جمالية للإنجاز
        st.info("جاري تحويلك إلى قسم الصفقات الذكية...")

# استدعاء الواجهة
show_overview()
