# app/wallet.py

class Wallet:
    def __init__(self):
        self.users = {}
        self.transactions = {}

    def create_user(self, user_id):
        if user_id in self.users:
            return "User already exists"
        self.users[user_id] = 0
        self.transactions[user_id] = []
        return "User created"

    def add_money(self, user_id, amount):
        if amount <= 0:
            return "Amount should be greater than zero"
        self.users[user_id] += amount
        self.transactions[user_id].append(f"Credited ₹{amount}")
        return f"₹{amount} added"

    def withdraw_money(self, user_id, amount):
        if amount < 50:
            return "Minimum withdrawal is ₹50"
        if self.users[user_id] < amount:
            return "Insufficient balance"
        self.users[user_id] -= amount
        self.transactions[user_id].append(f"Debited ₹{amount}")
        return f"₹{amount} withdrawn"

    def get_balance(self, user_id):
        return self.users[user_id]

    def get_transactions(self, user_id):
        return self.transactions[user_id]
