from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulated wallet data (for demo purposes)
wallet = {
    "balance": 1000.0  # starting balance
}

@app.route('/')
def home():
    return "Wallet Management System is running!"

@app.route('/wallet', methods=['GET'])
def get_wallet_balance():
    return jsonify({
        "balance": wallet['balance']
    })

@app.route('/wallet/add', methods=['POST'])
def add_funds():
    data = request.get_json()
    amount = data.get('amount', 0)
    if amount <= 0:
        return jsonify({"error": "Please provide a valid amount greater than 0"}), 400
    
    wallet['balance'] += amount
    return jsonify({
        "message": f"Added {amount} to wallet",
        "new_balance": wallet['balance']
    })

if __name__ == "__main__":
    app.run(debug=True)
