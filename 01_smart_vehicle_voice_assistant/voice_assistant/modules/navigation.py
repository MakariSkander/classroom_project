# modules/navigation.py

import requests

def get_route_steps(origin_lat, origin_lon, dest_lat, dest_lon):
    url = (
        f"http://router.project-osrm.org/route/v1/driving/"
        f"{origin_lon},{origin_lat};{dest_lon},{dest_lat}"
        f"?overview=false&steps=true"
    )

    try:
        data = requests.get(url).json()
        if "routes" not in data:
            return None

        steps = data["routes"][0]["legs"][0]["steps"]
        output = []

        for s in steps:
            maneuver = s.get("maneuver", {})
            instruction = maneuver.get("instruction")
            if not instruction:
                continue
            dist = int(s.get("distance", 0))
            output.append(f"{instruction}, in {dist} meters")

        return output

    except:
        return None
