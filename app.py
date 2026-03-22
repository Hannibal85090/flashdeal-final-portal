import streamlit as st

st.header("💹 Transactions Portal")

# --- عرض السعر مع تقييم ---
col1, col2 = st.columns([1, 2])
with col1:
    st.metric("Price", "$99.99")
    st.metric("Token", "FD-62147-STAR")
with col2:
    st.write("Customer Rating:")
    # تقييم بالنجوم (أخضر = إيجابي، أحمر = سلبي)
    st.markdown(
        """
        <span style="color:green;">★ ★ ★ ★ ☆</span>  
        <span style="color:red;">★ ☆ ☆ ☆ ☆</span>
        """,
        unsafe_allow_html=True
    )

# --- زر تأكيد الصفقة ---
if st.button("Confirm Deal"):
    st.success("Deal confirmed successfully!")
    st.snow()

    # --- شهادة إبرام الصفقة ---
    st.subheader("📜 Deal Certificate")
    st.markdown(
        """
        **Certificate of Agreement**  
        Code: `FD-STAR-2026-AX91`  
        Status: ✅ Validated  
        Date: 22/03/2026
        """)
    st.balloons()
