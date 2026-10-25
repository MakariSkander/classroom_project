import whisper
import serial
import sounddevice as sd
import scipy.io.wavfile as wav
import time

# ===================== CONFIG =====================
SERIAL_PORT = "COM13"      # Windows example -> check Device Manager
BAUDRATE = 115200
AUDIO_FILE = "input.wav"
RECORD_SECONDS = 4
SAMPLE_RATE = 16000

# ===================== INIT =====================
model = whisper.load_model("small")
ser = serial.Serial(SERIAL_PORT, BAUDRATE, timeout=1)
time.sleep(2)  # let STM reset

print("[INFO] Ready. Speak...")

# ===================== FUNCTIONS =====================
def record_audio():
    print("[STT] Recording...")
    audio = sd.rec(int(RECORD_SECONDS * SAMPLE_RATE),
                    samplerate=SAMPLE_RATE,
                    channels=1,
                    dtype="int16")
    sd.wait()
    wav.write(AUDIO_FILE, SAMPLE_RATE, audio)
    print("[STT] Recording done")

def transcribe_audio():
    print("[STT] Transcribing...")
    result = model.transcribe(AUDIO_FILE)
    text = result.get("text", "").lower().strip()
    print(f"[STT] Heard: {text}")
    return text

def send_to_stm(cmd):
    print(f"[UART] Sending: {cmd}")
    ser.write((cmd + "\n").encode())

# ===================== MAIN LOOP =====================
while True:
    record_audio()
    text = transcribe_audio()

    if "ticket" in text:
        print("Which guichet do you want? (1, 2 or 3)")

        record_audio()
        answer = transcribe_audio()

        if "one" in answer or "1" in answer:
            send_to_stm("ticket1")
        elif "two" in answer or "2" in answer:
            send_to_stm("ticket2")
        elif "three" in answer or "3" in answer:
            send_to_stm("ticket3")
        else:
            print("[ERROR] Could not understand number")

    time.sleep(1)
