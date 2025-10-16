from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Point to your VM’s public IP
OLLAMA_URL = "http://4.227.19.194:11434/api/generate"

@app.post("/api/chat")
def chat():
    data = request.get_json()
    prompt = data.get("prompt", "")

    try:
        response = requests.post(OLLAMA_URL, json={"model": "tinyllama", "prompt": prompt})
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500
