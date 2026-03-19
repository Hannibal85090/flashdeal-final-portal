import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="FlashDeal Master Portal", layout="wide")

# تصميم القائمة العلوية
selected = option_menu(
    menu_title="FlashDeal: رحلة الابتكار وتدرج المزايا",
    options=["نظرة عامة", "جناح الصفقات والشفافية", "جناح التواصل واللغات"],
    icons=["info-circle", "gem", "translate"],
    orientation="horizontal",
)

if selected == "نظرة عامة":
    st.header("📖 قصة التطور (تدرج العمل)")
    st.write("مرحباً بكم في منصة العرض المنهجي. هنا نعرض المزايا بشكل منفصل لضمان استقرار الأداء التقني.")
    st.image("https://via.placeholder.com/800x400.png?text=FlashDeal+Evolution+Path") # يمكنك استبدال الرابط بصورة لمخطط مشروعك

elif selected == "جناح الصفقات والشفافية":
    st.header("💎 ميزة إبرام الصفقات والنزاهة الرقمية")
    st.info("في هذا الجناح، نركز على قوة النظام في إدارة العقود والشفافية.")
    st.link_button("🚀 دخول للواجهة الحية (نسخة الأداء المالي)", "ضع_هنا_رابط_الواجهة_التي_تعمل_بها_الصفقة")
    st.markdown("---")
    st.subheader("💡 ماذا يرى الحكام هنا؟")
    st.write("1. تسلسل مالي واضح. 2. وكيل ذكي يدعم الإشارة.")

elif selected == "جناح التواصل واللغات":
    st.header("🌍 ميزة الشمولية والتواصل العالمي")
    st.success("هنا نركز على قدرة النظام على ترجمة العقود والتحدث بلغة المستخدم.")
    st.link_button("📢 دخول للواجهة الحية (نسخة التواصل)", "ضع_هنا_رابط_الواجهة_التي_تعمل_بها_الترجمة")
    st.markdown("---")
    st.subheader("💡 ماذا يرى الحكام هنا؟")
    st.write("1. ترجمة فورية للعقود. 2. واجهة مستخدم متعددة اللغات.")
