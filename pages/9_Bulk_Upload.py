import streamlit as st
from components.state import initialize_state, can_edit
from components.ui import inject_css

st.set_page_config(page_title="Bulk Upload", layout="wide")
initialize_state()
inject_css()

st.title("Bulk Upload")
st.caption("Controlled Excel-based import for bulk updates. This is support tooling, not the primary operating model.")

if can_edit():
    uploaded = st.file_uploader("Upload Excel template", type=["xlsx", "xls", "csv"])
    if uploaded is not None:
        st.success(f"Received file: {uploaded.name}")
        st.info("Prototype only: validation and import flow would process the uploaded file here.")
else:
    st.info("Bulk upload is available only to editor/approver/admin roles.")

c1, c2, c3 = st.columns(3)
with c1:
    st.subheader("Templates")
    st.write("Download controlled templates for entity-regime mappings, field mappings, or exemptions.")
    st.button("Download Template")
with c2:
    st.subheader("Validation Rules")
    st.write("System checks invalid regimes, missing owners, duplicate rows, and invalid dates before import.")
    st.warning("12 rows flagged in sample upload")
with c3:
    st.subheader("Import Outcome")
    st.write("Accepted rows move to draft or approval workflow depending on materiality.")
    st.button("View Error Log")
