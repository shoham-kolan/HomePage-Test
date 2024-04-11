import streamlit as st

st.header("My Contact")

with st.form(key="emailField"):
    userEmail = st.text_input("Your email address")
    message = st.text_area("Email Message")
    button = st.form_submit_button("Send")
    if button:
        None
