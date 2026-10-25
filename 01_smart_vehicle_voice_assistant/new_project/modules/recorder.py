import sounddevice as sd
import soundfile as sf

DURATION = 4  # seconds
SAMPLE_RATE = 16000
FILE_PATH = "audio/temp.wav"

def record_audio():
    print("[REC] Recording...")
    audio = sd.rec(int(DURATION * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=1)
    sd.wait()
    sf.write(FILE_PATH, audio, SAMPLE_RATE)
    print("[REC] Saved to", FILE_PATH)
    return FILE_PATH
