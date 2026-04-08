import streamlit as st
from components.state import initialize_state, can_edit
from components.ui import inject_css

st.set_page_config(page_title="Applicability Detail", layout="wide")
initialize_state()
inject_css()

detail = st.session_state.selected_detail

st.title("Applicability Detail")
st.caption("The governable record behind a heatmap cell. This is where compliance interprets, documents, and submits material changes.")

meta_cols = st.columns(4)
fields = [
    ("Entity", detail["entity"]),
    ("Jurisdiction", detail["jurisdiction"]),
    ("Regulator", detail["regulator"]),
    ("Regime", detail["regime"]),
    ("Owner", detail["owner"]),
    ("Reviewer", detail["reviewer"]),
    ("Last Review", detail["reviewDate"]),
    ("Next Review", detail["nextReviewDate"]),
]
for i, (k, v) in enumerate(fields):
    with meta_cols[i % 4]:
        st.metric(k, v)

left, right = st.columns([2,1])
with left:
    st.subheader("Current Status")
    st.write(detail["status"])
    if can_edit():
        rationale = st.text_area("Rationale", value=detail["rationale"], height=120)
        trigger = st.text_area("Trigger Conditions", value=detail["triggerConditions"], height=120)
        source = st.text_input("Source Reference", value=detail["source"])
        a, b = st.columns(2)
        if a.button("Save Draft"):
            detail["rationale"] = rationale
            detail["triggerConditions"] = trigger
            detail["source"] = source
            st.success("Draft saved in session.")
        if b.button("Submit for Approval"):
            detail["rationale"] = rationale
            detail["triggerConditions"] = trigger
            detail["source"] = source
            st.session_state.approvals.insert(0, {
                "id": 2000 + len(st.session_state.approvals),
                "itemType": "Applicability Change",
                "submittedBy": st.session_state.role,
                "submissionDate": "2026-04-08",
                "entity": detail["entity"],
                "regime": detail["regime"],
                "summary": "Updated rationale / trigger conditions / source reference.",
                "priority": "High",
                "status": "Pending",
            })
            st.success("Submitted for approval.")
    else:
        st.write(detail["rationale"])
        st.write(detail["triggerConditions"])
        st.caption(detail["source"])

with right:
    st.subheader("Governance")
    st.write(f"Approval Status: {detail['approvalStatus']}")
    st.write(f"Linked Exemptions: {detail['linkedExemptions']}")
    st.write(f"Linked Decision: {detail['linkedDecision']}")
