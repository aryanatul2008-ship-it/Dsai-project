
import streamlit as st

st.set_page_config(
    page_title="HealthClaim AI",
    page_icon="🏥",
    layout="wide"
)

st.title("🏥 HealthClaim AI")

st.subheader("Healthcare Cost Estimation and Insurance Billing Anomaly Detection")

st.write(
    "An AI-powered application for estimating medical insurance costs "
    "and identifying unusual insurance claims for human review."
)

st.divider()

st.info(
    "This application is an academic project. "
    "Predictions are estimates and should not be used as medical, "
    "insurance, or fraud-determination decisions."
)

st.header("Project Features")

col1, col2 = st.columns(2)

with col1:
    st.subheader("💰 Medical Cost Estimation")
    st.write(
        "Estimate medical insurance charges using patient information "
        "and a trained machine learning model."
    )

with col2:
    st.subheader("🔍 Billing Anomaly Detection")
    st.write(
        "Identify unusual insurance claims using machine learning "
        "and rule-based billing checks."
    )

st.divider()

st.caption("HealthClaim AI | DSAI Lab Project")
