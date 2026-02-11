# Changelog — Auracelle Charlie 3
### Auracelle AI Governance Labs

All notable changes to this project are documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

---

## [3.0.0] — 2026-02-10 | NATO Demonstration Build

### Added
- **3D AlphaFold-Style Influence Map** (enhanced build)
  - 25 country/organisation nodes with full position data
  - 7 policy pressure arrow sets (GDPR, US Export Controls, Belt & Road, AUKUS, UN Ethics, NATO Expansion, Conflict Zone)
  - 6 cultural force wireframe spheres
  - Live stress-test overlay with real-time actor pulsing
  - Country Focus drill-down panel with policy pressure and cultural force breakdown
  - Maximize/restore button for full-viewport 3D view
  - Collapsible sidebar with parameter sliders and animation controls
  - Robust multi-key authentication (`authenticated`, `logged_in`, `is_authenticated`)
- **Red Team Module** (`pages/3_Red_Team_Module.py`)
  - 6 belief-distortion moves: Narrative Entrenchment, Epistemic Distrust, Horizon Collapse, Panic Amplification, Metric Spoofing, Frame Flip
  - Cognition state variables: H, Omega, Lambda, Pi
  - USI (Update Suppression Index) diagnostic
  - Full actor table with derived alpha (learning rate) column
  - Evidence provenance panel with NATO-grade traceability recommendations
- **Extended Actor Roster** (3D map and simulation): Israel, Paraguay, Belgium, Denmark, Ukraine, Serbia, Argentina, Norway, Switzerland, Poland, Global South
- **Enhanced NATO Policy Pressures**: NATO Expansion pressure arc (Ukraine, Poland, Norway, Denmark, Belgium); Conflict Zone arc (Ukraine, Israel, Iraq)
- **Stress-Test Metrics Trace**: Round-by-round Plotly chart (Reward, Risk, Tension, Alignment) in 3D Influence Map page
- **Per-Country Influence Breakdown Table**: Full external pressure and cultural force breakdown with download button (CSV)
- **Round Log Download**: CSV export of full round-by-round stress log from 3D map page
- **`agpo_data/actor_map.py`**: Comprehensive actor → ISO3 / M49 / Comtrade mapping utilities
- **FastAPI Research Backend** (v2.0): WB time-series, Comtrade partner breakdown, sanctions/export controls filter
- **Agentic Negotiation Agents**: Linear Q-approximator with opponent stance inference (conciliatory/neutral/hardline)

### Changed
- **3D Influence Map auth gate**: Now checks three session state keys (`authenticated`, `logged_in`, `is_authenticated`) to prevent spurious logouts
- **Real-World Data Metrics**: API now calls FastAPI backend for robust WB data reshaping; label renamed to "Stress Test"
- **Simulation UI**: Vertical single-column layout for better mobile/tablet display
- **`get_many_indicators`**: Signature fix for `wbgapi` DataFrame output (handles column renaming in newer library versions)

### Fixed
- `StreamlitSecretNotFoundError` on Real-World Data Metrics page (no `secrets.toml` required)
- Actor → ISO3 mapping for Dubai (now correctly maps to UAE `ARE`)
- `None`-safe sanctions count in adjudicator tension calculation

---

## [2.5.0] — 2026-01-15

### Added
- World Bank API integration (wbgapi): GDP, military expenditure, internet penetration
- US Consolidated Screening List (CSL) API integration
- SIPRI military expenditure CSV parser
- External shock injection system with real-world sanctions multiplier
- Deception detection with power/incentive mismatch scoring
- Real-World Data Metrics dashboard (tabs: Economic Indicators, Export Controls, Event History, Batch Evaluation)
- INSTRUCTIONS and Cognitive Science Mechanics page (E-AGPO-HT explainer)
- Agentic AI Demo page (self-contained multi-actor RL environment)

### Changed
- Adjudicator now incorporates real-world military expenditure factor in tension index
- Shock event system marks whether shock was triggered by sanctions data

---

## [2.0.0] — 2025-11-01

### Added
- Full war gaming HTML/JS simulation interface (single-page application embedded in Streamlit)
- Policy Scenario selector: EU AI Act, US EO, UK Pro-Innovation, China CAC, OECD Principles, Bletchley Declaration
- Country/Actor selector with 20 actors and role assignment
- AI Agentic Adjudicator with tension index, confidence scoring, and alignment tracking
- Basic deception detection (consistency scoring)
- Episode length control (1–30 rounds) with stochastic/deterministic toggle
- Round History timeline with narrative generation
- Session statistics panel

---

## [1.0.0] — 2025-08-01

### Added
- Initial Auracelle Charlie prototype
- E-AGPO-HT framework integration (g-GWC, BGC, NOF)
- Basic multi-actor policy comparison (US, EU, China, UK)
- Streamlit login page
- Ngrok tunnel deployment via Google Colab
