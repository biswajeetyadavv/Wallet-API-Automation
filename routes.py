# app/routes.py

from flask import Flask, request, jsonify
from app.wallet import Wallet

wallet = Wallet()
app = Flask(__name__)

@app.route('/create', methods=['POST'])
def create_user():
    user_id = request.json['user_id']
    return jsonify(message=wallet.create_user(user_id))

@app.route('/add', methods=['POST'])
def add_money():
    user_id = request.json['user_id']
    amount = request.json['amount']
    return jsonify(message=wallet.add_money(user_id, amount))

@app.route('/withdraw', methods=['POST'])
def withdraw_money():
    user_id = request.json['user_id']
    amount = request.json['amount']
    return jsonify(message=wallet.withdraw_money(user_id, amount))

@app.route('/balance/<user_id>', methods=['GET'])
def get_balance(user_id):
    return jsonify(balance=wallet.get_balance(user_id))

@app.route('/transactions/<user_id>', methods=['GET'])
def transactions(user_id):
    return jsonify(transactions=wallet.get_transactions(user_id))
