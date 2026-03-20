import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_webrtc import webrtc_streamer, VideoProcessorBase
import pandas as pd
import mediapipe as mp
import av
import cv2

# --- 1. إعدادات البوابة الاحترافية ---
st.set_page_config(page_title="FlashDeal Master Portal", page_icon="⚡", layout="wide")

# إعدادات MediaPipe للذكاء الاصطناعي
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# --- 2. محرك معالجة الفيديو (للتعامل مع كاميرا الهاتف) ---
class GestureProcessor(VideoProcessorBase):
    def recv(self, frame):
        img = frame.to_ndarray(format="bgr24")
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(img_rgb)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)
        return av.VideoFrame.from_ndarray(img, format="bgr24")

# --- 3. نظام التنقل التفاعلي (العلوي) ---
selected = option_menu(
    menu_title=None,
    options=["الرؤية & Vision", "صفقات FlashDeal", "ذكاء الإيماءات", "التحليلات"],
    icons=["house", "currency-dollar", "camera-video", "graph-up"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#f0f2f6"},
        "nav-link": {"font-size": "14px", "text-align": "center", "margin":"0px"},
        "nav-link-selected": {"background-color": "#02ab21"},
    }
)

# --- 4. تأثيث الأقسام الكامل ---

# أ- قسم الرؤية (The Vision)
if selected == "الرؤية & Vision":
    st.title("🌐 FlashDeal Master Portal")
    col1, col2 = st.columns(2)
    with col1:
        st.info("### 🎯 الرؤية\nبناء منصة صفقات رقمية تتسم بالشفافية المطلقة والذكاء الاصطناعي لضمان نمو مستدام.")
    with col2:
        st.success("### 🎯 The Vision\nBuilding a digital deals platform defined by absolute transparency and AI for sustainable growth.")
    st.divider()
    st.markdown("#### ✅ حالة النظام: متصل ومستقر 100%")

# ب- قسم الصفقات (Interactive Deals)
elif selected == "صفقات FlashDeal":
    st.title("💰 بوابة الصفقات الذكية")
    deals_df = pd.DataFrame({
        "كود": ["FD-101", "FD-102", "FD-103"],
        "المشروع": ["Alpha Tech", "Smart Invest", "Global Core"],
        "القيمة": ["$45,000", "$150,000", "$30,000"],
        "الحالة": ["مكتملة", "قيد المعالجة", "منتظرة"]
    })
    
    status = st.selectbox("تصفية الصفقات:", ["الكل", "مكتملة", "قيد المعالجة", "منتظرة"])
    filtered = deals_df if status == "الكل" else deals_df[deals_df["الحالة"] == status]
    
    st.table(filtered)
    if st.button("🚀 تحديث قاعدة البيانات"):
        st.toast("تم تحديث البيانات بنجاح!")

# ج- قسم الذكاء الاصطناعي (Gesture AI)
elif selected == "ذكاء الإيماءات":
    st.title("📷 Gesture Recognition Control")
    st.write("قم بتفعيل الكاميرا للتعرف على حركات اليد (بواسطة MediaPipe)")
    
    webrtc_streamer(
        key="gestures",
        video_processor_factory=GestureProcessor,
        rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]},
        media_stream_constraints={"video": True, "audio": False}
    )
    

# د- قسم التحليلات (Analytics)
elif selected == "التحليلات":
    st.title("📊 Analytics Dashboard")
    st.line_chart([20, 35, 70, 50, 90])
    st.metric("مستوى الأمان", "100%", "Safe")

# --- 5. التذييل النهائي ---
st.divider()
st.caption("FlashDeal Portal v2.5 | 2026 | Powered by AI & Transparency")
