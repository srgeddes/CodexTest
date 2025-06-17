import requests
import time


FACT_URL = "https://catfact.ninja/fact"
CATAAS_URL = "https://cataas.com/cat"


def _fetch_json(url: str, timeout: float = 5.0) -> dict:
    """Helper to fetch JSON data with basic error handling."""
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
        return response.json()
    except Exception:
        return {}


def get_random_fact() -> str:
    """Return a random cat fact from the API."""
    data = _fetch_json(FACT_URL)
    return data.get("fact", "Could not load a cat fact right now.")


def get_random_image() -> str:
    """Return a URL to a random cat image from the API."""
    timestamp = int(time.time())
    return f"{CATAAS_URL}?{timestamp}"
