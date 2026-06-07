import streamlit as st
from utils.styles import load_css
st.set_page_config(page_title="Settings",layout="wide")
st.markdown(load_css(),unsafe_allow_html=True)
with st.sidebar:
    st.page_link("app.py",label="🏠 Home")
    st.page_link("pages/compose.py",label="✉ Compose")
    st.page_link("pages/history.py",label="🕒 History")
    st.page_link("pages/receiver.py",label="📨 Receiver")
    st.page_link("pages/settings.py",label="⚙ Settings")
if not st.session_state.get("logged",False):
    st.switch_page("app.py")
st.markdown("""
    <div class="topbar">
    <div class="logo">
    📧
    </div>
    <div class="brand">
    MAILCRAFT AI
    </div>
    </div>
    <div class="subtitle">
    Settings
    </div>
    """,
unsafe_allow_html=True
)
st.subheader("Connected Account")
st.success(st.session_state.email)
if st.button("Clear Saved Password",use_container_width=True):
    if "password" in st.session_state:
        del st.session_state["password"]
    st.success("Password Removed")
if st.button("Logout",use_container_width=True):
    st.session_state.clear()
    st.switch_page("app.py")