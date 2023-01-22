from wallet import Wallet, InsufficientAmount
import unittest , main

class TestWallet(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print(f'==> Starting Test Case')

    @classmethod
    def tearDownClass(cls):
        print(f'==> Test Case Ended')
    
    def test_total(self):
        """ La somme de plusieurs éléments d'une liste doit être correcte """
        with self.subTest():
            somme_total = main.total([1.0, 2.0, 3.0])
            self.assertEqual(somme_total, 6.0)

        with self.subTest():
            self.assertEqual(main.total([4.0, 3.0, 3.0]), 10.0)

    def test_NP(self):
        """ Vérifie que la somme marche avec un nombre négatif et un positif """
        somme_negatif_positif = main.total([1, -1])
        self.assertEqual(somme_negatif_positif, 0)

    def test_NN(self):
        """ Vérifie que la somme marche avec deux négatifs -1 - 1 = -2 """
        somme_negatif_negatif = main.total([-1, -1])
        self.assertEqual(somme_negatif_negatif, -2)

    def test_null(self):
        """ La somme d'une liste vide doit être 0 """
        somme_liste_vide = main.total([])
        self.assertEqual(somme_liste_vide, 0)
    
# python3 -m unittest unittest_test.py -v 