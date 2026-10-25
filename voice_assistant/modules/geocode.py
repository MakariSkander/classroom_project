# modules/geocode.py

import requests

def geocode_place(place_name: str):
    try:
        response = requests.get(
            "https://nominatim.openstreetmap.org/search",
            params={"q": place_name, "format": "json", "limit": 1},
            headers={"User-Agent": "AI-Driving-Assistant"}
        )
        data = response.json()
        if not data:
            return None, None
        return float(data[0]["lat"]), float(data[0]["lon"])
    except:
        return None, None
