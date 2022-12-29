from BaseAnimale import *
class Valier:
    def __init__(self, name, biom, ValierSquare):
        self._name = name
        self._biom = biom
        self._ValierSquare = ValierSquare
        self._Animals = []

    def AddAnimal(self, Animal):

        Flag = True

        #Проверка на биом
        if self._biom not in Animal.biome:
            Flag = False
            print("Не тот биом!")

        #Проверка на площадь
        if self._ValierSquare - self.ZanyatayaSquare() < Animal._square:
            Flag = False
            print("Мало места!")

        #Проверка на тип животного
        if Animal._kogoest == "Хищник":
            for i in self._Animals:
                if i._kogoest != "Веган":
                    if Animal._type != i._type:
                        Flag = False
                        print("Тип хищника животного не совпадает с типом другого животного хищника!")
                        break
                else:
                    Flag = False
                    print("Эти животные не талерантны друг к другу!")
                    break
        else:
            if Animal._kogoest == "Веган":
                for i in self._Animals:
                    if i._kogoest != Animal._kogoest:
                        Flag = False
                        print("Эти животные не талерантны друг к другу!")
                        break

        if Flag:
            self._Animals.append(Animal)
            print("Животное добавлено!")

    def doSound(self):
        for i in self._Animals:
            i.DoSound()

    def DelAnimal(self, Animal):
        self._Animals.remove(Animal)
        print("Животное удвлено.")

    def EatAnimals(self, typeFood, mass):
        n = 0
        for i in self._Animals:
            if typeFood in i._foodTypes:
                if mass >= i.dayWeightEat:
                    i.Eat(typeFood)
                    mass -= i.dayWeightEat
                    n += 1
                else:
                    print(i.name, ":", "Мне не хватило еды покушать(")
            else:
                print(i.name, ":", "Я такое не буду есть!")

        return n

    @property
    def listAnimals(self):
        return self._Animals

    def toString(self):
        str=''
        for i in self._Animals:
            str += i._type + " " + i.name + ","
        return str

    @property
    def plase(self):
        return self._ValierSquare

    def ZanyatayaSquare(self):
        Sq = 0
        for i in self._Animals:
            Sq += i._square
        return Sq

    @property
    def AnimalsCount(self):
        a = str()
        return a
