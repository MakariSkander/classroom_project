import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np

def record_audio(filename="input.wav", duration=5, fs=16000):
    print("🎤 Recording...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype=np.int16)
    sd.wait()
    write(filename, fs, recording)
    print(f"✅ Saved recording to {filename}")
    return filename
