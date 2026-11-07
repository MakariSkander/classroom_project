# 🎓 Classroom Projects

Academic projects completed during my studies, covering embedded systems, AI and C++ programming.

| # | Project | Topics | Tech |
|---|---|---|---|
| 01 | [Smart Vehicle with Voice Assistant](./01_smart_vehicle_voice_assistant/) | Embedded systems, speech recognition, local LLM | Python, Whisper, Llama, Raspberry Pi, STM32, CAN |
| 02 | [Code / Decode String](./02_code_decode_string/) | Character encoding and decoding | C++, Visual Studio |
| 03 | [KNN Classification (KPPV)](./03_correction_kppv/) | Machine learning, k-nearest neighbors, GUI | C++, MFC, Visual Studio |

## 01 · Smart Vehicle with Voice Assistant

Classroom prototype of an in-car voice assistant. The driver speaks a command, the assistant converts it to text (Whisper), understands it with a local language model (Llama 3.2), runs the matching action and answers by voice. The project report describes the embedded architecture: a Raspberry Pi running Yocto Linux that talks to an STM32 board over the CAN bus to control lights and a DC motor and to read temperature, light and humidity sensors.

## 02 · Code / Decode String

C++ console program that encodes each character of a text into a scrambled group of 8 letters, then decodes it back using a letter histogram and bit shifting.

## 03 · KNN Classification (KPPV)

Windows desktop application (MFC) to visualize the k-nearest neighbors algorithm. Click to place training points of two classes, then classify new points with the KNN rule (k = 7). The app can also compute and draw the barycenter of each class.

## Author

Skandar Makari · [GitHub](https://github.com/MakariSkander)
