import streamlit as st
import plotly.express as px
import pandas as pd

def compliance_pie_chart():
    # Compliance Status Data
    data = pd.DataFrame({
        "Status": ["Completed", "Pending", "High Risk"],
        "Count": [13, 12, 4]
    })
    
    # Donut / Pie Chart
    fig = px.pie(
        data, 
        values="Count", 
        names="Status", 
        title="Compliance Status Overview",
        color_discrete_sequence=["#16A34A", "#F59E0B", "#DC2626"],
        hole=0.4
    )
    fig.update_layout(margin=dict(t=40, b=0, l=0, r=0))
    st.plotly_chart(fig, use_container_width=True)


def monthly_trend_chart():
    # Monthly Compliance Data
    data = pd.DataFrame({
        "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
        "Circulars": [5, 8, 10, 12, 18, 25]
    })
    
    # Bar Chart
    fig = px.bar(
        data, 
        x="Month", 
        y="Circulars", 
        title="Monthly Compliance Trend",
        color_discrete_sequence=["#2563EB"]
    )
    fig.update_layout(margin=dict(t=40, b=0, l=0, r=0))
    st.plotly_chart(fig, use_container_width=True)