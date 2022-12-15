from BaseAnimale import *
class Valier:
    def __init__(self, name, biom, square):
        self._name = name
        self._biom = biom
        self._square = square
        self._Animals = []

    def AddAnimal(self, Animal):
        if self._biom == Animal.biome:
            if len(self._Animals) == 0:
                self._Animals.append(Animal)
            else:
                for i in self._Animals:
                    if Animal._kogoest == i._kogoest and Animal._kogoest == "Хищник":
                        if Animal._type == i._type:
                            self._Animals.append(Animal)
                        else:
                            print("Незя")
                    else:
                        print("Незя")
                        self._Animals.append(Animal)
        else:
            print("Незя")


    def DelAnimal(self, Animal):
        self._Animals.remove(Animal)

    def EatAnimals(self, typeFood):
        for i in self._Animals:
            i.Eat(typeFood)



