# Snowflake Deployment Guide

## Fit
This app can be adapted for Streamlit in Snowflake. The included `snowflake.yml` and `environment.yml` provide a starting point.

## What is included
- `app.py` as the main file
- `pages/` for multipage navigation
- `snowflake.yml` as a starter project definition
- `environment.yml` for package specification

## Typical deployment flow
1. Install Snowflake CLI in the client environment.
2. Configure a Snowflake connection with rights to create Streamlit apps.
3. Update `snowflake.yml` with the correct stage, warehouse, database, and schema context.
4. Deploy using Snowflake CLI.

Example command:

```bash
snow streamlit deploy --replace
```

## Things to validate with client data platform team
- database and schema where the app should live
- compute warehouse for the app
- access model and role grants
- whether data will stay as demo seed data or be read from Snowflake tables

## Important caveats
- This prototype currently uses Streamlit session state rather than persistent storage.
- External-resource restrictions and other platform limitations should be reviewed before productionizing.
- Authentication and authorization design should align to Snowflake roles and any client IAM expectations.
