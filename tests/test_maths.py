# -*- coding: utf-8 -*-
"""
Tests unitaires
"""
from unittest import TestCase, main
from myapp.maths import addition, subtraction


class MathsTest(TestCase):
    """
    Classe qui va contenir nos test unitaires
    """
    def setUp(self):
        """ Méthode qui permet d'initialiser des variables pour nos tests """
        self.a = 25
        self.b = 12

    def test_addition(self):
        """ Test de l'addition """
        self.assertEqual(addition(self.a, self.b), 37)

    def test_subtraction(self):
        """ Test de la soustraction """
        self.assertEqual(subtraction(self.a, self.b), 13)

    def tearDown(self):
        """ Méthode appelée à la fin des tests """
        self.a = None
        self.b = None

if __name__ == '__main__':
    main()
