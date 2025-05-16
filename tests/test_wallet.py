# tests/test_wallet.py

import pytest
from app.wallet import Wallet

@pytest.fixture
def wallet():
    return Wallet()

def test_create_user(wallet):
    assert wallet.create_user("user1") == "User created"

def test_add_money(wallet):
    wallet.create_user("user1")
    assert wallet.add_money("user1", 100) == "₹100 added"

def test_withdraw_money(wallet):
    wallet.create_user("user1")
    wallet.add_money("user1", 200)
    assert wallet.withdraw_money("user1", 100) == "₹100 withdrawn"

def test_withdraw_less_than_min(wallet):
    wallet.create_user("user1")
    wallet.add_money("user1", 500)
    assert wallet.withdraw_money("user1", 40) == "Minimum withdrawal is ₹50"

def test_get_balance(wallet):
    wallet.create_user("user1")
    wallet.add_money("user1", 300)
    assert wallet.get_balance("user1") == 300
