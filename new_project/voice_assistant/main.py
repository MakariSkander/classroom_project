from modules.recorder import record_audio
from modules.stt import transcribe_audio
from modules.llama_brain import ask_brain
from modules.tools import run_tool
from modules.tts import speak

print("\n=== Car Voice Assistant Started ===\n")

while True:
    print("\n--- Listening... ---")
    audio_path = record_audio()          # record user audio

    text = transcribe_audio(audio_path)  # Whisper STT
    print("You said:", text)

    if text.lower() in ["exit", "quit", "stop"]:
        speak("Goodbye.")
        break

    brain = ask_brain(text)              # LLaMA tool selection
    tool = brain.get("tool")
    args = brain.get("args")
    response = brain.get("response")

    if tool and tool != "none":
        result = run_tool(tool, args)
        speak(result)
    else:
        speak(response)
