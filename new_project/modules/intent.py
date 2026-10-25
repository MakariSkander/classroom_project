def detect_intent(text):
    text = text.lower()

    if "navigate" in text or "go to" in text:
        return "navigate"
    if "speed" in text:
        return "car_speed"
    if "temperature" in text:
        return "car_temp"
    if "light on" in text:
        return "light_on"
    if "light off" in text:
        return "light_off"
    if "where am i" in text:
        return "get_location"

    return "unknown"
