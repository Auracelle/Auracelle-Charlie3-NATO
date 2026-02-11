# Security Policy — Auracelle Charlie 3

## Supported Versions

| Version | Supported |
|---------|-----------|
| 3.0.x (NATO Build) | ✅ Active |
| 2.5.x | ⚠️ Critical fixes only |
| < 2.5 | ❌ Unsupported |

## Reporting a Security Vulnerability

This is a proprietary, restricted-access platform. If you have discovered a
potential security vulnerability, please **do not** open a public GitHub issue.

Contact Auracelle AI Governance Labs directly with:
- A description of the vulnerability
- Steps to reproduce
- Potential impact assessment
- Your suggested mitigation (if any)

We aim to acknowledge reports within 48 hours and provide a remediation
timeline within 7 business days.

## Known Security Considerations

### Authentication
- The platform uses Streamlit session-state password authentication, suitable
  for demonstration and research use behind ngrok access control
- For production deployments serving sensitive data, integrate OAuth2 or
  institutional SSO (e.g., Microsoft Entra ID, Okta)
- Password is set via the `APP_PASSWORD` environment variable; the default
  `charlie2025` must be changed before any external-facing deployment

### API Keys
- **Never commit API keys** to version control. Use `.env` (local) or
  Colab secrets / GitHub Actions secrets (CI/CD)
- Rotate the ngrok auth token regularly
- The COMTRADE and TRADEGOV API keys have rate limits; monitor usage

### Data
- No personally identifiable information (PII) is collected or stored
- Simulation session state is in-memory only (not persisted to disk)
- World Bank and trade.gov data are public; no special handling required

### Network
- ngrok tunnels expose the application publicly when active. Close tunnels
  after demonstration sessions
- The FastAPI backend runs on localhost:8000; ensure firewall rules prevent
  external access to port 8000 in shared environments

### Dependencies
- Run `pip-audit` or `safety check` regularly to screen for known CVEs in
  the dependency tree
- `pyngrok==7.2.1` is pinned due to breaking changes; update only after
  testing

## Responsible Disclosure

We follow a coordinated disclosure process. We ask that you allow us
reasonable time to patch and notify affected stakeholders before any
public disclosure.
