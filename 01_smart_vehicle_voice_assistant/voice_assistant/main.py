import time

from modules.recorder import record_audio
from modules.stt import transcribe  # current STT (later you can swap to Whisper)
from modules.tts import speak

from modules.llama_brain import ask_brain
from modules.tools import run_tool


def main():
    speak("Hello, I am your AI driving assistant. I am ready when you are.")

    # Global assistant state
    state = {
        "driving_mode": False,
        "current_destination": None,
    }

    while True:
        # 1) Record voice
        audio_path = record_audio(duration=5)

        # 2) STT (for now your existing transcribe; later: Whisper)
        user_text = transcribe(audio_path)
        if not user_text:
            continue

        print("🗣 User:", user_text)

        # 3) Ask the brain what to do
        brain = ask_brain(user_text, state)
        print("🧠 Brain:", brain)

        # Apply state changes
        for key, val in brain.get("state_changes", {}).items():
            state[key] = val

        tool = brain.get("tool", "none")
        args = brain.get("args", {})

        # 4) If no tool → just answer
        if tool == "none":
            response = brain.get("response", "I have nothing to say.")
            speak(response)
            continue

        # 5) Tool call
        tool_result_text = run_tool(tool, args, state)
        print("🛠 Tool result:", tool_result_text)

        # 6) Speak result
        speak(tool_result_text)

        time.sleep(0.2)


if __name__ == "__main__":
    main()
