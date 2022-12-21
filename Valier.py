from BaseAnimale import *
class Valier:
    def __init__(self, name, biom, square):
        self._name = name
        self._biom = biom
        self._ValierSquare = square
        self._Animals = []

    def AddAnimal(self, Animal):
        if self._biom == Animal.biome:
            if len(self._Animals) == 0:
                if self._ValierSquare > self._square:
                    self._Animals.append(Animal)
                    self._ValierSquare -= self._square
                else:
                    print("Мало места!")
            else:
                for i in self._Animals:
                    if Animal._kogoest == i._kogoest and Animal._kogoest == "Хищник":
                        if Animal._type == i._type:
                            if self._ValierSquare > self._square:
                                self._Animals.append(Animal)
                                self._ValierSquare -= self._square
                            else:
                                print("Мало места!")
                        else:
                            print("Незя")
                    else:
                        print("Незя")
                        self._Animals.append(Animal)
        else:
            print("Незя")

    def doSound(self):
        for i in self._Animals:
            i.DoSound()

    def DelAnimal(self, Animal):
        self._Animals.remove(Animal)

    def EatAnimals(self, typeFood, mass):
        for i in self._Animals:
            if typeFood in i._kogoest:
                if mass > i.dayWeightEat:
                    i.Eat(i.dayWeightEat, typeFood)
                    mass -= i.dayWeightEat
                else:
                    print(i.name, ":", "Мне не хватило еды покушать(")
            else:
                print(i.name, ":", "Я такое не буду есть!")

    @property
    def listAnimals(self):
        return self._Animals

    @property
    def plase(self):
        return self._square