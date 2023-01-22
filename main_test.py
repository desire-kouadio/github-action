from main import total 
import pytest 

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

def test_total_raises_exception_on_non_list_arguments():
    """ renvoie une erreur lorsqu'on lui soumet un int """
    with pytest.raises(TypeError):
        total(1)
