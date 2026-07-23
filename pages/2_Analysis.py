import streamlit as st
import pandas as pd
from components.sidebar import render_sidebar

# 1. Sidebar Render
render_sidebar()

# 2. Main Title Section
st.title("🤖 AI Compliance Analysis")
st.caption("Detailed breakdown, risk rating, and compliance actionable items extracted by AI.")

st.markdown("---")

# 3. Executive Summary
st.subheader("📄 Executive Summary")
st.info(
    "This SEBI circular introduces revised KYC (Know Your Customer) verification requirements "
    "and mandatory quarterly reporting standards for all registered intermediaries to enhance transparency."
)

st.markdown("---")

# 4. Metrics: Risk Level & Compliance Score
col1, col2 = st.columns(2)

with col1:
    st.markdown("### ⚠️ Risk Level")
    st.error("🔴 **HIGH RISK**")

with col2:
    st.markdown("### 📊 Compliance Score")
    st.progress(82)
    st.caption("Current Readiness: **82%**")

st.markdown("---")

# 5. Affected Departments & Checklist
col_dept, col_check = st.columns(2)

with col_dept:
    st.subheader("🏢 Affected Departments")
    st.markdown("""
    * ⚖️ **Legal & Regulatory**
    * 🔍 **Compliance Team**
    * ⚙️ **Operations**
    * 🛡️ **Risk Management**
    """)

with col_check:
    st.subheader("📋 Actionable Checklist")
    st.checkbox("Update internal KYC verification policy", value=True)
    st.checkbox("Notify all active clients via email", value=True)
    st.checkbox("Conduct employee training session", value=False)
    st.checkbox("Submit quarterly compliance report to SEBI", value=False)

st.markdown("---")

# 6. Recommendations & Important Deadlines
col_rec, col_dead = st.columns(2)

with col_rec:
    st.subheader("💡 AI Recommendations")
    st.success("• Automate KYC document checks to speed up compliance.")
    st.warning("• Ensure client notification is completed prior to the upcoming deadline.")
    st.info("• Schedule an internal audit by next month.")

with col_dead:
    st.subheader("📅 Key Deadlines")
    deadlines_df = pd.DataFrame({
        "Task": ["Update Policy", "Client Notification", "Submit Audit"],
        "Deadline": ["30 Jul 2026", "05 Aug 2026", "15 Aug 2026"]
    })
    st.table(deadlines_df)

st.markdown("---")

# 7. Report Download Button
st.subheader("📥 Export Results")
st.download_button(
    label="Download Full AI Compliance Report (PDF)",
    data="SEBI Circular AI Analysis Report - Sample Content",
    file_name="SEBI_Compliance_Report.txt",
    mime="text/plain",
    type="primary"
)