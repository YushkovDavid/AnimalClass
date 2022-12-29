from Elephant import *
from Penguin import *
from Giraffe import *
from Valier import *


g1 = Giraffe("Виталя", 4, 12)
g1._square = 10


V1 = Valier("QweQwe", "Тропики", 50)
V1.AddAnimal(g1)
V1.EatAnimals("Сено", 5)

