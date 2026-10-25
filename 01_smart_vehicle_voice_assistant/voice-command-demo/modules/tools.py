import json

from modules.geocode import geocode_place
from modules.navigation import get_route_steps
from modules.gps import get_gps_location
from modules.alerts import get_incident_alerts

def run_tool(tool_name, args):
    if tool_name == "navigate":
        dest = args.get("destination")
        dlat, dlon = geocode_place(dest)
        lat, lon = get_gps_location()
        steps = get_route_steps(lat, lon, dlat, dlon)
        return steps

    if tool_name == "location":
        return get_gps_location()

    if tool_name == "alerts":
        lat, lon = get_gps_location()
        return get_incident_alerts(lat, lon)

    return "Unknown tool"
