from wallet import Wallet, InsufficientAmount
import pytest

@pytest.fixture
def empty_wallet():
    return Wallet()

@pytest.fixture
def wallet():
   return Wallet(20)

def test_default_balance(empty_wallet):
	
	assert empty_wallet.balance == 0

def test_new_wallet():
	wak = Wallet(100)
	assert wak.balance == 100

def test_add_cash(wallet):
	
	wallet.add_cash(90)
	assert wallet.balance == 110

def test_wallet_spend_cash_raises_exception_on_insufficient_amount():
    wallet = Wallet()
    with pytest.raises(InsufficientAmount):
        wallet.spend_cash(100)

@pytest.mark.parametrize("earned,spent,expected", [(30, 10, 20), (20, 2, 18)])
def test_transactions(earned, spent, expected):
    my_wallet = Wallet()
    my_wallet.add_cash(earned)
    my_wallet.spend_cash(spent)
    assert my_wallet.balance == expected
