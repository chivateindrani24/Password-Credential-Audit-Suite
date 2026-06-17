import streamlit as st

st.title("Password Credential Audit Suite")

password = st.text_input("Enter Password", type="password")

if st.button("Analyze"):
    score = len(password)
    st.write(f"Password Length: {score}")
