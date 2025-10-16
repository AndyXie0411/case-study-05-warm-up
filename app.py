from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Point to your VM’s public IP
OLLAMA_URL = "http://4.227.19.194:11434/api/generate"

@app.post("/api/chat")
def chat():
    data = request.get_json(silent=True) or {}
    prompt = data.get("prompt", "").strip()

    if not prompt:
        return jsonify({"reply": "(empty prompt)"}), 400
