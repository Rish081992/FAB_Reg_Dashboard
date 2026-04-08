import streamlit as st
from components.state import initialize_state, can_edit
from components.ui import inject_css, filters_match

st.set_page_config(page_title="Decision Log", layout="wide")
initialize_state()
inject_css()

st.title("Decision Log")
st.caption("Preserve interpretation history, rationale, ownership, and closure status.")

if can_edit():
    with st.expander("Add Decision"):
        c1, c2 = st.columns(2)
        date = c1.date_input("Date")
        owner = c2.text_input("Owner")
        entity = c1.text_input("Entity")
        regime = c2.text_input("Regime")
        question = st.text_area("Decision question")
        rationale = st.text_area("Rationale")
        if st.button("Save Decision"):
            if entity and regime and question:
                st.session_state.decisions.insert(0, {
                    "id": 7000 + len(st.session_state.decisions),
                    "date": str(date),
                    "entity": entity,
                    "regime": regime,
                    "question": question,
                    "outcome": "Open",
                    "owner": owner or st.session_state.role,
                    "rationale": rationale,
                    "status": "Open",
                })
                st.success("Decision added.")
            else:
                st.error("Please fill Entity, Regime, and Decision question.")

for item in st.session_state.decisions:
    if filters_match(item["entity"], item["regime"], " ".join(map(str, item.values()))):
        with st.container(border=True):
            st.subheader(item["question"])
            st.caption(f"{item['date']} · {item['entity']} · {item['regime']}")
            st.write(f"Owner: {item['owner']}")
            st.write(f"Outcome: {item['outcome']}")
            st.write(item["rationale"])
            if can_edit():
                st.button(f"Edit Decision #{item['id']}", key=f"edit_dec_{item['id']}")
