import streamlit as st
import pandas as pd
from components.sidebar import render_sidebar

# 1. Render Sidebar
render_sidebar()

# 2. Page Title & Description
st.title("📜 Compliance Audit History")
st.caption("Archive of all previously analyzed SEBI circulars, risk assessments, and compliance reports.")

st.markdown("---")

# 3. Search and Filters
col_search, col_risk, col_date = st.columns([2, 1, 1])

with col_search:
    search_query = st.text_input("🔍 Search History", placeholder="Search circular title or keyword...")

with col_risk:
    risk_filter = st.selectbox("Filter Risk", ["All Risks", "High Risk 🔴", "Medium Risk 🟡", "Low Risk 🟢"])

with col_date:
    sort_order = st.selectbox("Sort By", ["Newest First", "Oldest First"])

st.markdown("---")

# 4. Dummy History Data Setup
history_data = [
    {
        "Circular ID": "SEBI/HO/2026/012",
        "Title": "Revised Master Circular on KYC Verification Norms",
        "Date Analyzed": "21 Jul 2026",
        "Risk Rating": "High Risk 🔴",
        "Status": "Completed ✅"
    },
    {
        "Circular ID": "SEBI/HO/2026/009",
        "Title": "Guidelines on Anti-Money Laundering (AML) Standards",
        "Date Analyzed": "15 Jul 2026",
        "Risk Rating": "Medium Risk 🟡",
        "Status": "Completed ✅"
    },
    {
        "Circular ID": "SEBI/HO/2026/005",
        "Title": "Investor Protection & Dispute Resolution Mechanism",
        "Date Analyzed": "10 Jul 2026",
        "Risk Rating": "Low Risk 🟢",
        "Status": "Pending Review ⏳"
    },
    {
        "Circular ID": "SEBI/HO/2026/002",
        "Title": "Cybersecurity & Cyber Resilience Framework for Stock Brokers",
        "Date Analyzed": "01 Jul 2026",
        "Risk Rating": "High Risk 🔴",
        "Status": "Completed ✅"
    }
]

df_history = pd.DataFrame(history_data)

# 5. Display History Table
st.subheader(f"📑 Past Circular Reports ({len(df_history)})")
st.dataframe(
    df_history,
    use_container_width=True,
    hide_index=True
)

st.markdown("---")

# 6. View / Download Archived Report Section
st.subheader("🔍 View Past Circular Summary")
col_select_circ, col_action = st.columns([3, 1])

with col_select_circ:
    selected_circ = st.selectbox(
        "Select Circular to View", 
        df_history["Circular ID"] + " - " + df_history["Title"]
    )

with col_action:
    st.write(" ") # Spacing
    st.write(" ")
    if st.button("📄 View Full Summary", type="primary", use_container_width=True):
        st.info(f"Loading detailed report summary for **{selected_circ.split(' - ')[0]}**...")