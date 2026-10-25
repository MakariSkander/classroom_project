# modules/gps.py
import requests

def get_gps_location():
    """
    Returns approximate (lat, lon).
    Uses IP-based lookup first.
    Falls back to Monastir coordinates if lookup fails.
    """

    # Try real IP → GPS lookup
    try:
        resp = requests.get("https://ipapi.co/json/", timeout=3)
        data = resp.json()

        lat = data.get("latitude")
        lon = data.get("longitude")

        if lat is not None and lon is not None:
            return lat, lon

    except Exception as e:
        print(f"[GPS] Error getting location: {e}")

    # Fallback location (Monastir, Tunisia)
    fallback_lat = 35.7643
    fallback_lon = 10.8113

    print("[GPS] Using fallback location: Monastir")
    return fallback_lat, fallback_lon
