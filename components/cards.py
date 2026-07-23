import streamlit as st

def metric_cards():
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(label="📄 Total Circulars", value="25")
    with col2:
        st.metric(label="⚠️ High Risk", value="4")
    with col3:
        st.metric(label="⏳ Pending Tasks", value="12")
    with col4:
        st.metric(label="✅ Completed Tasks", value="13")