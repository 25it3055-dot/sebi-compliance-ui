import streamlit as st
import os

def render_sidebar():
    """Sidebar component for SEBI Compliance Dashboard"""
    st.sidebar.title("🏛️ SEBI Portal")
    
    # Logo Check (if exists)
    if os.path.exists("assets/logo.png"):
        st.sidebar.image("assets/logo.png", width=120)
    
    st.sidebar.markdown("---")
    
    # Status Badges
    st.sidebar.success("🟢 AI System Active")
    st.sidebar.info("📋 Compliance Engine v1.0")
    
    st.sidebar.markdown("---")
    st.sidebar.caption("Powered by SEBI Agentic Compliance")