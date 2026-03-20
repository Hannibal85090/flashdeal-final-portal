import streamlit as st
try:
    from streamlit_option_menu import option_menu
    from streamlit_webrtc import webrtc_streamer, VideoProcessorBase
    import mediapipe as mp
    import av
    import cv2
    import pandas as pd
except ImportError as e:
    st.error(f"يرجى التأكد من تثبيت كافة المكتبات في requirements.txt. الخطأ: {e}")

# --- إعدادات الصفحة ---
st.set_page_config(page_title="My FlashDeal Star", page_icon="⭐", layout="wide")

# تعريف مكتبات الذكاء الاصطناعي
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

class GestureProcessor(VideoProcessorBase):
    def recv(self, frame):
        img = frame.to_ndarray(format="bgr24")
        results = hands.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)
        return av.VideoFrame.from_ndarray(img, format="bgr24")

# --- القائمة التفاعلية ---
selected = option_menu(
    menu_title=None,
    options=["الرؤية", "الصفقات", "AI الإيماءات"],
    icons=["house", "currency-dollar", "camera"],
    orientation="horizontal"
)

if selected == "الرؤية":
    st.title("⚡ ⭐ My FlashDeal Star")
    st.info("الرؤية: بناء منصة صفقات ذكية ومستقرة بنسبة 100%.")

elif selected == "الصفقات":
    st.subheader("Transparence: Prix et Valeur")
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=500", caption="Product Sample")
    with col2:
        st.metric("Price", "$99.99")
        st.button("Confirmer l'accord")

elif selected == "AI الإيماءات":
    st.write("قم بتشغيل الكاميرا للتفاعل مع النظام:")
    webrtc_streamer(
        key="key",
        video_processor_factory=GestureProcessor,
        rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
    )
