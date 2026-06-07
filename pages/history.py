import streamlit as st
import json
import os
from utils.styles import load_css
st.set_page_config(
    page_title="History",
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
    Email History
    </div>
    """,
unsafe_allow_html=True
)
history_file="data/history.json"
if not os.path.exists(history_file):
    history=[]
else:
    with open(history_file,"r",encoding="utf-8") as f:
        try:
            history=json.load(f)
        except:
            history=[]
if len(history)==0:
    st.info("No Emails Sent Yet")
else:
    history.reverse()
    for item in history:
        with st.container():
            st.markdown(
                f"""
                ### {item['subject']}
                **To:** {item['receiver']}
                **Time:** {item['time']}
                """)
            st.text(item["body"][:250])
            st.divider()