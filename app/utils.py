import requests
import time
import random


FACT_URL = "https://raw.githubusercontent.com/Val7498/Turtle-facts-json/master/facts.json"
IMAGE_URLS = [
    "https://raw.githubusercontent.com/twitter/twemoji/master/assets/72x72/1f422.png",
    "https://raw.githubusercontent.com/hfg-gmuend/openmoji/master/color/72x72/1F422.png",
]


def _fetch_json(url: str, timeout: float = 5.0) -> dict:
    """Helper to fetch JSON data with basic error handling."""
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
        return response.json()
    except Exception:
        return {}


def get_random_fact() -> str:
    """Return a random turtle fact from the API."""
    data = _fetch_json(FACT_URL)
    facts = data.get("JSON", {}).get("Facts", [])
    if not facts:
        return "Could not load a turtle fact right now."
    return random.choice(facts)


def get_random_image() -> str:
    """Return a URL to a random turtle image."""
    url = random.choice(IMAGE_URLS)
    timestamp = int(time.time())
    return f"{url}?{timestamp}"
