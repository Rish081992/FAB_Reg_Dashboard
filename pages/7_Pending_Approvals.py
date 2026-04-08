import streamlit as st
from components.state import initialize_state, can_approve
from components.ui import inject_css

st.set_page_config(page_title="Pending Approvals", layout="wide")
initialize_state()
inject_css()

st.title("Pending Approvals")
st.caption("Maker-checker workflow for material changes.")

if can_approve():
    st.success("Approve / Reject enabled for current role.")
else:
    st.info("Read only for current role.")

for item in list(st.session_state.approvals):
    with st.container(border=True):
        c1, c2 = st.columns([4,1])
        with c1:
            st.subheader(item["itemType"])
            st.caption(f"{item['entity']} · {item['regime']} · submitted by {item['submittedBy']} on {item['submissionDate']}")
            st.write(item["summary"])
        with c2:
            st.write(f"Priority: {item['priority']}")
            st.write(f"Status: {item['status']}")
            if can_approve():
                if st.button(f"Approve #{item['id']}"):
                    item["status"] = "Approved"
                    st.rerun()
                if st.button(f"Reject #{item['id']}"):
                    item["status"] = "Rejected"
                    st.rerun()
