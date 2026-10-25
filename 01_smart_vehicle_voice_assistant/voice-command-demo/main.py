import time
import random

# Old system imports
from modules.recorder import record_audio
from modules.stt import transcribe
from modules.intent import interpret_command
from modules.tts import speak

# Navigation
from modules.geocode import geocode_place
from modules.gps import get_gps_location
from modules.navigation import get_route_steps

# New AI system
from modules.llama_brain import ask_brain
from modules.tools import run_tool


# Simple chat fallback
chat_responses = {
    "how are you": [
        "I'm doing great today, thank you!",
        "I feel good. What about you?",
        "I'm fine, just happy to talk with you."
    ],
    "hello": [
        "Hello there! How can I help?",
        "Hi! Nice to hear your voice.",
        "Hello! What would you like me to do?"
    ]
}

def get_chat_response(text):
    text = text.lower()
    for k, replies in chat_responses.items():
        if k in text:
            return random.choice(replies)
    return None


def main():
    speak("Hello, I am your hybrid AI assistant. You can talk to me any time.")

    driving_mode = False  # Old system safety switch

    while True:
        audio_file = record_audio(duration=5)
        text = transcribe(audio_file)
        if not text:
            continue

        print("🗣 You said:", text)

        # -----------------------------
        # FIRST LAYER: RULE-BASED COMMANDS
        # -----------------------------
        command = interpret_command(text)
        print("🎯 Interpreted command:", command)

        if command == "DRIVING_MODE_ON":
            driving_mode = True
            speak("Driving mode activated.")
            continue

        elif command == "DRIVING_MODE_OFF":
            driving_mode = False
            speak("Driving mode deactivated.")
            continue

        elif command == "START_NAVIGATION":
            if not driving_mode:
                speak("Please activate driving mode first.")
                continue

            speak("Where would you like to go?")
            dest_audio = record_audio(duration=4)
            dest_text = transcribe(dest_audio)

            if not dest_text:
                speak("I didn't catch the destination.")
                continue

            speak(f"Searching for {dest_text}.")
            dlat, dlon = geocode_place(dest_text)

            if dlat is None:
                speak("I could not find that destination.")
                continue

            lat, lon = get_gps_location()
            if lat is None:
                speak("I cannot detect your location.")
                continue

            speak("Calculating route.")
            steps = get_route_steps(lat, lon, dlat, dlon)

            if not steps:
                speak("I could not calculate the route.")
                continue

            speak("Here are the directions.")
            for step in steps:
                speak(step)
            continue

        elif command == "CHECK_LOCATION":
            lat, lon = get_gps_location()
            if lat:
                speak(f"Your current location is lat {lat:.3f}, lon {lon:.3f}.")
            else:
                speak("I cannot detect your location right now.")
            continue

        elif command == "LIGHT_ON":
            speak("Turning the light on.")
            continue

        elif command == "LIGHT_OFF":
            speak("Turning the light off.")
            continue

        elif command == "CHECK_SPEED":
            speak("Current speed is sixty kilometers per hour.")
            continue

        elif command == "CHECK_TEMP":
            speak("Engine temperature is eighty five degrees.")
            continue

        elif command == "EXIT":
            speak("Goodbye!")
            break

        # Chat response (second fallback)
        chat = get_chat_response(text)
        if chat:
            speak(chat)
            continue

        # -----------------------------
        # SECOND LAYER: LLaMA BRAIN
        # -----------------------------
        brain = ask_brain(text)
        print("🧠 Brain:", brain)

        tool = brain.get("tool", "none")

        if tool == "none":
            speak(brain.get("response"))
            continue

        # Tool call
        result = run_tool(tool, brain.get("args", {}))
        speak(str(result))

        time.sleep(0.2)


if __name__ == "__main__":
    main()
