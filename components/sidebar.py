import streamlit as st
import os

def render_sidebar():
    """Sidebar component for SEBI Compliance Dashboard"""
    st.sidebar.title("🏛️ SEBI Portal")
    
    # Check if logo exists AND is not empty (size > 0)
    logo_path = "assets/logo.png"
    if os.path.exists(logo_path) and os.path.getsize(logo_path) > 0:
        st.sidebar.image(logo_path, width=120)
    else:
        st.sidebar.markdown("### Agentic Compliance")
    
    st.sidebar.markdown("---")
    
    # Status Badges
    st.sidebar.success("🟢 AI System Active")
    st.sidebar.info("📋 Compliance Engine v1.0")
    
    st.sidebar.markdown("---")
    st.sidebar.caption("Powered by SEBI Agentic Compliance")