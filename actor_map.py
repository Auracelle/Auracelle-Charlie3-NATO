"""
AGPO Data Package — Actor Mapping Utilities
Auracelle Charlie 3 | E-AGPO-HT Framework

Maps simulation actor names to standard codes for external data APIs:
  - ISO 3166-1 alpha-3 (World Bank, most APIs)
  - UN M49 numeric codes (UN Comtrade legacy)
  - Comtrade partner codes
"""

# ── ISO 3166-1 alpha-3 mappings ──────────────────────────────────────────────
# Key: simulation actor name (as used in UI dropdowns and session state)
# Value: ISO3 code for World Bank API (wbgapi)

ACTOR_TO_ISO3: dict[str, str] = {
    # Primary actors
    "United States": "USA",
    "US": "USA",
    "European Union": "EUU",    # World Bank aggregate code for EU
    "EU": "EUU",
    "China": "CHN",
    "CN": "CHN",
    "United Kingdom": "GBR",
    "UK": "GBR",
    "Japan": "JPN",
    "JP": "JPN",
    "India": "IND",
    "IN": "IND",
    "Brazil": "BRA",
    "BR": "BRA",
    "Russia": "RUS",
    "RU": "RUS",
    # Gulf / Middle East
    "Dubai": "ARE",             # Proxy: UAE (no city-level WB code)
    "UAE": "ARE",
    "Qatar": "QAT",
    "Iraq": "IRQ",
    "Israel": "ISR",
    "Saudi Arabia": "SAU",
    # Europe (extended)
    "Belgium": "BEL",
    "Denmark": "DNK",
    "Norway": "NOR",
    "Switzerland": "CHE",
    "Poland": "POL",
    "Ukraine": "UKR",
    "Serbia": "SRB",
    "Turkey": "TUR",
    "Germany": "DEU",
    "France": "FRA",
    # Americas
    "Argentina": "ARG",
    "Paraguay": "PRY",
    "Mexico": "MEX",
    "Canada": "CAN",
    # Arctic / other
    "Greenland": "GRL",
    "Venezuela": "VEN",
    "Indonesia": "IDN",
    "South Korea": "KOR",
    "Australia": "AUS",
    "Singapore": "SGP",
    # International organisations — no WB country code; handled gracefully
    "NATO": None,
    "Global South": None,
    "UN": None,
    "OECD": None,
}


# ── UN M49 numeric codes (for UN Comtrade legacy API) ────────────────────────
ACTOR_TO_M49: dict[str, str | None] = {
    "United States": "842",
    "US": "842",
    "European Union": "97",     # UN Comtrade: EU as reporter
    "EU": "97",
    "China": "156",
    "CN": "156",
    "United Kingdom": "826",
    "UK": "826",
    "Japan": "392",
    "JP": "392",
    "India": "356",
    "IN": "356",
    "Brazil": "76",
    "BR": "76",
    "Russia": "643",
    "RU": "643",
    "Dubai": "784",             # UAE proxy
    "UAE": "784",
    "Qatar": "634",
    "Iraq": "368",
    "Israel": "376",
    "Saudi Arabia": "682",
    "Belgium": "56",
    "Denmark": "208",
    "Norway": "578",
    "Switzerland": "756",
    "Poland": "616",
    "Ukraine": "804",
    "Serbia": "688",
    "Turkey": "792",
    "Germany": "276",
    "France": "250",
    "Argentina": "32",
    "Paraguay": "600",
    "Mexico": "484",
    "Canada": "124",
    "Greenland": "304",
    "Venezuela": "862",
    "Indonesia": "360",
    "South Korea": "410",
    "Australia": "36",
    "Singapore": "702",
    # International organisations
    "NATO": None,
    "Global South": None,
    "UN": None,
    "OECD": None,
}


# ── UN Comtrade partner codes (v2 API) ───────────────────────────────────────
# These may differ from M49 in the new Comtrade v2 API
ACTOR_TO_COMTRADE: dict[str, str | None] = {
    "United States": "842",
    "US": "842",
    "China": "156",
    "CN": "156",
    "United Kingdom": "826",
    "UK": "826",
    "European Union": "97",
    "EU": "97",
    "Japan": "392",
    "JP": "392",
    "India": "356",
    "IN": "356",
    "Brazil": "076",
    "BR": "076",
    "Russia": "643",
    "RU": "643",
    "Dubai": "784",
    "UAE": "784",
    "Qatar": "634",
    "Iraq": "368",
    "Israel": "376",
    "Saudi Arabia": "682",
    "Belgium": "056",
    "Denmark": "208",
    "Norway": "578",
    "Switzerland": "756",
    "Poland": "616",
    "Ukraine": "804",
    "Serbia": "688",
    "Turkey": "792",
    "Germany": "276",
    "France": "250",
    "Argentina": "032",
    "Paraguay": "600",
    "Mexico": "484",
    "Canada": "124",
    "Greenland": "304",
    "Venezuela": "862",
    "Indonesia": "360",
    "South Korea": "410",
    "Australia": "036",
    "Singapore": "702",
    # International organisations
    "NATO": None,
    "Global South": None,
    "UN": None,
    "OECD": None,
}


# ── Reverse lookups ──────────────────────────────────────────────────────────

ISO3_TO_ACTOR: dict[str, str] = {
    v: k for k, v in ACTOR_TO_ISO3.items() if v is not None
}


def actor_to_iso3(actor_name: str) -> str | None:
    """Return ISO3 code for a simulation actor name. Returns None for
    international organisations that lack a WB country code."""
    return ACTOR_TO_ISO3.get(actor_name)


def actor_to_m49(actor_name: str) -> str | None:
    """Return UN M49 numeric code for a simulation actor name."""
    return ACTOR_TO_M49.get(actor_name)


def actor_to_comtrade(actor_name: str) -> str | None:
    """Return UN Comtrade partner code for a simulation actor name."""
    return ACTOR_TO_COMTRADE.get(actor_name)


def iso3_to_actor(iso3: str) -> str | None:
    """Reverse lookup: ISO3 code → simulation actor name."""
    return ISO3_TO_ACTOR.get(iso3)


def get_valid_wb_actors(actor_list: list[str]) -> list[str]:
    """Filter an actor list to those with valid World Bank ISO3 codes."""
    return [a for a in actor_list if ACTOR_TO_ISO3.get(a) is not None]


def get_iso3_list(actor_list: list[str]) -> list[str]:
    """Convert a list of actor names to ISO3 codes, dropping None values."""
    return [ACTOR_TO_ISO3[a] for a in actor_list if ACTOR_TO_ISO3.get(a)]
