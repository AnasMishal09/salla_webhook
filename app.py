from flask import Flask

app = Flask(__name__)

@app.route('https://salla-webhook-7l4u.onrender.com/')
def index():
    return "✅ Flask app is running on Render!"

# ✅ Webhook route for Salla
@app.route('/webhook', methods=['POST'])
def salla_webhook():
    # Log the incoming webhook payload
    data = request.get_json()
    print("✅ Webhook received from Salla:")
    print(data


if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 10000))  # Render usually sets this to 10000
    app.run(host="0.0.0.0", port=port)
