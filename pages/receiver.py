import streamlit as st
from utils.email_sender import send_email
from utils.styles import load_css

# PAGE CONFIG
st.set_page_config(
    page_title="MAILCRAFT AI",
    page_icon="📧",
    layout="wide"
)
st.markdown(load_css(),unsafe_allow_html=True)
with st.sidebar:
    st.page_link("app.py",label="🏠 Home")
    st.page_link("pages/compose.py",label="✉ Compose")
    st.page_link("pages/history.py",label="🕒 History")
    st.page_link("pages/receiver.py",label="📨 Receiver")
    st.page_link("pages/settings.py",label="⚙ Settings")
# CHECK LOGIN
if not st.session_state.get("logged",False):
    st.switch_page("app.py")
    st.stop()
if "body" not in st.session_state:
    st.switch_page("pages/compose.py")
    st.stop()
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
    Send Generated Email
    </div>
    """,
unsafe_allow_html=True
)
# CENTER LAYOUT
left,center,right=st.columns([1,1.5,1])
with center:
    edited_subject=st.text_input("Subject",value=st.session_state.subject)
    edited_body=st.text_area(
        "Preview",
        value=st.session_state.body,
        height=320
    )
    receiver_count=st.number_input(
        "Number Of Receivers",
        min_value=1,
        max_value=20,
        value=1
    )
    receiver_list=[]
    for i in range(receiver_count):
        receiver=st.text_input(
            f"Receiver {i+1}",
            key=f"receiver_{i}"
        )
        if receiver.strip():
            receiver_list.append(receiver.strip())
    send=st.button("Send Email",use_container_width=True)
# SEND
if send:
    if len(receiver_list)==0:
        st.error("Enter Receiver Email")
        st.stop()
    attachments=[]
    if "attachments" in st.session_state:
        attachments=st.session_state.attachments
    success=True
    with st.spinner("Sending..."):
        for receiver in receiver_list:
            try:
                send_email(
                    receiver,
                    edited_subject,
                    edited_body,
                    attachments,
                    st.session_state.email,
                    st.session_state.password
                )
            except:
                success=False
    if success:
        st.success("Email Sent Successfully")
    else:
        st.error("Some Emails Failed")
# SMALL NEW MAIL BUTTON
left,center,right=st.columns([1,5,5])
with left:
    if st.button("← New Mail"):
        keys=[
            "subject",
            "body",
            "attachments"
        ]
        for key in keys:
            if key in st.session_state:
                del st.session_state[key]
        st.switch_page("pages/compose.py")