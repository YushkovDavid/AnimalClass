from BaseAnimale import *
from Giraffe import *
from Penguin import *
from Elephant import *
from Valier import *
import unittest

class Valier_Tests(unittest.TestCase):

    def setUp(self):
        self.valier = Valier("QweQwe", "Тропики", 14)

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
