import streamlit as st
from components.data import ENTITIES, REFERENCE_DATA
from components.state import initialize_state, is_admin
from components.ui import inject_css

st.set_page_config(page_title="Reference Data Admin", layout="wide")
initialize_state()
inject_css()

st.title("Reference Data Admin")
st.caption("Admin-only configuration for entities, regimes, users, roles, and master data.")

if not is_admin():
    st.warning("Admin-only editing. Current role can review but not maintain reference data.")
else:
    st.button("Add Reference Record")

c1, c2, c3 = st.columns(3)
with c1:
    st.subheader("Entities")
    st.dataframe(ENTITIES[:6], use_container_width=True, hide_index=True)
with c2:
    st.subheader("Users & Roles")
    st.dataframe(REFERENCE_DATA["users"], use_container_width=True, hide_index=True)
with c3:
    st.subheader("Products")
    st.dataframe([{"product": p} for p in REFERENCE_DATA["products"]], use_container_width=True, hide_index=True)
