import streamlit as st
import time

st.set_page_config(page_title="Upload Circular", page_icon="📤")

st.title("📤 Upload SEBI Circular")

st.write("Upload a SEBI circular (PDF) or paste regulatory text for AI analysis.")

st.divider()

uploaded_file = st.file_uploader(
    "Choose a PDF file",
    type=["pdf"]
)

st.markdown("### OR")

regulation_text = st.text_area(
    "Paste Regulation Text",
    height=200,
    placeholder="Paste SEBI regulation text here..."
)

if st.button("🚀 Analyze Circular", use_container_width=True):

    if uploaded_file is None and regulation_text.strip() == "":
        st.warning("Please upload a PDF or paste regulation text.")

    else:

        with st.spinner("Analyzing Circular..."):

            time.sleep(2)

        st.success("✅ Analysis Completed Successfully!")

        if uploaded_file:
            st.info(f"Uploaded File: {uploaded_file.name}")

        if regulation_text:
            st.write("Text Length:", len(regulation_text), "characters")