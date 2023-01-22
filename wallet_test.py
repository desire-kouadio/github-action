from wallet import Wallet, InsufficientAmount
import pytest

@pytest.fixture
def empty_wallet():
    '''Returns a Wallet instance with a zero balance'''
    return Wallet()

@pytest.fixture
def wallet():
    '''Returns a Wallet instance with a balance of 20'''
    return Wallet(20)

# L’avantage de cette méthode est que l’objet wallet est instancié de nouveau à chaque fonction test.

def test_default_initial_amount(empty_wallet):
    assert empty_wallet.balance == 0

def test_setting_initial_amount(wallet):
    assert wallet.balance == 20

def test_wallet_add_cash(wallet):
    wallet.add_cash(80)
    assert wallet.balance == 100

def test_wallet_spend_cash(wallet):
    wallet.spend_cash(10)
    assert wallet.balance == 10

def test_wallet_spend_cash_raises_exception_on_insufficient_amount(empty_wallet):
    with pytest.raises(InsufficientAmount):
        empty_wallet.spend_cash(100)

@pytest.mark.parametrize("earned,spent,expected", [(30, 10, 20), (20, 2, 18)])
def test_transactions(earned, spent, expected):
    """ 
    Cette fonction test part d'un portefeuille de valeur 30, ajoute 10, retire 20 puis vérifie le résultat. 
    Elle fait ensuite pareil avec un portefeuille de 20, auquel elle ajoute 2 puis retire 18.
    """
    my_wallet = Wallet()
    my_wallet.add_cash(earned)
    my_wallet.spend_cash(spent)
    assert my_wallet.balance == expected
