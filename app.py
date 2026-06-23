import streamlit as st
import webbrowser

# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(
    page_title="KrishiMitra 🌾",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- TITLE ---------------- #
st.title("🌾 KrishiMitra - Intelligent Agricultural Assistant")
st.markdown("### 🚀 AI-based Crop, Fertilizer & Disease Prediction System")

# ---------------- SIDEBAR ---------------- #
st.sidebar.title("📌 Navigation")

page = st.sidebar.radio(
    "Choose a Module",
    [
        "🏠 Home",
        "🌾 Crop Recommendation",
        "🌱 Fertilizer Recommendation",
        "🦠 Crop Disease Detection",
        "📜 Government Schemes"   # 👈 ADDED
    ]
)

# ---------------- HOME PAGE ---------------- #
if page == "🏠 Home":
    st.subheader("Welcome to KrishiMitra 🌿")

    st.write("""
    This intelligent system helps farmers and users make better agricultural decisions using Machine Learning & Deep Learning.

    ### 🔍 Features:
    🌾 Crop Recommendation → Suggest best crop based on soil & weather  
    🌱 Fertilizer Recommendation → Suggest best fertilizer  
    🦠 Disease Detection → Detect crop disease from leaf image  

    ### 🎯 How to Use:
    1. Select a module from sidebar  
    2. Enter required inputs / upload image  
    3. Get instant AI prediction  
    """)

    st.info("💡 Tip: Provide accurate inputs for better results")

# ---------------- CROP PAGE ---------------- #
elif page == "🌾 Crop Recommendation":
    import Crop_Page
    Crop_Page.app()

# ---------------- FERTILIZER PAGE ---------------- #
elif page == "🌱 Fertilizer Recommendation":
    import Fertilizer_Page
    Fertilizer_Page.app()

# ---------------- DISEASE PAGE ---------------- #
elif page == "🦠 Crop Disease Detection":
    import Crop_Disease_Page
    Crop_Disease_Page.app()

# ---------------- SCHEMES PAGE ---------------- #
elif page == "📜 Government Schemes":

    st.subheader("🌱 Government Schemes for Farmers")

    st.markdown("""
    ### Government of India provides many beneficial schemes for farmers:

    - PM-KISAN (Income support)
    - Pradhan Mantri Fasal Bima Yojana (Crop Insurance)
    - Soil Health Card Scheme
    - Kisan Credit Card (KCC)
    - PM Krishi Sinchai Yojana

    These schemes help improve productivity, income and risk management.
    """)

    st.success("✅ Click below to explore all schemes")

    # Button → redirect
    if st.button("🌐 View Government Schemes"):
        webbrowser.open_new_tab("https://www.myscheme.gov.in/search/category/Agriculture,Rural%20%26%20Environment")

# ---------------- FOOTER ---------------- #
st.sidebar.markdown("---")
st.sidebar.write("""👨‍💻 Developed by Yash Maheshwari s""")