import streamlit as st

def load_css():
    """Applies custom CSS for modern Hackathon UI styling"""
    st.markdown("""
        <style>
        /* Main background and clean padding */
        .main {
            background-color: #F8FAFC;
        }
        
        /* Modernized Metric Cards */
        [data-testid="stMetric"] {
            background-color: #FFFFFF;
            padding: 18px 22px;
            border-radius: 12px;
            border: 1px solid #E2E8F0;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }
        
        [data-testid="stMetric"]:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.08);
        }

        /* Metric Label & Value Colors */
        [data-testid="stMetricLabel"] {
            font-size: 14px !important;
            color: #64748B !important;
            font-weight: 600 !important;
        }

        [data-testid="stMetricValue"] {
            font-size: 26px !important;
            color: #0F172A !important;
            font-weight: 700 !important;
        }

        /* Customized Buttons */
        .stButton>button {
            border-radius: 8px;
            font-weight: 600;
            border: none;
            transition: all 0.2s;
        }

        /* Sidebar Styling */
        [data-testid="stSidebar"] {
            background-color: #0F172A;
        }
        [data-testid="stSidebar"] * {
            color: #F8FAFC !important;
        }
        </style>
    """, unsafe_allow_html=True)