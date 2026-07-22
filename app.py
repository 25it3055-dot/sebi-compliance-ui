import pandas as pd
import streamlit as st
from components.charts import bar_chart, pie_chart

# Page Configuration
st.set_page_config(
    page_title="SEBI Compliance Dashboard", page_icon="📑", layout="wide"
)

st.sidebar.title("🏛️ SEBI Portal")

st.sidebar.markdown("---")

st.sidebar.success("AI Compliance Assistant")

st.sidebar.markdown("---")
import streamlit as st

# Sidebar me logo dikhane ke liye:
st.sidebar.image("assets/logo.png", width=120)

# Main Title
st.title("📑 SEBI Agentic Compliance Dashboard")
st.write("---")

# 1. Dashboard Metrics / Cards
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="📄 Total Circulars", value="25")

with col2:
    st.metric(label="⚠ High Risk", value="4", delta_color="inverse")

with col3:
    st.metric(label="⏳ Pending Tasks", value="12")

with col4:
    st.metric(label="✅ Completed", value="13")

st.write("---")

# 2. Plotly Charts Section
left, right = st.columns(2)

with left:
    st.plotly_chart(pie_chart(), use_container_width=True)

with right:
    st.plotly_chart(bar_chart(), use_container_width=True)

st.write("---")

# 3. Recent Compliance Tasks Table
st.subheader("📋 Recent Compliance Tasks")

data = {
    "Task ID": ["TSK-101", "TSK-102", "TSK-103", "TSK-104"],
    "Category": [
        "KYC Norms",
        "Cybersecurity",
        "Risk Management",
        "Insider Trading",
    ],
    "Deadline": ["2026-07-25", "2026-07-30", "2026-08-05", "2026-08-10"],
    "Priority": ["High", "Medium", "High", "Low"],
    "Status": ["Pending", "In Progress", "Pending", "Completed"],
}

df = pd.DataFrame(data)

# Table Render
st.dataframe(df, use_container_width=True)
st.subheader("📅 Upcoming Deadlines")

deadline_data = {
    "Task": [
        "Update KYC Process",
        "Submit Compliance Report",
        "Notify Clients"
    ],
    "Deadline": [
        "22 Jul 2026",
        "25 Jul 2026",
        "28 Jul 2026"
    ]
}

st.table(deadline_data)

