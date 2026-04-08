import streamlit as st
from components.data import ENTITIES, REGIMES, HEATMAP
from components.state import initialize_state, can_edit
from components.ui import inject_css

st.set_page_config(page_title="Entity Heatmap", layout="wide")
initialize_state()
inject_css()

st.title("Entity Heatmap")
st.caption("Core review screen. Select an entity-regime pair and push the record into the Applicability Detail page.")

if can_edit():
    st.button("Propose Change", use_container_width=False)
else:
    st.info("Read only for current role.")

selection_cols = st.columns(3)
entity_name = selection_cols[0].selectbox("Entity", [e["name"] for e in ENTITIES])
regime_name = selection_cols[1].selectbox("Regime", REGIMES)
if selection_cols[2].button("Open Applicability Detail", use_container_width=True):
    entity = next(e for e in ENTITIES if e["name"] == entity_name)
    status = HEATMAP[entity["id"]][regime_name]
    st.session_state.selected_detail = {
        "entity": entity["name"],
        "jurisdiction": entity["jurisdiction"],
        "regulator": entity["regulator"],
        "regime": regime_name,
        "status": status,
        "rationale": "This entity is directly mapped in-scope for the selected regime based on booking footprint and local regulatory perimeter." if status == "Applicable" else ("Applicability depends on booking model, counterparty location, product type, or execution facts." if status == "Conditional" else "No direct applicability is currently mapped for this entity-regime pair."),
        "triggerConditions": "Cross-border activity, delegated reporting structure, execution venue, or product scope may trigger obligations." if status == "Conditional" else "No additional trigger conditions recorded.",
        "owner": "Compliance Governance",
        "reviewer": "Regulatory Reporting Lead",
        "reviewDate": "2026-02-25",
        "nextReviewDate": "2026-06-30",
        "source": "Internal legal-entity inventory and regime applicability note.",
        "approvalStatus": "Approved" if status == "Not Applicable" else "Under Review",
        "linkedExemptions": "Relevant exemptions linked where applicable" if status == "Applicable" else "None linked",
        "linkedDecision": "Decision log available for interpretation history",
    }
    st.success("Selected record updated. Open the Applicability Detail page from the sidebar.")

rows = []
for entity in ENTITIES:
    row = {"Entity": entity["name"], "Type": entity["type"], "Regulator": entity["regulator"]}
    for regime in REGIMES:
        row[regime] = HEATMAP[entity["id"]][regime]
    rows.append(row)

st.dataframe(rows, use_container_width=True, hide_index=True)
