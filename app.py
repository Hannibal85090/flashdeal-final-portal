import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import cv2
import mediapipe as mp
import time

# --- ١. إعدادات استباقية (الارتقاء بالواجهة) ---
st.set_page_config(page_title="FlashDeal Master Portal", page_icon="⚡", layout="wide")

# إعدادات MediaPipe للتعرف على اليد (Gestures)
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# --- ٢. التخزين المؤقت لسرعة الإنجاز (Caching) ---
@st.cache_data
def load_full_data():
    return pd.DataFrame({
        "كود": ["FD-101", "FD-102", "FD-103", "FD-104"],
        "المشروع": ["Alpha Tech", "Smart City", "FinCore", "Green Energy"],
        "القيمة": [45000, 150000, 30000, 85000],
        "الحالة": ["مكتملة", "قيد المعالجة", "في الانتظار", "قيد المعالجة"]
    })

# --- ٣. القائمة التفاعلية العلوية (Horizontal Navigation) ---
selected = option_menu(
    menu_title=None,
    options=["الرؤية", "الصفقات الذكية", "الذكاء الاصطناعي", "التحليلات"],
    icons=["eye", "cash-stack", "camera-video", "graph-up"],
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#f8f9fa"},
        "nav-link-selected": {"background-color": "#007bff", "color": "white"},
    }
)

# --- ٤. تأثيث الأقسام (الدقة والتدقيق) ---

# أ- قسم الرؤية (The Vision)
if selected == "الرؤية":
    st.markdown("## 🌐 FlashDeal Strategic Vision")
    col1, col2 = st.columns(2)
    with col1:
        st.info("### 🎯 رؤيتنا العربية\nبناء جسور من الثقة والشفافية في عالم الصفقات الرقمية بنسبة استقرار 100%.")
    with col2:
        st.success("### 🚀 Global Vision\nEmpowering digital deals through AI and 100% transparency.")
    st.image("https://img.icons8.com/bubbles/200/business-group.png")

# ب- قسم الصفقات التفاعلي (Interactive Deals)
elif selected == "الصفقات الذكية":
    st.markdown("## 💰 بوابة الصفقات الذكية")
    df = load_full_data()
    status_filter = st.selectbox("تصفية حسب الحالة:", ["الكل"] + list(df["الحالة"].unique()))
    
    final_df = df if status_filter == "الكل" else df[df["الحالة"] == status_filter]
    st.table(final_df) # جدول كلاسيكي منظم بدقة
    
    if st.button("تأكيد النزاهة المالية"):
        st.balloons()
        st.success("تم التحقق من جميع الأرصدة والصفقات.")

# ج- قسم الذكاء الاصطناعي (Gestures & Camera)
elif selected == "الذكاء الاصطناعي":
    st.markdown("## 📷 التعرف على الإيماءات (Gesture Control)")
    st.write("استخدم يدك أمام الكاميرا للتفاعل مع النظام.")
    
    run_cam = st.checkbox("تشغيل الكاميرا التفاعلية")
    FRAME_WINDOW = st.image([]) # نافذة عرض الكاميرا
    camera = cv2.VideoCapture(0)

    while run_cam:
        ret, frame = camera.read()
        if not ret: break
        
        # تحويل الألوان لـ RGB لـ MediaPipe
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(frame_rgb)
        
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                st.toast("تم اكتشاف حركة يد!") # تفاعل فوري عند الحركة
        
        FRAME_WINDOW.image(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    else:
        st.warning("الكاميرا متوقفة حالياً.")

# د- قسم التحليلات (Future Analytics)
elif selected == "التحليلات":
    st.markdown("## 📊 Analytics Dashboard")
    df = load_full_data()
    st.bar_chart(df.set_index("المشروع")["القيمة"])
    st.metric("إجمالي قيمة الصفقات", f"${df['القيمة'].sum():,}", "+12%")

st.divider()
st.caption("FlashDeal Portal v2.0 | 2026 | All Rights Reserved")
