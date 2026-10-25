# modules/tools.py

from modules.geocode import geocode_place
from modules.gps import get_gps_location
from modules.navigation import get_route_steps


def run_tool(tool_name: str, args: dict, state: dict):
    tool_name = (tool_name or "").lower()
    args = args or {}

    # === NAVIGATION ===
    if tool_name == "navigate":
        destination = args.get("destination")
        if not destination:
            return "I didn't receive a destination."

        dlat, dlon = geocode_place(destination)
        if dlat is None:
            return f"I could not find {destination}."

        lat, lon = get_gps_location()
        if lat is None:
            return "I cannot detect your current location."

        steps = get_route_steps(lat, lon, dlat, dlon)
        if not steps:
            return f"I could not find a route to {destination}."

        state["current_destination"] = destination

        preview = steps[:5]
        return "Here are the first directions: " + " | ".join(preview)

    # === LOCATION ===
    if tool_name == "location":
        lat, lon = get_gps_location()
        if lat is None:
            return "I cannot detect your location right now."
        return f"Your location is latitude {lat:.3f}, longitude {lon:.3f}."

    # === ALERTS ===
    if tool_name == "alerts":
        lat, lon = get_gps_location()
        if lat is None:
            return "I cannot check alerts because your location is not available."
        return "I have no accident or roadblock alerts for your area."

    # === CAR CONTROL ===
    if tool_name == "car_control":
        action = (args.get("action") or "").lower()

        if action == "light_on":
            return "Turning the light on."

        if action == "light_off":
            return "Turning the light off."

        if action == "read_speed":
            return "The current speed is sixty kilometers per hour."

        if action == "read_temperature":
            return "The engine temperature is eighty five degrees."

        return "Unknown car control action."

    return f"Unknown tool: {tool_name}"
