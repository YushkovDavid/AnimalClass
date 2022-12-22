from Elephant import *
from Penguin import *
from Giraffe import *
from Valier import *

g1 = Giraffe("Виталя", 4, 12)
g1._square = 5
g2 = Giraffe("Виталя2", 4, 12)
g2._square = 5

V = Valier("QweQwe", "Тропики", 14)
V.AddAnimal(g1)
V.AddAnimal(g2)
V.EatAnimals("Сено", 8)

