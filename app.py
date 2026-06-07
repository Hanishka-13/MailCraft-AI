import streamlit as st
from pages import compose
from utils.styles import load_css
from utils.auth import login
st.set_page_config(
    page_title="MAILCRAFT AI",
    page_icon="📧",
    layout="wide",
    initial_sidebar_state="collapsed"
)
st.markdown(
    load_css(),
    unsafe_allow_html=True
)
with st.sidebar:
    st.page_link("app.py",label="🏠 Home")
    st.page_link("pages/compose.py",label="✉ Compose")
    st.page_link("pages/history.py",label="🕒 History")
    st.page_link("pages/receiver.py",label="📨 Receiver")
    st.page_link("pages/settings.py",label="⚙ Settings")
if st.session_state.get("logged",False):
    st.switch_page("pages/compose.py")

# TITLE
st.markdown(
    """
    <div class="topbar">
    <div class="logo">
    📧
    </div>
        <div class="brand">
        MAILCRAFT AI
        </div>
    </div>
    <div class="subtitle">
    AI Powered Professional Email Assistant
    </div>
    """,
unsafe_allow_html=True
)

# LOGIN SECTION
left,center,right=st.columns([1,1.15,1])
with center:
    login()

# STEPS BOX
left,center,right=st.columns([1,1.3,1])
with center:
    st.markdown(
        """
        <div class="steps">
        <h2>How To Create Gmail App Password</h2>
        <div class="step-text">
        <p>
        <b>1.Open your Google Account settings
        </p>
        <p>
        <b>2.Go to Security section
        </p>
        <p>
        <b>3.Enable Two Step Verification
        </p>
        <p>
        <b>4.Open App Passwords
        </p>
        <p>
        <b>5.Generate password for Mail
        </p>
        <p>
        <b>6.Copy password and paste above
        </p>
        </div>
        </div>
        """,
unsafe_allow_html=True
)