import pyttsx3

# initialize only once
engine = pyttsx3.init()
voices = engine.getProperty('voices')

# Set female voice (Zira for English, index=1 on your system)
engine.setProperty('voice', voices[1].id)

def speak(text: str):
    """Speak a given text using pyttsx3 TTS."""
    engine.say(text)
    engine.runAndWait()
