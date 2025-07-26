from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "✅ Flask app is running on Render!"

@app.route("https://salla-webhook-7l4u.onrender.com/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("✅ Webhook received:")
    print(data)
    return jsonify({"status": "received"}), 200


if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 10000))  # Render usually sets this to 10000
    app.run(host="0.0.0.0", port=port)
