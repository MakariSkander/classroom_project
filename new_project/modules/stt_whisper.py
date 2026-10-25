import whisper

model = whisper.load_model("small")

def transcribe_audio(file_path):
    print("[STT] Transcribing...")
    result = model.transcribe(file_path)
    return result.get("text", "").strip()
