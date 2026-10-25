# modules/llama_brain.py

import json
from llama_cpp import Llama

# Load local GGUF model
llm = Llama(
    model_path="models/llama-3.2-3b-instruct.Q4_K_M.gguf",
    n_ctx=2048,
    n_threads=6,
)


SYSTEM_PROMPT = """
You are an AI driving assistant.
Your job is to understand natural language and decide which tool to call.

Always respond in pure JSON using exactly this structure:

{
  "tool": "...",
  "args": { ... },
  "state_changes": { ... },
  "response": "..."
}

Rules:
- If a tool is needed, set "tool" to one of:
  ["navigate", "location", "alerts", "car_control"]
- If no tool is needed, set "tool": "none" and put your reply in "response".
- Never output anything outside JSON.
- Never talk outside the JSON.
"""

def ask_brain(user_text: str, state: dict):
    """
    Sends the user message to LLaMA and returns parsed JSON.
    """

    # Full conversation context
    prompt = f"""
SYSTEM:
{SYSTEM_PROMPT}

USER:
{user_text}

CURRENT_STATE:
{json.dumps(state)}
"""

    completion = llm(
        prompt,
        max_tokens=512,
        stop=None,
        temperature=0.2
    )

    raw_output = completion["choices"][0]["text"]
    print("=== RAW LLaMA OUTPUT ===")
    print(raw_output)
    print("=========================")

    # Try parsing JSON
    try:
        data = json.loads(raw_output)
        return data
    except:
        # Fallback
        return {
            "tool": "none",
            "args": {},
            "state_changes": {},
            "response": "Sorry, I could not understand the command."
        }
