import streamlit as st
from components.data import ROLES
from components.state import initialize_state
from components.ui import inject_css, apply_sidebar_filters

st.set_page_config(page_title="FAB Regulatory Reporting Platform", page_icon="🏦", layout="wide")
initialize_state()
inject_css()

st.title("FAB Regulatory Reporting Platform")
st.caption("Hosted Streamlit multipage prototype for review, editing, approvals, and admin workflows")

with st.sidebar:
    st.markdown("## Role View")
    st.session_state.role = st.selectbox("Active role", ROLES, index=ROLES.index(st.session_state.role))
    st.caption("Switch roles to test viewer, editor, approver, and admin access.")

apply_sidebar_filters()

st.markdown(
    f"""
    ### Start here
    Use the pages in the left sidebar to move across the prototype. Current role: **{st.session_state.role}**.

    This app includes:
    - Executive Dashboard
    - Entity Heatmap
    - Applicability Detail
    - Instrument Field Explorer
    - Exemptions Tracker
    - Decision Log
    - Pending Approvals
    - Reference Data Admin
    - Bulk Upload
    """
)

c1, c2 = st.columns([2,1])
with c1:
    st.info("This is a deployable Streamlit prototype structured for Azure or Snowflake hosting. It is not yet connected to a persistent database or SSO.")
with c2:
    st.success("Use the left sidebar pages to review or edit the workflow.")
