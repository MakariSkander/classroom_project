import whisper

whisper_model = whisper.load_model("small")

def transcribe_audio(file_path):
    result = whisper_model.transcribe(file_path)
    return result["text"]
