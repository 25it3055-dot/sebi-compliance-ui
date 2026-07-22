import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Circular History",
    page_icon="📜",
    layout="wide"
)

st.title("📜 Circular History")

st.markdown("View previously analyzed SEBI circulars.")

st.divider()

# Search Box
search = st.text_input("🔍 Search Circular")

# Dummy Data
history = pd.DataFrame({
    "Circular ID": ["SEBI-001", "SEBI-002", "SEBI-003", "SEBI-004"],
    "Title": [
        "KYC Update",
        "Cyber Security",
        "Investor Protection",
        "AML Guidelines"
    ],
    "Risk": [
        "High",
        "Medium",
        "Low",
        "High"
    ],
    "Status": [
        "Completed",
        "Completed",
        "Pending",
        "Completed"
    ],
    "Upload Date": [
        "20 Jul 2026",
        "18 Jul 2026",
        "15 Jul 2026",
        "10 Jul 2026"
    ]
})

# Search Filter
if search:
    history = history[
        history["Title"].str.contains(search, case=False)
    ]

st.dataframe(history, use_container_width=True)

st.divider()

st.metric("Total Circulars", len(history))