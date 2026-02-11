# Deployment Guide — Auracelle Charlie 3
### NATO Demonstration Build | Auracelle AI Governance Labs

---

## Deployment Options

| Method | Best For | Complexity |
|--------|----------|------------|
| Google Colab + ngrok | Live demonstrations, quick spin-up | Low |
| Local development | Development, testing | Low |
| Streamlit Community Cloud | Persistent public demos | Medium |
| Docker (self-hosted) | Institutional deployment | Medium |

---

## 1. Google Colab + ngrok (Primary Demonstration Method)

This is the recommended method for NATO and institutional demonstrations.

### Prerequisites
- Google account with Colab access
- ngrok account with reserved domain (`aiwargame.ngrok.app`)
- API keys (see `.env.example`)

### Steps

1. **Open the notebook** in Google Colab
2. **Run Cell 0** — installs dependencies and configures ngrok auth token
3. **Run Cell 3** — writes all application files to the Colab filesystem
4. **Run Cell 4** — writes `simulation_vertical.html`
5. **Run Cell 5** — writes `pages/20_3D_Influence_Map.py`
6. **Run Cell 6** — launches Streamlit + ngrok tunnel

   ```
   ✅ Tunnel created: https://aiwargame.ngrok.app
   ```

7. **Access**: `https://aiwargame.ngrok.app`
8. **Login**: Password is `charlie2025`

### Session Management
- Colab sessions time out after ~12 hours of inactivity
- Re-run Cells 3–6 to restart after a timeout
- The filesystem resets on each new Colab session; all files are re-written by the notebook

### Updating API Keys in Colab
Edit Cell 10 in the notebook before launching:
```python
os.environ["COMTRADE_SUBSCRIPTION_KEY"] = "your_key"
os.environ["TRADEGOV_API_KEY"] = "your_key"
```

---

## 2. Local Development

### Prerequisites
- Python 3.10 or higher
- pip

### Setup

```bash
# Clone
git clone https://github.com/[your-org]/auracelle-charlie-3.git
cd auracelle-charlie-3

# Virtual environment
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

# Dependencies
pip install -r requirements.txt

# Environment variables
cp .env.example .env
# Open .env and fill in your API keys

# Run
streamlit run app.py
```

Open `http://localhost:8501` in your browser.

### Local ngrok Tunnel (optional)
To expose local dev to external reviewers:

```bash
ngrok http --domain=aiwargame.ngrok.app 8501
```

---

## 3. Streamlit Community Cloud

### Prerequisites
- GitHub repository (public or private with Streamlit access)
- Streamlit Community Cloud account

### Steps

1. Push repository to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io/)
3. Click **New app** → select repo → set **Main file path** to `app.py`
4. In **Advanced settings → Secrets**, add:

```toml
[api_keys]
TRADEGOV_API_KEY = "your_key"
COMTRADE_SUBSCRIPTION_KEY = "your_key"
APP_PASSWORD = "charlie2025"
```

5. Deploy

**Note**: The `simulation_vertical.html` file must be committed to the repository. Streamlit Community Cloud cannot run the Colab notebook cells that generate it at runtime.

---

## 4. Docker (Self-Hosted / Institutional)

### Dockerfile

```dockerfile
FROM python:3.11-slim

WORKDIR /app

# System dependencies for geopandas
RUN apt-get update && apt-get install -y \
    libgdal-dev \
    libgeos-dev \
    libproj-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "app.py", \
    "--server.port=8501", \
    "--server.address=0.0.0.0", \
    "--server.headless=true"]
```

### Build & Run

```bash
docker build -t auracelle-charlie3 .

docker run -p 8501:8501 \
  -e APP_PASSWORD=your_secure_password \
  -e TRADEGOV_API_KEY=your_key \
  -e COMTRADE_SUBSCRIPTION_KEY=your_key \
  auracelle-charlie3
```

---

## Port Reference

| Service | Port | Notes |
|---------|------|-------|
| Streamlit | 8501 | Main application |
| FastAPI backend | 8000 | Real-world data API (localhost only) |
| ngrok | — | Tunnel only; no local port |

---

## Troubleshooting

### ngrok tunnel not starting
```bash
# Kill existing ngrok processes
pkill -f ngrok
# Re-run the launch cell
```

### Streamlit session state lost after page refresh
This is expected behaviour in Colab deployments. The session state is
in-memory only. Re-login at `https://aiwargame.ngrok.app`.

### World Bank API returning empty data
The wbgapi library caches data. If indicators return empty:
```python
# In a Colab cell:
import wbgapi as wb
wb.data.DataFrame('NY.GDP.MKTP.CD', ['USA'], time=range(2020, 2025))
```
Check for network connectivity to `api.worldbank.org`.

### `StreamlitSecretNotFoundError`
Ensure you are not importing `st.secrets` directly in any page. The
application uses environment variables (`os.environ`) instead of
`secrets.toml`.

### 3D Influence Map not rendering
The map requires Three.js r128 from the Cloudflare CDN:
`https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js`
Check browser console for CDN load errors.
