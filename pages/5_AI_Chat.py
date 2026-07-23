import streamlit as st
from components.sidebar import render_sidebar

# 1. Render Sidebar
render_sidebar()

# 2. Page Title & Subtitle
st.title("💬 AI Compliance Assistant")
st.caption("Ask questions, clarify regulation doubts, and get instant guidance on SEBI circulars.")

st.markdown("---")

# 3. Suggested Quick Questions
st.subheader("💡 Suggested Prompts")
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("📌 Summarize KYC changes", use_container_width=True):
        st.session_state["user_input"] = "Summarize the key KYC policy changes."

with col2:
    if st.button("⚠️ What are non-compliance penalties?", use_container_width=True):
        st.session_state["user_input"] = "What are the potential penalties for missing this deadline?"

with col3:
    if st.button("📋 List high priority action items", use_container_width=True):
        st.session_state["user_input"] = "List all high priority actionable items for compliance team."

st.markdown("---")

# 4. Initialize Chat History in Session State
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant", 
            "content": "👋 Hello! I am your **SEBI AI Compliance Assistant**. Ask me anything about recent circulars, penalties, or compliance deadlines."
        }
    ]

# 5. Display Chat Messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 6. Chat Input Bar
prompt = st.chat_input("Ask a question about SEBI compliance...")

# Handle user input from input bar or suggested buttons
if prompt:
    # Add User Message to History
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Simulated AI Response
    with st.chat_message("assistant"):
        response_text = f"🤖 **AI Analysis:** Based on SEBI Circular *SEBI/HO/2026/012*, regarding your query **'{prompt}'**:\n\n" \
                        f"1. **Primary Requirement:** Entities must complete verification within 30 days.\n" \
                        f"2. **Documentation:** Updated identity proof and address logs must be submitted online.\n" \
                        f"3. **Penalty Warning:** Non-compliance by **30 Jul 2026** may attract regulatory notices."
        
        st.markdown(response_text)
        st.session_state.messages.append({"role": "assistant", "content": response_text})