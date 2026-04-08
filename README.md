# FAB Regulatory Reporting Platform - Streamlit Prototype

A deployable Streamlit multipage prototype for FAB Global Markets regulatory reporting governance.

## What this includes
- Executive Dashboard
- Entity Heatmap
- Applicability Detail
- Instrument Field Explorer
- Exemptions Tracker
- Decision Log
- Pending Approvals
- Reference Data Admin
- Bulk Upload
- Role-based viewing modes: CXO Viewer, Compliance Editor, Approver, Admin

## Run locally
```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

## What is already working
- Multipage navigation
- Sidebar role switcher
- Global filters
- In-memory edit flows using Streamlit session state
- Approval queue behavior for submitted changes
- Docker packaging for container deployment
- Starter files for Azure and Snowflake deployment

## Project structure
- `app.py` — entrypoint
- `pages/` — all business screens
- `components/` — seed data, state, and UI helpers
- `.streamlit/config.toml` — theme and server config
- `Dockerfile` — container deployment
- `startup.sh` — app startup script for Azure-style hosting
- `snowflake.yml` — starter Snowflake deployment definition
- `environment.yml` — package spec for Snowflake-style deployment
- `azure_app_service.md` — Azure deployment note
- `snowflake_deployment.md` — Snowflake deployment note
- `DEPLOYMENT_CHECKLIST.txt` — client handoff checklist

## Deploy to Azure
Use the included `Dockerfile` or `startup.sh`.
See `azure_app_service.md`.

## Deploy to Snowflake
Adapt `snowflake.yml` and use Snowflake CLI.
See `snowflake_deployment.md`.

## Notes
- This is a hosted prototype and workflow demo.
- Data is currently stored in Streamlit session state only.
- It is not yet connected to a persistent database, SSO, or backend API.
- It is intended for workflow validation and phase-1 hosted review.
