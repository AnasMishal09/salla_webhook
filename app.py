from flask import Flask, request, jsonify
import requests
import hmac
import hashlib
import os

app = Flask(__name__)

EXTERNAL_API_KEY = os.getenv("API9RQZ301753331276999")
EXTERNAL_API_URL = os.getenv("https://a-api.yokcash.com/api/order")
SALLA_WEBHOOK_SECRET = os.getenv("hello123")

def verify_signature(payload, signature):
    computed = hmac.new(
        SALLA_WEBHOOK_SECRET.encode(),
        payload,
        hashlib.sha256
    ).hexdigest()
    return hmac.compare_digest(computed, signature)

@app.route("/salla-webhook", methods=["POST"])
def salla_webhook():
    raw_body = request.get_data()
    signature = request.headers.get("X-Salla-Signature")

    if not verify_signature(raw_body, signature):
        return "Unauthorized", 401

    salla_data = request.json
    print("✅ Received from Salla:", salla_data)

    headers = {
        "Authorization": f"Bearer {EXTERNAL_API_KEY}",
        "Content-Type": "application/json"
    }
    response = requests.post(EXTERNAL_API_URL, json=salla_data, headers=headers)
    print("➡️ Forwarded to external API:", response.status_code, response.text)

    return jsonify({"status": "forwarded"}), 200

@app.route("/")
def home():
    return "✅ Webhook server is running!", 200

if __name__ == "__main__":
    import os
    app.run(host="0.0.0.0", port=10000)
