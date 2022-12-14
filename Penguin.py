from BaseAnimale import *
class Penguin(BaseAnimale):

    def __init__(self, name, dayWeightEat, age):
        super().__init__(name, dayWeightEat, age)
        self._type = "Пинвин"
        self.biome = ["Антарктида", "Южная Америка"]
        self.area = 15
        self.foodTypes = ["Рыба", "Моллюски"]
        self._kogoest = "Хищник"

    def Play(self):
        print(self.name, ": Давай поиграем в футбол")
        otvet = input("Пользоватль : ")
        if otvet == "Да" or otvet == "да" or otvet == "давай":
            print(self.name, ": Ура!")
            print("Пользователь : *пинает*")
            print(self.name, "ЭЙ! ТЫ ПНУЛ МОЁ ЯЙЦО!!!!")
            print("Пользователь : *убегает*")
        else:
            print(self.name, ": Ну и ладно(")
