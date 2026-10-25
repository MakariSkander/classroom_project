from modules.intent import interpret_command
from modules.tts import speak
from modules.geocode import geocode_place
from modules.gps import get_gps_location
from modules.navigation import get_route_steps

def simulate_assistant(text):
    print(f"🔵 You said: {text}")
    command = interpret_command(text)
    print(f"➡️ Command interpreted: {command}")

    if command == "DRIVING_MODE_ON":
        speak("Driving mode activated.")
    elif command == "DRIVING_MODE_OFF":
        speak("Driving mode deactivated.")
    elif command == "CHECK_LOCATION":
        lat, lon = get_gps_location()
        if lat is None:
            speak("I cannot detect your location.")
        else:
            speak(f"Your location is {lat}, {lon}")
    elif command == "START_NAVIGATION":
        speak("Navigation test: calculating route.")
        dlat, dlon = geocode_place("Berlin Hauptbahnhof")
        lat, lon = get_gps_location()
        if lat and lon:
            steps = get_route_steps(lat, lon, dlat, dlon)
            if steps:
                speak("Route is ready.")
                for s in steps[:3]:
                    speak(s)
    elif command == "LIGHT_ON":
        speak("Turning the light on.")
    elif command == "LIGHT_OFF":
        speak("Turning the light off.")
    elif command == "CHECK_SPEED":
        speak("Speed is 60 km/h.")
    elif command == "CHECK_TEMP":
        speak("Engine temperature is 85 degrees.")
    elif command == "EXIT":
        speak("Goodbye.")
    else:
        speak("Chat response triggered.")

print("=== Simulation Started ===")

with open("test_commands.txt", "r") as f:
    for line in f:
        text = line.strip()
        if text:
            simulate_assistant(text)

print("=== Simulation Finished ===")
