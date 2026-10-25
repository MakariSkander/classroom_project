def geocode_place(place):
    place = place.lower()

    if "monastir" in place:
        return {"lat": 35.778, "lon": 10.826}

    if "tunis" in place:
        return {"lat": 36.806, "lon": 10.181}

    return None
