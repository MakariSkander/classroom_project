import requests

def ask(prompt):
    r = requests.post("http://localhost:11434/api/generate", json={
        "model": "llama3.2:1b",
        "prompt": prompt,
        "stream": False
    })
    print(r.json()["response"])

ask("Hello, how are you?")
