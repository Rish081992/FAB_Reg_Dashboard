import streamlit as st
from components.data import ROLES, seed_state


def initialize_state():
    if "role" not in st.session_state:
        st.session_state.role = ROLES[0]
    for key, value in seed_state().items():
        if key not in st.session_state:
            st.session_state[key] = value
    if "search" not in st.session_state:
        st.session_state.search = ""
    if "entity_filter" not in st.session_state:
        st.session_state.entity_filter = "All entities"
    if "regime_filter" not in st.session_state:
        st.session_state.regime_filter = "All regimes"


def can_edit() -> bool:
    return st.session_state.role in ["Compliance Editor", "Approver", "Admin"]


def can_approve() -> bool:
    return st.session_state.role in ["Approver", "Admin"]


def is_admin() -> bool:
    return st.session_state.role == "Admin"
