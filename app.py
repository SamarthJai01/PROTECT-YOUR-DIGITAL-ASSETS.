import os
import json
import requests
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Replace with your Anthropic API Key or set as environment variable
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "your-api-key-here")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

@app.route("/api/analyze", methods=["POST"])
def analyze():
    data = request.json
    user_input = data.get("input", "")
    
    if not user_input:
        return jsonify({"error": "No input provided"}), 400

    prompt = f"""You are ShieldForge, an AI cybersecurity threat analyzer. Analyze the following input for security threats:

INPUT: "{user_input}"

Analyze it as a cybersecurity expert. Determine if it is:
- PHISHING (fake login pages, credential harvesting, impersonation)
- MALWARE (malicious downloads, ransomware, keyloggers)
- SCAM (fake investment, fraud, social engineering)
- ANOMALY (suspicious behavior, unusual access patterns)
- SAFE (legitimate, no threat detected)

Respond in this EXACT JSON format only, no other text:
{{
  "verdict": "PHISHING|MALWARE|SCAM|ANOMALY|SAFE",
  "severity": "critical|high|medium|low|none",
  "confidence": "XX%",
  "summary": "One sentence summary of the threat or confirmation of safety.",
  "detail": "2-3 sentences explaining what was detected, why it is suspicious (or safe), and what the user should do.",
  "action": "The single most important recommended action (10 words max)"
}}"""

    headers = {
        "x-api-key": ANTHROPIC_API_KEY,
        "anthropic-version": "2023-06-01",
        "content-type": "application/json"
    }

    payload = {
        "model": "claude-3-sonnet-20240229",
        "max_tokens": 1024,
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = requests.post("https://api.anthropic.com/v1/messages", headers=headers, json=payload)
        response.raise_for_status()
        
        result_text = response.json()["content"][0]["text"]
        # Extract JSON from potential Markdown formatting
        clean_json = result_text.replace("```json", "").replace("```", "").strip()
        return jsonify(json.loads(clean_json))
        
    except Exception as e:
        print(f"Error calling Anthropic: {e}")
        return jsonify({"error": "AI analysis failed. Please check your API key and connection."}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
