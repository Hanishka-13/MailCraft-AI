import streamlit as st
from smart_email_generator import (
    generate_email,
    extract_placeholders,
    fill_placeholders
)
from services.attachment_handler import prepare_attachments
from utils.styles import load_css
# PAGE CONFIG
st.set_page_config(
    page_title="MAILCRAFT AI",
    page_icon="📧",
    layout="wide"
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
# SESSION CHECK
if not st.session_state.get("logged",False):
    st.switch_page("app.py")
    st.stop()
# TOP RIGHT LOGOUT
top1,top2=st.columns([12,1])
with top2:
    if st.button("Logout"):
        st.session_state.clear()
        st.switch_page("app.py")
# HEADER
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
st.write("")
# MAIN LAYOUT
left,right=st.columns([2.3,1])
# LEFT SIDE
with left:
    purpose=st.text_area(
        "Purpose",
        height=330,
        placeholder=
        """Example:
        Write internship request mail
        Request leave
        Meeting invitation
        Follow up email
        """)
    generate=st.button("Generate Email",use_container_width=True)
# RIGHT SIDE
with right:
    tone=st.selectbox(
        "Email Tone",
        [
            "Professional",
            "Friendly",
            "Formal",
            "Casual"
        ]
    )
    uploaded=st.file_uploader(
        "Attachments",
        accept_multiple_files=True
    )
# GENERATE EMAIL
if generate:
    if purpose.strip()=="":
        st.error("Enter Purpose")
    else:
        result=generate_email(purpose,tone)
        st.session_state.subject=result["subject"]
        st.session_state.body=result["body"]
        if uploaded:
            st.session_state.attachments=prepare_attachments(uploaded)
# GENERATED EMAIL
if "body" in st.session_state:
    st.divider()
    st.subheader(st.session_state.subject)
    edited=st.text_area("Generated Email",value=st.session_state.body,height=350)
    placeholders=extract_placeholders(edited)
    values={}
    for p in placeholders:
        values[p]=st.text_input(p)
    edited=fill_placeholders(edited,values)
    st.session_state.body=edited
    if st.button("Confirm Email",use_container_width=True):
        st.switch_page("pages/receiver.py")