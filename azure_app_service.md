# Azure App Service Deployment Guide

## Recommended route
Deploy this Streamlit app as a Linux web app using a custom container.

## Option A: App Service with Docker
1. Build the Docker image from the included `Dockerfile`.
2. Push the image to Azure Container Registry or another registry approved by the client.
3. Create an Azure Web App for Containers.
4. Point the Web App to the container image.
5. Set any environment variables in App Settings.
6. Expose port `8501` or map the platform `PORT` to the Streamlit startup command.

## Startup command
The included `startup.sh` runs:

```bash
streamlit run app.py --server.port=${PORT:-8501} --server.address=0.0.0.0
```

## App settings to consider
- `PORT`
- `STREAMLIT_SERVER_HEADLESS=true`
- `STREAMLIT_BROWSER_GATHER_USAGE_STATS=false`

## Suggested client hardening
- Front with Azure Application Gateway / WAF if required
- Integrate Microsoft Entra ID in front of the app or via app auth
- Store secrets in Azure Key Vault
- Restrict ingress using private networking if required
- Add CI/CD via Azure DevOps or GitHub Actions

## Phase 2 production upgrades
- Replace session-state demo data with PostgreSQL / Azure SQL / Snowflake data access
- Add real authentication and RBAC
- Add audit logging and approval persistence
