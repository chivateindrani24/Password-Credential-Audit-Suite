# app.py

import streamlit as st
import hashlib
import math
import re
import pandas as pd
from datetime import datetime

st.set_page_config(
    page_title="Password Credential Audit Suite",
    page_icon="🔐",
    layout="wide"
)

# ---------------------------
# Utility Functions
# ---------------------------

def calculate_entropy(password):
    charset = 0

    if re.search(r"[a-z]", password):
        charset += 26

    if re.search(r"[A-Z]", password):
        charset += 26

    if re.search(r"[0-9]", password):
        charset += 10

    if re.search(r"[^a-zA-Z0-9]", password):
        charset += 32

    if charset == 0:
        return 0

    entropy = len(password) * math.log2(charset)
    return round(entropy, 2)


def analyze_password(password):

    score = 0
    remarks = []

    if len(password) >= 12:
        score += 2
        remarks.append("Good password length")
    else:
        remarks.append("Use at least 12 characters")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        remarks.append("Add uppercase letters")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        remarks.append("Add lowercase letters")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        remarks.append("Add numbers")

    if re.search(r"[^a-zA-Z0-9]", password):
        score += 1
    else:
        remarks.append("Add special characters")

    common_passwords = [
        "password",
        "admin",
        "admin123",
        "123456",
        "welcome",
        "qwerty"
    ]

    if password.lower() in common_passwords:
        remarks.append("Common password detected")

    entropy = calculate_entropy(password)

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return strength, score, entropy, remarks


def identify_hash(hash_value):

    length = len(hash_value)

    if length == 32:
        return "Possible MD5"

    elif length == 40:
        return "Possible SHA1"

    elif length == 64:
        return "Possible SHA256"

    elif length == 128:
        return "Possible SHA512"

    return "Unknown Hash"


def generate_dictionary(name, year):

    words = set()

    base = name.strip()

    if not base:
        return []

    words.add(base.lower())
    words.add(base.capitalize())

    if year:
        words.add(f"{base}{year}")
        words.add(f"{base}@{year}")
        words.add(f"{base}123")
        words.add(f"{base}!123")

    words.add(base.replace("a", "@"))
    words.add(base.replace("i", "1"))
    words.add(base.replace("e", "3"))

    return sorted(words)


# ---------------------------
# Header
# ---------------------------

st.title("🔐 Password Credential Audit Suite")
st.markdown(
    "Educational cybersecurity project for password security assessment."
)

# ---------------------------
# Sidebar
# ---------------------------

module = st.sidebar.selectbox(
    "Select Module",
    [
        "Dashboard",
        "Password Strength Analyzer",
        "Dictionary Generator",
        "Hash Identifier",
        "Password Policy Checker",
        "Audit Report"
    ]
)

# ---------------------------
# Dashboard
# ---------------------------

if module == "Dashboard":

    st.subheader("Project Overview")

    st.info(
        """
        Modules Included:
        • Password Strength Analyzer
        • Dictionary Generator
        • Hash Identifier
        • Password Policy Checker
        • Audit Reporting
        """
    )

    st.success("Educational & Defensive Security Tool")

# ---------------------------
# Password Analyzer
# ---------------------------

elif module == "Password Strength Analyzer":

    st.subheader("Password Strength Analyzer")

    password = st.text_input(
        "Enter Password",
        type="password"
    )

    if st.button("Analyze Password"):

        strength, score, entropy, remarks = analyze_password(password)

        st.metric("Strength", strength)
        st.metric("Score", f"{score}/6")
        st.metric("Entropy", entropy)

        st.write("### Recommendations")

        for item in remarks:
            st.write(f"• {item}")

# ---------------------------
# Dictionary Generator
# ---------------------------

elif module == "Dictionary Generator":

    st.subheader("Dictionary Generator")

    name = st.text_input("Name")

    year = st.text_input("Year")

    if st.button("Generate Dictionary"):

        words = generate_dictionary(name, year)

        st.write("Generated Words")

        for word in words:
            st.code(word)

        st.download_button(
            label="Download Wordlist",
            data="\n".join(words),
            file_name="wordlist.txt",
            mime="text/plain"
        )

# ---------------------------
# Hash Identifier
# ---------------------------

elif module == "Hash Identifier":

    st.subheader("Hash Identifier")

    hash_value = st.text_input("Enter Hash")

    if st.button("Identify"):

        result = identify_hash(hash_value)

        st.success(result)

# ---------------------------
# Password Policy Checker
# ---------------------------

elif module == "Password Policy Checker":

    st.subheader("Password Policy Checker")

    password = st.text_input(
        "Password to Check",
        type="password"
    )

    if st.button("Check Policy"):

        checks = {
            "Minimum Length 12":
                len(password) >= 12,

            "Uppercase Letter":
                bool(re.search(r"[A-Z]", password)),

            "Lowercase Letter":
                bool(re.search(r"[a-z]", password)),

            "Number":
                bool(re.search(r"[0-9]", password)),

            "Special Character":
                bool(re.search(r"[^a-zA-Z0-9]", password))
        }

        df = pd.DataFrame(
            checks.items(),
            columns=["Requirement", "Passed"]
        )

        st.dataframe(df)

# ---------------------------
# Audit Report
# ---------------------------

elif module == "Audit Report":

    st.subheader("Password Audit Report")

    password = st.text_input(
        "Enter Password",
        type="password"
    )

    if st.button("Generate Report"):

        strength, score, entropy, remarks = analyze_password(password)

        report = pd.DataFrame({
            "Metric": [
                "Strength",
                "Score",
                "Entropy",
                "Generated On"
            ],
            "Value": [
                strength,
                score,
                entropy,
                datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ]
        })

        st.dataframe(report)

        st.write("### Security Recommendations")

        for item in remarks:
            st.write(f"• {item}")

        csv = report.to_csv(index=False)

        st.download_button(
            "Download Report",
            csv,
            "audit_report.csv",
            "text/csv"
        )

st.sidebar.markdown("---")
st.sidebar.caption(
    "Password Credential Audit Suite v1.0"
)
import streamlit as st

st.title("Password Credential Audit Suite")

password = st.text_input("Enter Password", type="password")

if st.button("Analyze"):
    score = len(password)
    st.write(f"Password Length: {score}")
