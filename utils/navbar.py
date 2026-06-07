import streamlit as st
def navbar():
    c1,c2,c3,c4=st.columns([2,2,2,1])
    with c1:
        if st.button("Compose",use_container_width=True):
            st.switch_page("pages/compose.py")
    with c2:
        if st.button("History",use_container_width=True):
            st.switch_page("pages/history.py")
    with c3:
        if st.button("Settings",use_container_width=True):
            st.switch_page("pages/settings.py")
    with c4:
        if st.button("Logout"):
            st.session_state.clear()
            st.switch_page("app.py")