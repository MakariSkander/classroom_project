import ollama
import json

def ask_brain(user_text):
    prompt = f"""
You are a car assistant. Your job is to choose the correct tool.
Return ONLY valid JSON with this structure:

{{
  "tool": "...", 
  "args": {{}}, 
  "response": "..."
}}

Tools:
- navigate      → expects: {{ "destination": "..." }}
- location
- car_control   → expects: {{ "action": "light_on/light_off/read_speed/read_temperature" }}
- none

User command: "{user_text}"
"""

    response = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": prompt}]
    )

    content = response["message"]["content"]

    try:
        return json.loads(content)
    except:
        return {"tool": "none", "args": {}, "response": content}
