from modules.gps import get_current_location
from modules.geocode import geocode_place
from modules.navigation import navigate_to

def run_tool(tool, args):
    if tool == "navigate":
        dest = args.get("destination")
        loc = geocode_place(dest)
        if not loc:
            return f"I cannot find {dest}."
        return navigate_to(dest)

    if tool == "location":
        loc = get_current_location()
        return f"Your location is {loc['lat']}, {loc['lon']}."

    if tool == "car_control":
        action = args.get("action")
        if action == "light_on":
            return "Lights turned ON."
        if action == "light_off":
            return "Lights turned OFF."
        if action == "read_speed":
            return "Your speed is 60 km/h."
        if action == "read_temperature":
            return "Engine temperature is 85°C."
        return "Unknown action."

    return "Unknown tool."
