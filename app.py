import streamlit as st
import pandas as pd

# Reusable Components
from components.cards import metric_cards
from components.charts import compliance_pie_chart, monthly_trend_chart
from utils.style import load_css

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="SEBI Compliance Dashboard",
    page_icon="📑",
    layout="wide"
)

# Load CSS
load_css()

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("🏛️ SEBI Portal")
st.sidebar.markdown("---")
st.sidebar.success("🤖 AI Compliance Assistant")
st.sidebar.markdown("---")

st.sidebar.page_link("app.py", label="🏠 Dashboard")
st.sidebar.page_link("pages/1_Upload.py", label="📤 Upload")
st.sidebar.page_link("pages/2_Analysis.py", label="🤖 Analysis")
st.sidebar.page_link("pages/3_Tasks.py", label="✅ Tasks")
st.sidebar.page_link("pages/4_History.py", label="📜 History")
st.sidebar.page_link("pages/5_AI_Chat.py", label="💬 AI Chat")

st.sidebar.markdown("---")
st.sidebar.caption("Version 1.0")

# -----------------------------
# Main Title
# -----------------------------
st.title("📑 SEBI Agentic Compliance Dashboard")
st.write("AI-powered compliance monitoring and regulatory analysis.")

st.divider()

# -----------------------------
# KPI Cards
# -----------------------------
metric_cards()

st.divider()

# -----------------------------
# Metrics
# -----------------------------
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("📄 Circulars", "25")

with col2:
    st.metric("⚠ High Risk", "4")

with col3:
    st.metric("⏳ Pending", "12")

with col4:
    st.metric("✅ Completed", "13")

st.divider()

# -----------------------------
# Charts
# -----------------------------
left, right = st.columns(2)

with left:
    compliance_pie_chart()

with right:
    monthly_trend_chart()

st.divider()

# -----------------------------
# Recent Compliance Tasks
# -----------------------------
st.subheader("📋 Recent Compliance Tasks")

data = {
    "Task ID": ["TSK-101", "TSK-102", "TSK-103", "TSK-104"],
    "Category": [
        "KYC Norms",
        "Cybersecurity",
        "Risk Management",
        "Insider Trading"
    ],
    "Deadline": [
        "25 Jul 2026",
        "30 Jul 2026",
        "05 Aug 2026",
        "10 Aug 2026"
    ],
    "Priority": [
        "High",
        "Medium",
        "High",
        "Low"
    ],
    "Status": [
        "Pending",
        "In Progress",
        "Pending",
        "Completed"
    ]
}

df = pd.DataFrame(data)

st.dataframe(df, use_container_width=True)

st.divider()

# -----------------------------
# Upcoming Deadlines
# -----------------------------
st.subheader("📅 Upcoming Deadlines")

deadline_data = pd.DataFrame({
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
})

st.table(deadline_data)

st.success("✅ Frontend Dashboard Ready")

    






    
