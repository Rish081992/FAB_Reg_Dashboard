import streamlit as st
from components.state import initialize_state, can_edit
from components.ui import inject_css, filters_match

st.set_page_config(page_title="Instrument Field Explorer", layout="wide")
initialize_state()
inject_css()

st.title("Instrument Field Explorer")
st.caption("Product-level mapping of reporting fields by entity and regime.")

if can_edit():
    with st.expander("Add Field Mapping"):
        c1, c2 = st.columns(2)
        product = c1.text_input("Product")
        entity = c2.text_input("Entity")
        regime = c1.text_input("Regime")
        rule = c2.selectbox("Rule", ["Applicable", "Conditional"])
        req_fields = st.text_area("Required fields (comma separated)")
        rationale = st.text_area("Rationale")
        if st.button("Save Field Mapping"):
            if product and entity and regime:
                st.session_state.products.insert(0, {
                    "id": 3000 + len(st.session_state.products),
                    "product": product,
                    "entity": entity,
                    "regime": regime,
                    "rule": rule,
                    "requiredFields": [x.strip() for x in req_fields.split(",") if x.strip()],
                    "rationale": rationale,
                    "reviewStatus": "Draft",
                })
                st.session_state.approvals.insert(0, {
                    "id": 4000 + len(st.session_state.approvals),
                    "itemType": "Field Mapping Change",
                    "submittedBy": st.session_state.role,
                    "submissionDate": "2026-04-08",
                    "entity": entity,
                    "regime": regime,
                    "summary": f"Added field mapping for {product}.",
                    "priority": "Medium",
                    "status": "Pending",
                })
                st.success("Field mapping added.")
            else:
                st.error("Please fill Product, Entity, and Regime.")

for item in st.session_state.products:
    haystack = " ".join(map(str, [item["product"], item["entity"], item["regime"], item["rule"], item["rationale"], *item["requiredFields"]]))
    if filters_match(item["entity"], item["regime"], haystack):
        with st.container(border=True):
            a, b = st.columns([3,1])
            with a:
                st.subheader(item["product"])
                st.caption(f"{item['entity']} · {item['regime']}")
            with b:
                st.write(item["rule"])
                st.write(item["reviewStatus"])
            st.write(", ".join(item["requiredFields"]))
            st.caption(item["rationale"])
            if can_edit():
                st.button(f"Edit Mapping #{item['id']}", key=f"edit_map_{item['id']}")
