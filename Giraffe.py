from BaseAnimale import *
class Giraffe(BaseAnimale):

    def __init__(self, name, dayWeightEat, age):
        super().__init__(name, dayWeightEat, age)
        self._type = "Жираф"
        self.biome = "Тропики"
        self.area = 50
        self.foodTypes = ["Сено", "Фрукты", "Листва"]
        self._kogoest = "Веган"

    def Play(self):
        print(self.name, ": Значит играем в копьютер!")
        print("*2 Часа спустя*")
        print("Рашим B!!")

