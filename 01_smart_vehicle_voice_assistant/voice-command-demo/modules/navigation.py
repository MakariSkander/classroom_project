# modules/navigation.py
import requests

def get_route_steps(origin_lat, origin_lon, dest_lat, dest_lon):
    url = (
        f"http://router.project-osrm.org/route/v1/driving/"
        f"{origin_lon},{origin_lat};{dest_lon},{dest_lat}"
        f"?overview=false&steps=true"
    )

    try:
        res = requests.get(url, timeout=8).json()
    except Exception as e:
        print("[OSRM] Request error:", e)
        return None

    if "routes" not in res:
        print("[OSRM] No routes found.", res)
        return None

    steps = res["routes"][0]["legs"][0]["steps"]

    instructions = []
    for s in steps:
        maneuver = s.get("maneuver", {})
        text = maneuver.get("instruction")
        
        # Skip steps that have no text instruction
        if not text:
            continue
        
        distance = round(s.get("distance", 0))
        instructions.append(f"{text}, in {distance} meters")

    if not instructions:
        print("[OSRM] No valid steps extracted.")
        return None

    return instructions
