import streamlit as st
import pandas as pd
from components.sidebar import render_sidebar

# 1. Render Sidebar
render_sidebar()

# 2. Page Title
st.title("📋 Compliance Action Tasks")
st.caption("Track, filter, and manage action items extracted from analyzed SEBI circulars.")

st.markdown("---")

# 3. Search and Filters Section
col_search, col_status, col_prio = st.columns([2, 1, 1])

with col_search:
    search_query = st.text_input("🔍 Search Tasks", placeholder="Search by task name or circular...")

with col_status:
    status_filter = st.selectbox("Status", ["All", "Pending", "In Progress", "Completed"])

with col_prio:
    priority_filter = st.selectbox("Priority", ["All", "High 🔴", "Medium 🟡", "Low 🟢"])

st.markdown("---")

# 4. Dummy Task Data Setup
tasks_data = [
    {
        "ID": "TSK-101",
        "Task Name": "Update KYC Policy Document",
        "Department": "Legal & Compliance",
        "Priority": "High 🔴",
        "Status": "Pending ⏳",
        "Deadline": "30 Jul 2026"
    },
    {
        "ID": "TSK-102",
        "Task Name": "Notify Active Clients via Email",
        "Department": "Operations",
        "Priority": "High 🔴",
        "Status": "Completed ✅",
        "Deadline": "25 Jul 2026"
    },
    {
        "ID": "TSK-103",
        "Task Name": "Conduct Staff Training Session",
        "Department": "Human Resources",
        "Priority": "Medium 🟡",
        "Status": "In Progress 🔄",
        "Deadline": "05 Aug 2026"
    },
    {
        "ID": "TSK-104",
        "Task Name": "Schedule Internal Compliance Audit",
        "Department": "Risk Management",
        "Priority": "Medium 🟡",
        "Status": "Pending ⏳",
        "Deadline": "15 Aug 2026"
    },
    {
        "ID": "TSK-105",
        "Task Name": "Archive Superceded Regulation Docs",
        "Department": "IT / Records",
        "Priority": "Low 🟢",
        "Status": "Completed ✅",
        "Deadline": "20 Jul 2026"
    }
]

df = pd.DataFrame(tasks_data)

# 5. Display Tasks Dataframe / Table
st.subheader(f"📌 Task List ({len(df)})")
st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)

st.markdown("---")

# 6. Quick Task Status Update Section
st.subheader("⚡ Quick Task Update")
col_select, col_new_status, col_btn = st.columns([2, 2, 1])

with col_select:
    task_id = st.selectbox("Select Task ID", df["ID"].tolist())

with col_new_status:
    new_status = st.selectbox("Update Status To", ["Pending ⏳", "In Progress 🔄", "Completed ✅"])

with col_btn:
    st.write(" ") # Spacing
    st.write(" ")
    if st.button("Update Status", type="primary"):
        st.success(f"Task **{task_id}** updated to **{new_status}**!")