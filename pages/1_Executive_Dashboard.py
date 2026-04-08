import streamlit as st
from components.data import ENTITIES, REGIMES, HEATMAP
from components.state import initialize_state
from components.ui import inject_css, metric_card, pill, filters_match

st.set_page_config(page_title="Executive Dashboard", layout="wide")
initialize_state()
inject_css()

st.title("Executive Dashboard")
st.caption("Read-only management view showing open items, expiring exemptions, and pending approvals.")

products = st.session_state.products
exemptions = st.session_state.exemptions
decisions = st.session_state.decisions
approvals = st.session_state.approvals

all_statuses = [v for row in HEATMAP.values() for v in row.values()]
applicable = sum(1 for v in all_statuses if v == "Applicable")
conditional = sum(1 for v in all_statuses if v == "Conditional")
expiring = sum(1 for e in exemptions if e["status"] == "Expiring")
open_items = sum(1 for d in decisions if d["status"] == "Open")
pending = sum(1 for a in approvals if a["status"] == "Pending")

cols = st.columns(5)
with cols[0]: metric_card(str(len(REGIMES)), "Regimes")
with cols[1]: metric_card(str(len(ENTITIES)), "Entities")
with cols[2]: metric_card(f"{applicable} / {conditional}", "Applicable / Conditional", "Mapped outcomes")
with cols[3]: metric_card(str(expiring), "Exemptions Expiring")
with cols[4]: metric_card(str(pending), "Pending Approvals")

left, right = st.columns([2,1])
with left:
    st.subheader("Heatmap Snapshot")
    header = ["Entity"] + REGIMES[:6]
    rows = []
    for entity in ENTITIES[:6]:
        row = {"Entity": entity["name"]}
        for regime in REGIMES[:6]:
            row[regime] = HEATMAP[entity["id"]][regime]
        rows.append(row)
    st.dataframe(rows, use_container_width=True, hide_index=True)

with right:
    st.subheader("Open Decisions")
    shown = False
    for d in decisions:
        if d["status"] == "Open" and filters_match(d["entity"], d["regime"], " ".join(map(str, d.values()))):
            shown = True
            st.markdown(f"**{d['question']}**")
            st.caption(f"{d['entity']} · {d['regime']}")
            st.divider()
    if not shown:
        st.caption("No open decisions under current filters.")

    st.subheader("Expiring Exemptions")
    shown = False
    for e in exemptions:
        if e["status"] == "Expiring" and filters_match(e["entity"], e["regime"], " ".join(map(str, e.values()))):
            shown = True
            st.markdown(f"**{e['exemption']}**")
            st.caption(f"{e['entity']} · expires {e['expiry']}")
            st.divider()
    if not shown:
        st.caption("No expiring exemptions under current filters.")
