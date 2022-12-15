from Elephant import *
from Penguin import *
from Giraffe import *
from Valier import *

g1 = Penguin("Виталя", 4, 12)
g1._foodTypes = "Мать"
g1.Eat("Мать")

V = Valier()
V.AddAnimal(g1)


