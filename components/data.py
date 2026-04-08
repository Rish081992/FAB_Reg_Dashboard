from copy import deepcopy

ROLES = ["CXO Viewer", "Compliance Editor", "Approver", "Admin"]

NAV_ITEMS = [
    "Executive Dashboard",
    "Entity Heatmap",
    "Applicability Detail",
    "Instrument Field Explorer",
    "Exemptions Tracker",
    "Decision Log",
    "Pending Approvals",
    "Reference Data Admin",
    "Bulk Upload",
]

REGIMES = [
    "CFTC",
    "EMIR Refit",
    "UK EMIR",
    "MiFIR (EU)",
    "UK MiFIR",
    "SFTR (EU)",
    "UK SFTR",
    "MAS OTC",
    "HKMA OTC",
    "SAMA",
]

ENTITIES = [
    {"id": 1, "name": "Abu Dhabi Head Office", "location": "Abu Dhabi", "type": "Head Office", "regulator": "CBUAE", "jurisdiction": "UAE"},
    {"id": 2, "name": "ADGM Branch", "location": "Abu Dhabi", "type": "Branch", "regulator": "FSRA", "jurisdiction": "UAE"},
    {"id": 3, "name": "Paris Subsidiary", "location": "Paris", "type": "Subsidiary", "regulator": "ACPR / AMF", "jurisdiction": "France"},
    {"id": 4, "name": "London Branch", "location": "London", "type": "Branch", "regulator": "PRA / FCA", "jurisdiction": "United Kingdom"},
    {"id": 5, "name": "Saudi Operations", "location": "Riyadh", "type": "Branch", "regulator": "SAMA / CMA", "jurisdiction": "Saudi Arabia"},
    {"id": 6, "name": "FABMISR", "location": "Cairo", "type": "Subsidiary", "regulator": "CBE / FRA", "jurisdiction": "Egypt"},
    {"id": 7, "name": "Singapore Branch", "location": "Singapore", "type": "Branch", "regulator": "MAS", "jurisdiction": "Singapore"},
    {"id": 8, "name": "Hong Kong Branch", "location": "Hong Kong", "type": "Branch", "regulator": "HKMA / SFC", "jurisdiction": "Hong Kong"},
    {"id": 9, "name": "India Branch", "location": "Mumbai", "type": "Branch", "regulator": "RBI / SEBI", "jurisdiction": "India"},
    {"id": 10, "name": "FAB Private Bank Suisse", "location": "Switzerland", "type": "Subsidiary", "regulator": "FINMA", "jurisdiction": "Switzerland"},
    {"id": 11, "name": "FAB USA N.V.", "location": "New York", "type": "Branch", "regulator": "NYDFS / CFTC", "jurisdiction": "United States"},
    {"id": 12, "name": "Malaysia Rep Office", "location": "Kuala Lumpur", "type": "Representative Office", "regulator": "BNM", "jurisdiction": "Malaysia"},
    {"id": 13, "name": "China Branch Shanghai", "location": "Shanghai", "type": "Branch", "regulator": "PBOC / CBIRC", "jurisdiction": "China"},
    {"id": 14, "name": "Bahrain Branch", "location": "Bahrain", "type": "Branch", "regulator": "CBB", "jurisdiction": "Bahrain"},
]

HEATMAP = {
    1: {"CFTC": "Conditional", "EMIR Refit": "Conditional", "UK EMIR": "Conditional", "MiFIR (EU)": "Not Applicable", "UK MiFIR": "Not Applicable", "SFTR (EU)": "Conditional", "UK SFTR": "Conditional", "MAS OTC": "Not Applicable", "HKMA OTC": "Not Applicable", "SAMA": "Not Applicable"},
    2: {"CFTC": "Conditional", "EMIR Refit": "Not Applicable", "UK EMIR": "Not Applicable", "MiFIR (EU)": "Not Applicable", "UK MiFIR": "Not Applicable", "SFTR (EU)": "Not Applicable", "UK SFTR": "Not Applicable", "MAS OTC": "Not Applicable", "HKMA OTC": "Not Applicable", "SAMA": "Not Applicable"},
    3: {"CFTC": "Conditional", "EMIR Refit": "Applicable", "UK EMIR": "Not Applicable", "MiFIR (EU)": "Applicable", "UK MiFIR": "Not Applicable", "SFTR (EU)": "Applicable", "UK SFTR": "Not Applicable", "MAS OTC": "Not Applicable", "HKMA OTC": "Not Applicable", "SAMA": "Not Applicable"},
    4: {"CFTC": "Conditional", "EMIR Refit": "Not Applicable", "UK EMIR": "Applicable", "MiFIR (EU)": "Not Applicable", "UK MiFIR": "Applicable", "SFTR (EU)": "Not Applicable", "UK SFTR": "Applicable", "MAS OTC": "Not Applicable", "HKMA OTC": "Not Applicable", "SAMA": "Not Applicable"},
    5: {"CFTC": "Not Applicable", "EMIR Refit": "Not Applicable", "UK EMIR": "Not Applicable", "MiFIR (EU)": "Not Applicable", "UK MiFIR": "Not Applicable", "SFTR (EU)": "Not Applicable", "UK SFTR": "Not Applicable", "MAS OTC": "Not Applicable", "HKMA OTC": "Not Applicable", "SAMA": "Applicable"},
    6: {"CFTC": "Not Applicable", "EMIR Refit": "Not Applicable", "UK EMIR": "Not Applicable", "MiFIR (EU)": "Not Applicable", "UK MiFIR": "Not Applicable", "SFTR (EU)": "Not Applicable", "UK SFTR": "Not Applicable", "MAS OTC": "Not Applicable", "HKMA OTC": "Not Applicable", "SAMA": "Not Applicable"},
    7: {"CFTC": "Conditional", "EMIR Refit": "Not Applicable", "UK EMIR": "Not Applicable", "MiFIR (EU)": "Not Applicable", "UK MiFIR": "Not Applicable", "SFTR (EU)": "Not Applicable", "UK SFTR": "Not Applicable", "MAS OTC": "Applicable", "HKMA OTC": "Not Applicable", "SAMA": "Not Applicable"},
    8: {"CFTC": "Conditional", "EMIR Refit": "Not Applicable", "UK EMIR": "Not Applicable", "MiFIR (EU)": "Not Applicable", "UK MiFIR": "Not Applicable", "SFTR (EU)": "Not Applicable", "UK SFTR": "Not Applicable", "MAS OTC": "Not Applicable", "HKMA OTC": "Applicable", "SAMA": "Not Applicable"},
    9: {"CFTC": "Not Applicable", "EMIR Refit": "Not Applicable", "UK EMIR": "Not Applicable", "MiFIR (EU)": "Not Applicable", "UK MiFIR": "Not Applicable", "SFTR (EU)": "Not Applicable", "UK SFTR": "Not Applicable", "MAS OTC": "Not Applicable", "HKMA OTC": "Not Applicable", "SAMA": "Not Applicable"},
    10: {"CFTC": "Not Applicable", "EMIR Refit": "Conditional", "UK EMIR": "Not Applicable", "MiFIR (EU)": "Conditional", "UK MiFIR": "Not Applicable", "SFTR (EU)": "Conditional", "UK SFTR": "Not Applicable", "MAS OTC": "Not Applicable", "HKMA OTC": "Not Applicable", "SAMA": "Not Applicable"},
    11: {"CFTC": "Applicable", "EMIR Refit": "Not Applicable", "UK EMIR": "Not Applicable", "MiFIR (EU)": "Not Applicable", "UK MiFIR": "Not Applicable", "SFTR (EU)": "Not Applicable", "UK SFTR": "Not Applicable", "MAS OTC": "Not Applicable", "HKMA OTC": "Not Applicable", "SAMA": "Not Applicable"},
    12: {"CFTC": "Not Applicable", "EMIR Refit": "Not Applicable", "UK EMIR": "Not Applicable", "MiFIR (EU)": "Not Applicable", "UK MiFIR": "Not Applicable", "SFTR (EU)": "Not Applicable", "UK SFTR": "Not Applicable", "MAS OTC": "Not Applicable", "HKMA OTC": "Not Applicable", "SAMA": "Not Applicable"},
    13: {"CFTC": "Not Applicable", "EMIR Refit": "Not Applicable", "UK EMIR": "Not Applicable", "MiFIR (EU)": "Not Applicable", "UK MiFIR": "Not Applicable", "SFTR (EU)": "Not Applicable", "UK SFTR": "Not Applicable", "MAS OTC": "Not Applicable", "HKMA OTC": "Not Applicable", "SAMA": "Not Applicable"},
    14: {"CFTC": "Not Applicable", "EMIR Refit": "Not Applicable", "UK EMIR": "Not Applicable", "MiFIR (EU)": "Not Applicable", "UK MiFIR": "Not Applicable", "SFTR (EU)": "Not Applicable", "UK SFTR": "Not Applicable", "MAS OTC": "Not Applicable", "HKMA OTC": "Not Applicable", "SAMA": "Not Applicable"},
}

PRODUCTS = [
    {"id": 1, "product": "FX Linear", "entity": "Abu Dhabi Head Office", "regime": "CFTC", "rule": "Conditional", "requiredFields": ["UTI", "Counterparty LEI", "Execution Timestamp", "Product Type", "Settlement Date"], "rationale": "Triggers where trades face US persons or fall within cross-border reporting conditions.", "reviewStatus": "Approved"},
    {"id": 2, "product": "Rates", "entity": "Paris Subsidiary", "regime": "EMIR Refit", "rule": "Applicable", "requiredFields": ["UTI", "UPI", "Clearing Obligation", "Execution Venue", "Maturity Date", "Collateralisation"], "rationale": "EU subsidiary booking OTC derivatives within EMIR scope.", "reviewStatus": "Approved"},
    {"id": 3, "product": "Repo / SFT", "entity": "London Branch", "regime": "UK SFTR", "rule": "Applicable", "requiredFields": ["Master Agreement Type", "Collateral Type", "Haircut", "Reuse Indicator", "Termination Date"], "rationale": "UK branch securities financing transactions fall within UK SFTR reporting perimeter.", "reviewStatus": "Approved"},
    {"id": 4, "product": "Credit / CDS", "entity": "Singapore Branch", "regime": "MAS OTC", "rule": "Applicable", "requiredFields": ["Counterparty Identifier", "Asset Class", "Trade Date", "Notional Amount", "Maturity Date"], "rationale": "MAS OTC reporting applicable to Singapore branch derivatives activity.", "reviewStatus": "Approved"},
    {"id": 5, "product": "Equity Derivatives", "entity": "Hong Kong Branch", "regime": "HKMA OTC", "rule": "Applicable", "requiredFields": ["Transaction Reference", "Product Category", "Execution Date", "Counterparty", "Underlying Identifier"], "rationale": "HK branch booking in-scope derivatives with local reporting obligations.", "reviewStatus": "Approved"},
    {"id": 6, "product": "Structured Finance", "entity": "Saudi Operations", "regime": "SAMA", "rule": "Applicable", "requiredFields": ["Client Classification", "Instrument Type", "Approval Reference", "Booking Entity", "Disclosure Status"], "rationale": "Internal reference mapping for KSA reporting and supervisory governance.", "reviewStatus": "Draft"},
    {"id": 7, "product": "Commodities", "entity": "Abu Dhabi Head Office", "regime": "EMIR Refit", "rule": "Conditional", "requiredFields": ["Counterparty Country", "Commodity Class", "Trade Date", "Valuation", "Collateral"], "rationale": "Applies where EU-facing counterparties or booking patterns trigger EMIR conditions.", "reviewStatus": "Under Review"},
]

EXEMPTIONS = [
    {"id": 1, "entity": "Abu Dhabi Head Office", "regime": "CFTC", "exemption": "End-user exception", "lawReference": "CFTC 17 CFR Part 50", "owner": "Sarah Al-Mansouri", "expiry": "2026-09-30", "status": "Active", "notes": "Applies where hedging criteria are evidenced and approved.", "approvalStatus": "Approved"},
    {"id": 2, "entity": "Paris Subsidiary", "regime": "EMIR Refit", "exemption": "Intragroup reporting relief", "lawReference": "EMIR Art. 9", "owner": "James Whitfield", "expiry": "2026-06-15", "status": "Expiring", "notes": "Annual validation required.", "approvalStatus": "Approved"},
    {"id": 3, "entity": "London Branch", "regime": "UK SFTR", "exemption": "Limited transitional treatment", "lawReference": "UK SFTR RTS", "owner": "Priya Nair", "expiry": "2026-05-10", "status": "Expiring", "notes": "Requires legal confirmation on continuation.", "approvalStatus": "Under Review"},
    {"id": 4, "entity": "Singapore Branch", "regime": "MAS OTC", "exemption": "Threshold-based exclusion", "lawReference": "MAS OTC Rules", "owner": "Ahmed Al-Rashidi", "expiry": "2026-12-31", "status": "Active", "notes": "Monitor monthly threshold usage.", "approvalStatus": "Approved"},
]

DECISIONS = [
    {"id": 1, "date": "2026-02-12", "entity": "Abu Dhabi Head Office", "regime": "CFTC", "question": "Should cross-border trades with US persons be classified as conditional rather than directly applicable?", "outcome": "Approved", "owner": "Sarah Al-Mansouri", "rationale": "Retained as Conditional because applicability depends on counterparty and execution facts.", "status": "Closed"},
    {"id": 2, "date": "2026-02-18", "entity": "Paris Subsidiary", "regime": "EMIR Refit", "question": "Should MiFIR and EMIR mappings be maintained independently for EU branch activities?", "outcome": "Approved", "owner": "James Whitfield", "rationale": "Yes. Transaction reporting and derivative reporting are separate obligations and must remain distinct.", "status": "Closed"},
    {"id": 3, "date": "2026-02-20", "entity": "Saudi Operations", "regime": "SAMA", "question": "Should local product governance fields be captured in the platform even where reporting is not transaction-level?", "outcome": "Open", "owner": "Ahmed Al-Rashidi", "rationale": "Pending compliance sign-off on data dictionary.", "status": "Open"},
]

APPROVALS = [
    {"id": 101, "itemType": "Applicability Change", "submittedBy": "Priya Nair", "submissionDate": "2026-02-22", "entity": "London Branch", "regime": "UK SFTR", "summary": "Change rationale and review date for UK SFTR applicability.", "priority": "High", "status": "Pending"},
    {"id": 102, "itemType": "Exemption Renewal", "submittedBy": "James Whitfield", "submissionDate": "2026-02-23", "entity": "Paris Subsidiary", "regime": "EMIR Refit", "summary": "Renew intragroup reporting relief and attach annual validation evidence.", "priority": "High", "status": "Pending"},
    {"id": 103, "itemType": "Field Mapping Change", "submittedBy": "Ahmed Al-Rashidi", "submissionDate": "2026-02-24", "entity": "Saudi Operations", "regime": "SAMA", "summary": "Add product governance fields for structured finance workflow.", "priority": "Medium", "status": "Pending"},
]

DEFAULT_DETAIL = {
    "entity": "Paris Subsidiary",
    "jurisdiction": "France",
    "regulator": "ACPR / AMF",
    "regime": "EMIR Refit",
    "status": "Applicable",
    "rationale": "EU subsidiary books in-scope OTC derivative activity and is subject to direct reporting obligations under EMIR Refit.",
    "triggerConditions": "Applies to in-scope derivatives booked through the French subsidiary; review where cross-border delegation applies.",
    "owner": "James Whitfield",
    "reviewer": "Group Compliance Governance",
    "reviewDate": "2026-02-25",
    "nextReviewDate": "2026-06-30",
    "source": "Internal legal-entity mapping and regulatory interpretation note.",
    "approvalStatus": "Approved",
    "linkedExemptions": "Intragroup reporting relief",
    "linkedDecision": "Decision #2",
}

REFERENCE_DATA = {
    "users": [
        {"name": "Sarah Al-Mansouri", "role": "Compliance Editor"},
        {"name": "James Whitfield", "role": "Approver"},
        {"name": "Priya Nair", "role": "Compliance Editor"},
        {"name": "Ahmed Al-Rashidi", "role": "Admin"},
    ],
    "products": ["FX Linear", "Rates", "Credit / CDS", "Equity Derivatives", "Commodities", "Repo / SFT", "Structured Finance"],
}


def seed_state():
    return {
        "products": deepcopy(PRODUCTS),
        "exemptions": deepcopy(EXEMPTIONS),
        "decisions": deepcopy(DECISIONS),
        "approvals": deepcopy(APPROVALS),
        "selected_detail": deepcopy(DEFAULT_DETAIL),
    }
