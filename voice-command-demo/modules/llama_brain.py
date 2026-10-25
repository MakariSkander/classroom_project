from llama_cpp import Llama
import json

MODEL_PATH = "models/llama-3.2-3b-instruct.Q4_K_M.gguf"

llm = Llama(
    model_path=MODEL_PATH,
    n_ctx=4096,
    n_threads=6,
    n_gpu_layers=0,   # set >0 if you have an Nvidia GPU
    verbose=False
)

def ask_brain(user_text: str, state: dict = None):
    if state is None:
        state = {}

    system = f"""
    You are an in-car AI assistant. Always reply in JSON.
    Example:
    {{
      "tool": "navigate" | "location" | "alerts" | "car_control" | "none",
      "args": {{}},
      "state_changes": {{}},
      "response": "..."
    }}
    """

    prompt = f"<s>[INST]{system}\nUser: {user_text}[/INST]"

    output = llm(prompt, max_tokens=256)
    text = output["choices"][0]["text"]

    # Extract JSON
    try:
        start = text.index("{")
        end = text.rindex("}") + 1
        return json.loads(text[start:end])
    except:
        return {"tool": "none", "response": text}
