from BaseAnimale import *
from Giraffe import *
from Penguin import *
from Elephant import *
from Valier import *
import unittest

class Valier_Tests(unittest.TestCase):

    def setUp(self):
        self.valier = Valier("QweQwe", "Тропики", 50)

    def test_AddAnimals(self):
        expected = 1
        g1 = Giraffe("Виталя", 4, 12)
        self.valier.AddAnimal(g1)
        actual = len(self.valier.listAnimals)
        self.assertEqual(expected, actual)

    def test_DelAnimal(self):
        expected = 0
        g1 = Giraffe("Виталя", 4, 12)
        self.valier.AddAnimal(g1)
        self.valier.DelAnimal(g1)
        actual = len(self.valier.listAnimals)
        self.assertEqual(expected, actual)

    def test_AllEatAnimals(self):
        expected = 2
        self.valier.AddAnimal(Giraffe("Виталя", 4, 12))
        self.valier.AddAnimal(Giraffe("Антон", 4, 14))
        actual = self.valier.EatAnimals("Сено", 8)
        self.assertEqual(expected, actual)

    def test_EatAnimal(self):
        expected = 1
        self.valier.AddAnimal(Giraffe("Виталя", 4, 12))
        self.valier.AddAnimal(Giraffe("Антон", 4, 14))
        actual = self.valier.EatAnimals("Сено", 7)
        self.assertEqual(expected, actual)

    def test_Square(self):
        expected = 12
        g1 = Giraffe("Виталя", 4, 15)
        self.valier.AddAnimal(g1)
        g1._square = 12
        actual = self.valier.ZanyatayaSquare()
        self.assertEqual(expected, actual)

    def test_EatOnlyAn(self):
        expected = 1
        g1 = Giraffe("Виталя", 4, 15)
        actual = g1.Eat("Сено")
        self.assertEqual(expected, actual)