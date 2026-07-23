import streamlit as st
import pandas as pd
import os

# Reusable Components Import
from components.cards import metric_cards
from components.charts import compliance_pie_chart, monthly_trend_chart
from utils.style import load_css

# 1. Page Configuration
st.set_page_config(
    page_title="SEBI Compliance Dashboard", 
    page_icon="📑", 
    layout="wide"
)

# Custom CSS Load
load_css()

# --- SIDEBAR SECTION ---
st.sidebar.title("🏛️ SEBI Portal")
st.sidebar.markdown("---")
st.sidebar.success("AI Compliance Assistant")
st.sidebar.markdown("---")
# KPI Cards
metric_cards()

st.divider()

# Charts
col1, col2 = st.columns(2)

with col1:
    compliance_pie_chart()

with col2:
    monthly_trend_chart()
import streamlit as st

# Sidebar me logo dikhane ke liye:
st.sidebar.image("assets/logo.png", width=120)

# Main Title
st.title("📑 SEBI Agentic Compliance Dashboard")
st.write("---")

metric_cards()

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

