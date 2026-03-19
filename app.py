import streamlit as st
from streamlit_option_menu import option_menu

# إعدادات واجهة العرض الكبرى
st.set_page_config(page_title="FlashDeal Master Portal", layout="wide")

# تصميم القائمة العلوية للتنقل بين الأبواب
selected = option_menu(
    menu_title="FlashDeal: رحلة الابتكار وتدرج المزايا",
    options=["نظرة عامة", "جناح الصفقات والشفافية", "جناح التواصل واللغات"],
    icons=["info-circle", "gem", "translate"],
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "25px"}, 
        "nav-link": {"font-size": "18px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#02ab21"},
    }
)

# --- الباب الأول: نظرة عامة ---
if selected == "نظرة عامة":
    st.header("📖 قصة التطور (تدرج العمل)")
    st.write("مرحباً بكم في منصة العرض المنهجي لـ FlashDeal. هنا نعرض تدرجنا من الفكرة إلى التنفيذ المتقدم.")
    
    st.info("💡 ملاحظة للحكام: تم توزيع الميزات في 'أجنحة' مستقلة لضمان استقرار الأداء التقني العالي لكل ميزة.")
    
    # هنا نضع فلسفة المشروع
    with st.expander("إظهار مبررات تدرج العمل"):
        st.write("""
        ١. بدأت الرحلة ببناء المحرك المالي الأساسي.
        ٢. تم تطوير الوكيل الذكي للتعامل مع الإيماءات.
        ٣. أضفنا طبقة الشمولية اللغوية لضمان وصول الخدمة للجميع.
        """)

# --- الباب الثاني: جناح الصفقات والشفافية ---
elif selected == "جناح الصفقات والشفافية":
    st.header("💎 ميزة إبرام الصفقات والنزاهة الرقمية")
    st.success("التركيز هنا: اكتمال الدورة المالية، الوكيل الذكي، والشفافية.")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.write("في هذه النسخة، يرى الحكام قدرة النظام على:")
        st.write("- إدارة العقود والصفقات المالية.")
        st.write("- توفير لوحة شفافية تتبع التدفق المالي.")
        # ملاحظة: ضع رابط تطبيقك الذي تكتمل فيه الصفقة أدناه
        st.link_button("🚀 دخول للواجهة الحية (نسخة الأداء المالي)", "https://share.streamlit.io/") 

# --- الباب الثالث: جناح التواصل واللغات ---
elif selected == "جناح التواصل واللغات":
    st.header("🌍 ميزة الشمولية والتواصل العالمي")
    st.warning("التركيز هنا: الترجمة الفورية للعقود، ودعم اللغات المتعددة.")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.write("هنا نبرهن على عالمية FlashDeal من خلال:")
        st.write("- ترجمة فورية لمحتوى الصفقات.")
        st.write("- واجهة مستخدم تتحدث لغة العميل.")
        # ملاحظة: ضع رابط تطبيقك الذي تبرز فيه الترجمة واللغات أدناه
        st.link_button("📢 دخول للواجهة الحية (نسخة التواصل العالمي)", "https://share.streamlit.io/")
