def total(liste):
    """ renvoie la somme des éléments d'une liste """
    #if type(liste) == int :
    #    return (liste)

    result : float = 0.0

    for item in liste:
        result += item

    return (result)


class Wallet(object):
    def __init__(self, initial_amount=0):
        self.balance = initial_amount

    def spend_cash(self, amount):
        if self.balance < amount:
            raise InsufficientAmount('Not enough available to spend {}'.format(amount))
        self.balance -= amount

    def add_cash(self, amount):
        self.balance += amount

class InsufficientAmount(Exception):
    pass