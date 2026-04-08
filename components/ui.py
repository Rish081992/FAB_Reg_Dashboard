import pandas as pd
import streamlit as st
from components.data import ENTITIES, REGIMES


def inject_css():
    st.markdown(
        """
        <style>
        .metric-card {
            background: rgba(8,18,31,.78);
            border: 1px solid #21324d;
            border-radius: 16px;
            padding: 16px;
            min-height: 92px;
        }
        .metric-card .value { font-size: 1.7rem; font-weight: 700; }
        .metric-card .label { color: #d7e0ee; margin-top: 4px; }
        .metric-card .sub { color: #9fb0c9; font-size: .82rem; margin-top: 4px; }
        .mini-note { color: #9fb0c9; font-size: .85rem; }
        .status-pill { padding: 4px 10px; border-radius: 999px; font-size: 12px; display: inline-block; }
        .green { background: rgba(30,203,139,.16); color: #9af0cf; border: 1px solid rgba(30,203,139,.3); }
        .amber { background: rgba(255,181,71,.15); color: #ffd28a; border: 1px solid rgba(255,181,71,.3); }
        .slate { background: rgba(113,131,156,.15); color: #d0d7e2; border: 1px solid rgba(113,131,156,.3); }
        </style>
        """,
        unsafe_allow_html=True,
    )


def status_class(value: str) -> str:
    value = str(value or "")
    if value in ["Applicable", "Active", "Approved", "Closed"]:
        return "green"
    if value in ["Conditional", "Expiring", "Open", "Pending", "High", "Under Review"]:
        return "amber"
    return "slate"


def pill(value: str) -> str:
    text = "–" if value == "Not Applicable" else str(value)
    return f'<span class="status-pill {status_class(value)}">{text}</span>'


def metric_card(value: str, label: str, sub: str = ""):
    st.markdown(
        f"""
        <div class="metric-card">
          <div class="value">{value}</div>
          <div class="label">{label}</div>
          <div class="sub">{sub}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def apply_sidebar_filters():
    st.sidebar.markdown("### Global Filters")
    q = st.sidebar.text_input("Search", value=st.session_state.get("search", ""))
    entity = st.sidebar.selectbox("Entity", ["All entities"] + [e["name"] for e in ENTITIES], index=0)
    regime = st.sidebar.selectbox("Regime", ["All regimes"] + REGIMES, index=0)
    st.session_state.search = q
    st.session_state.entity_filter = entity
    st.session_state.regime_filter = regime


def filters_match(entity_name: str, regime_name: str, haystack: str) -> bool:
    q = st.session_state.get("search", "").strip().lower()
    ef = st.session_state.get("entity_filter", "All entities")
    rf = st.session_state.get("regime_filter", "All regimes")
    return (not q or q in haystack.lower()) and (ef == "All entities" or entity_name == ef) and (rf == "All regimes" or regime_name == rf)


def dataframe_from_records(records):
    return pd.DataFrame(records)
