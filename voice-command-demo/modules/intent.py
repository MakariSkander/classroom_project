def interpret_command(text: str) -> str:
    text = text.lower()

    # Driving mode
    if "activate driving mode" in text or "start driving mode" in text:
        return "DRIVING_MODE_ON"

    if "deactivate driving mode" in text or "stop driving mode" in text:
        return "DRIVING_MODE_OFF"

    # Navigation
    if "navigate" in text or "go to" in text or "take me to" in text:
        return "START_NAVIGATION"

    if "where am i" in text or "my location" in text:
        return "CHECK_LOCATION"

    # Controls
    if "light on" in text or "turn on the light" in text:
        return "LIGHT_ON"

    if "light off" in text or "turn off the light" in text:
        return "LIGHT_OFF"

    if "speed" in text:
        return "CHECK_SPEED"

    if "temperature" in text:
        return "CHECK_TEMP"

    # Exit
    if "goodbye" in text or "exit" in text or "quit" in text:
        return "EXIT"

    # Fallback
    return "CHAT"
