import streamlit as st
from components.state import initialize_state, can_edit
from components.ui import inject_css, filters_match

st.set_page_config(page_title="Exemptions Tracker", layout="wide")
initialize_state()
inject_css()

st.title("Exemptions Tracker")
st.caption("Maintain legal basis, expiry, ownership, and review workflow for exemptions.")

if can_edit():
    with st.expander("Add Exemption"):
        c1, c2 = st.columns(2)
        entity = c1.text_input("Entity")
        regime = c2.text_input("Regime")
        exemption = c1.text_input("Exemption")
        law_reference = c2.text_input("Law Reference")
        owner = c1.text_input("Owner")
        expiry = c2.date_input("Expiry")
        notes = st.text_area("Notes")
        if st.button("Save Exemption"):
            if entity and regime and exemption:
                st.session_state.exemptions.insert(0, {
                    "id": 5000 + len(st.session_state.exemptions),
                    "entity": entity,
                    "regime": regime,
                    "exemption": exemption,
                    "lawReference": law_reference,
                    "owner": owner or st.session_state.role,
                    "expiry": str(expiry),
                    "status": "Active",
                    "notes": notes,
                    "approvalStatus": "Draft",
                })
                st.session_state.approvals.insert(0, {
                    "id": 6000 + len(st.session_state.approvals),
                    "itemType": "New Exemption",
                    "submittedBy": st.session_state.role,
                    "submissionDate": "2026-04-08",
                    "entity": entity,
                    "regime": regime,
                    "summary": f"New exemption: {exemption}",
                    "priority": "Medium",
                    "status": "Pending",
                })
                st.success("Exemption added.")
            else:
                st.error("Please fill Entity, Regime, and Exemption.")

rows = []
for item in st.session_state.exemptions:
    if filters_match(item["entity"], item["regime"], " ".join(map(str, item.values()))):
        rows.append(item)

st.dataframe(rows, use_container_width=True, hide_index=True)
