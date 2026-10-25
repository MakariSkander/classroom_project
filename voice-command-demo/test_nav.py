from modules.llama_brain import ask_brain
from modules.tools import run_tool
from modules.intent import interpret_command
from modules.geocode import geocode_place
from modules.gps import get_gps_location
from modules.navigation import get_route_steps


def simulate(text, state):
    print(f"\n🔵 User: {text}")

    # FIRST LAYER — RULE-BASED COMMANDS
    cmd = interpret_command(text)
    print(f"➡️  Rule-based command: {cmd}")

    if cmd == "DRIVING_MODE_ON":
        state["driving_mode"] = True
        print("AI: Driving mode activated.")
        return state

    elif cmd == "DRIVING_MODE_OFF":
        state["driving_mode"] = False
        print("AI: Driving mode deactivated.")
        return state

    elif cmd == "START_NAVIGATION":
        print("AI: Navigation requested (Hybrid Mode).")
        # Simulate destination
        dest = "Monastir train station"
        print("AI: Destination:", dest)
        dlat, dlon = geocode_place(dest)
        lat, lon = get_gps_location()
        steps = get_route_steps(lat, lon, dlat, dlon)
        print("AI Navigation Steps:", steps)
        return state

    elif cmd == "LIGHT_ON":
        print("AI: Light ON")
        return state

    elif cmd == "LIGHT_OFF":
        print("AI: Light OFF")
        return state

    elif cmd == "CHECK_SPEED":
        print("AI: Speed is 60 km/h")
        return state

    elif cmd == "CHECK_TEMP":
        print("AI: Engine temperature 85°C")
        return state

    elif cmd == "CHECK_LOCATION":
        lat, lon = get_gps_location()
        print("AI Location:", lat, lon)
        return state

    elif cmd == "EXIT":
        print("AI: Goodbye.")
        return state

    # SECOND LAYER — LLaMA BRAIN
    brain = ask_brain(text)
    print("🧠 Brain output:", brain)

    tool = brain.get("tool", "none")

    if tool == "none":
        print("AI:", brain.get("response"))
        return state

    print(f"🛠 Tool requested: {tool}")

    result = run_tool(tool, brain.get("args", {}), state)
    print("Tool result:", result)

    return state


if __name__ == "__main__":
    state = {"driving_mode": False}

    # Load test commands
    with open("test_hybrid_commands.txt", "r") as f:
        for line in f:
            text = line.strip()
            if text:
                state = simulate(text, state)

    print("\n=== Simulation Finished ===")
    