import streamlit as st
import time
from components.sidebar import render_sidebar

# 1. Sidebar render karein
render_sidebar()

# 2. Header Title
st.title("📤 Upload SEBI Circular")
st.caption("Upload a PDF circular or paste regulation text for AI analysis.")

st.markdown("---")

# 3. Layout: Columns for Uploader and Text Area
col1, col2 = st.columns(2)

with col1:
    st.subheader("📄 Upload PDF Document")
    uploaded_file = st.file_uploader(
        "Choose a SEBI Circular (PDF)", 
        type=["pdf"],
        help="Limit 20MB per file • PDF format only"
    )

    if uploaded_file is not None:
        st.info(f"**File Name:** {uploaded_file.name}")
        st.write(f"**File Size:** {round(uploaded_file.size / 1024, 2)} KB")

with col2:
    st.subheader("📝 Or Paste Circular Text")
    circular_text = st.text_area(
        "Paste regulation text here...", 
        height=180,
        placeholder="Enter SEBI circular details, guidelines, or requirements..."
    )

st.markdown("---")

# 4. Action Button & Analysis Logic
if st.button("🔍 Analyze Circular", type="primary", use_container_width=True):
    if uploaded_file is not None or circular_text.strip() != "":
        # Progress Bar Simulation
        progress_text = "Analyzing circular with AI agent..."
        my_bar = st.progress(0, text=progress_text)

        for percent_complete in range(100):
            time.sleep(0.01)
            my_bar.progress(percent_complete + 1, text=progress_text)
            
        time.sleep(0.3)
        my_bar.empty()
        
        st.success("✅ Analysis Complete! Check the **Analysis** page to view results.")
    else:
        st.warning("⚠️ Please upload a PDF file or paste circular text before analyzing.")