from Elephant import *
from Penguin import *
from Giraffe import *
from Valier import *


g1 = Giraffe("Виталя", 4, 12)
g1._square = 10
g2 = Giraffe("Виталя1", 6, 12)
g2._square = 10
g3 = Giraffe("Виталя2", 2, 12)
g3._square = 10


V1 = Valier("QweQwe", "Тропики", 50)
V1.AddAnimal(g1)
V1.AddAnimal(g2)
V1.AddAnimal(g3)
V1.EatAnimals("Сено", 10)


#for i in V1.listAnimals:
#    print(i._type, i.name)

