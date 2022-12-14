from BaseAnimale import *
class Valier:
    def __init__(self, name, biom, square):
        self._name = name
        self._biom = biom
        self._square = square
        self._Animals = []

    def AddAnimal(self, Animal):
        self._Animals.append(Animal)

    def DelAnimal(self, Animal):
        self._Animals.remove(Animal)

    def EatAnimals(self, typeFood):
        for i in self._Animals:
            i.Eat(typeFood)

