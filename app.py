from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Your VM’s public IP (Ollama endpoint)
OLLAMA_URL = "http://4.227.19.194:11434/api/generate"

@app.post("/api/chat")
def chat():
    data = request.get_json(silent=True) or {}
    prompt = data.get("prompt", "").strip()

    if not prompt:
        return jsonify({"reply": "(empty prompt)"}), 400

    # Prepare the request payload for Ollama
    payload = {
        "model": "tinyllama",
        "prompt": prompt,
        "stream": False  # disable streaming so we get one full response
    }

    try:
        # Send the prompt to the TinyLlama model running on your VM
        response = requests.post(OLLAMA_URL, json=payload, timeout=60)
        response.raise_for_status()

        # Extract generated text
        data = response.json()
        reply = data.get("response", "").strip()

        return jsonify({"reply": reply})

    except requests.exceptions.RequestException as e:
        # If there’s a connection or timeout error
        return jsonify({"error": str(e)}), 500
