import streamlit as st
import re

def check_password_strength(password):
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    special_char_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None
    
    errors = [length_error, digit_error, uppercase_error, lowercase_error, special_char_error]
    strength = 5 - sum(errors)

    if strength == 5:
        return "🟢 Strong", "green"
    elif strength >= 3:
        return "🟡 Moderate", "orange"
    else:
        return "🔴 Weak", "red"

st.title("🔐 Password Strength Meter")

password = st.text_input("Enter your password:", type="password")

if password:
    strength, color = check_password_strength(password)
    st.markdown(f"**Strength:** <span style='color:{color}; font-size:18px;'>{strength}</span>", unsafe_allow_html=True)
