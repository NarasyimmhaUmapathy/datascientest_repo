from wallet import Wallet, InsufficientAmount
import pytest


def test_default_balance(wallet:Wallet):
	wal = Wallet()
	assert wal.initial_amount == 0

def test_new_wallet(wallet:Wallet):
	wak = Wallet(initial_amount=100)
	assert wak.balance == 100

def test_add_cash(wallet:Wallet):
	wal = Wallet(inital_amount=10)
	wal.add_cash(90)
	assert wal.balance == 100

def test_wallet_spend_cash_raises_exception_on_insufficient_amount():
    wallet = Wallet()
    with pytest.raises(InsufficientAmount):
        wallet.spend_cash(100)
