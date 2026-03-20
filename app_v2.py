import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd

# 1. إعدادات الصفحة لتناسب الهاتف (Mobile-Friendly)
st.set_page_config(page_title="FlashDeal Master Portal", layout="wide")

# 2. وظيفة التخزين المؤقت لتسريع الأداء (Performance Boost)
@st.cache_data
def load_base_data():
    return pd.DataFrame({"Deal": ["Alpha", "Beta"], "Value": ["$10k", "$50k"]})

# 3. القائمة العلوية الأنيقة
selected = option_menu(
    menu_title=None,
    options=["Vision", "Deals", "Intelligence", "Analytics"],
    icons=["eye", "cash-stack", "cpu", "graph-up"],
    orientation="horizontal",
    styles={"nav-link-selected": {"background-color": "#02ab21"}}
)

# 4. محتوى الرؤية (كما ظهر في نجاحك الأول)
if selected == "Vision":
    st.title("⚡ ⭐ FlashDeal Master Portal")
    st.success("### Strategic Vision | الرؤية الاستراتيجية")
    st.write("Building bridges of trust and transparency in the digital deals world with 100% stability.")
    st.balloons()

elif selected == "Deals":
    st.header("Active Transactions")
    st.table(load_base_data())

else:
    st.info("System is stable and ready for expansion.")
