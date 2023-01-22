from main import total 

def test_total () :
    ## Les use cases 
    """La somme de plusieurs éléments d'une liste doit être correcte"""
    assert(total([1.0, 2.0, 3.0])) == 6.0

    """ Vérifie que la somme marche avec un nombre négatif et un positif"""
    assert total([1, -1]) == 0

    """ Vérifie que la somme marche avec deux négatifs 1 - 1 = 0 """
    assert total([-1, -1]) == -2

    ## Les edge cases :
    """La somme doit être égal à l'unique élément : -1 -1 = -2 """
    assert total([1]) == 1

    """La somme d'une liste vide doit être 0"""
    assert total([]) == 0
