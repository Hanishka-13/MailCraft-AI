import streamlit as st
import json
from pathlib import Path
SAVE_FILE="saved_login.json"
def save_login(email,password):
    data={
        "email":email,
        "password":password
    }
    with open(SAVE_FILE, "w") as f:
        json.dump(data,f)
def load_login():
    if Path(SAVE_FILE).exists():
        with open(SAVE_FILE,"r") as f:
            return json.load(f)
    return {}
def login():
    saved=load_login()
    default_email=saved.get("email","")
    default_password=saved.get("password","")
    email=st.text_input(
        "Enter Your Gmail",
        value=default_email,
        placeholder="example@gmail.com"
    )
    password=st.text_input(
        "App Password",
        type="password",
        value=default_password,
        placeholder="xxxx xxxx xxxx xxxx"
    )
    remember=st.checkbox(
        "Remember Password",
        value=bool(default_password)
    )
    connect=st.button(
        "Connect Gmail",
        use_container_width=True
    )
    if connect:
        if not email.strip():
            st.error("Enter Gmail")
            return
        if not password.strip():
            st.error("Enter Password")
            return
        if remember:
            save_login(email,password)
        st.session_state.email=email
        st.session_state.password=password
        st.session_state.logged=True
        st.switch_page("pages/compose.py")