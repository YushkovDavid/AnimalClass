from BaseAnimale import *
class Elephant(BaseAnimale):

    def __init__(self, name, dayWeightEat, age):
        super().__init__(name, dayWeightEat, age)
        self._type = "Слон"
        self.biome = "Тропики"
        self.area = 50
        self.foodTypes = ["Сено", "Фрукты"]
        self.__kogoest = "Веган"

    def Play(self):
        print(self.name, ": Давай расскажу анекдот")
        otvet = input("Пользователь : ")
        if otvet == "Да" or otvet == "да" or otvet == "давай":
            print(self.name, ": Гроб карлика-оптимиста наполовину полон.")
            print("Пользователь : Ххахаха")
        else:
            print(self.name, ": Ну и ладно(")
