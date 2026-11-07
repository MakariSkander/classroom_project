# 🚗 Smart Vehicle Simulation with Voice Assistant

Classroom prototype of an AI-powered in-car assistant that controls vehicle functions by voice.

**Team:** Skandar Makari, Hamza Benali
**Course:** Projet dans la spécialité, supervised by Mr. Najmedine Bahri (2025)

## How it works

1. The driver speaks into the microphone.
2. **Whisper** converts the speech to text.
3. A local language model (**Llama 3.2 3B**, through `llama-cpp-python`) understands the request and picks an action.
4. The assistant runs the action (vehicle command, navigation to a place, chat).
5. It answers by voice with text-to-speech (**pyttsx3**).

## Embedded architecture (from the project report)

- **Raspberry Pi** running a **Yocto**-based Linux, as the central platform
- **STM32** board with a CAN transceiver, connected to the Raspberry Pi over the **CAN bus**
- Sensors and actuators: DS18B20 (temperature), BME280 (weather), LDR (light), DC motor
- STM32 firmware configured with STM32CubeIDE

The full design, hardware setup and timeline are in [`Smart_Vehicle_Project_Full_Report.pdf`](./Smart_Vehicle_Project_Full_Report.pdf).

## Folder structure

| Folder | Content |
|---|---|
| `voice_assistant/` | Main voice assistant: recording, speech-to-text, LLM "brain", tools, text-to-speech |
| `voice-command-demo/` | Extended demo with navigation (geocoding, GPS, route steps) and intent detection |
| `new_project/` | Tests with Ollama as the local LLM backend |
| `digital-voice-assistant-in-car-main/` | Reference project used for comparison (see credits below) |

## Run the assistant

```bash
cd voice_assistant
pip install -r requirements.txt
python main.py
```

The LLM file (`llama-3.2-3b-instruct.Q4_K_M.gguf`) is not included because of its size. Download it and place it in a `models/` folder.

## Credits

The folder `digital-voice-assistant-in-car-main/` is a copy of the open-source project by M. Moeini, R. Ahmadian and M. Ghatee (Amirkabir University of Technology), used as a reference for in-vehicle voice command classification: [mbnmoeini/digital-voice-assistant-in-car](https://github.com/mbnmoeini/digital-voice-assistant-in-car).
