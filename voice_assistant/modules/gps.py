# modules/gps.py

import requests

def get_gps_location():
    """
    IP-based location fallback for development.
    Replace with hardware GPS later.
    """
    try:
        url = "https://ipinfo.io/json"
        data = requests.get(url).json()
        if "loc" not in data:
            return None, None
        lat, lon = map(float, data["loc"].split(","))
        return lat, lon
    except:
        return None, None
