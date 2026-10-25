from geopy.geocoders import Nominatim

_geolocator = Nominatim(user_agent="car_voice_assistant")

def geocode_place(place: str):
    """
    Convert a text place (e.g. 'Berlin Hauptbahnhof')
    into (lat, lon) using OpenStreetMap Nominatim.
    """
    if not place:
        return None, None

    try:
        location = _geolocator.geocode(place)
        if location is None:
            return None, None
        return location.latitude, location.longitude
    except Exception as e:
        print(f"[GEOCODE] Error geocoding '{place}': {e}")
        return None, None
