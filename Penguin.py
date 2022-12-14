class Penguin:

    def __init__(self, name, dayWeightEat, age):
        self.name = name
        self.dayWeightEat = dayWeightEat
        self.__age = age
        self._type = "Пинвин"
        self.biome = ["Антарктида", "Южная Америка"]
        self.area = 15
        self.foodTypes = ["Рыба", "Моллюски"]
        self.__kogoest = "Хищник"

    def DoSound(self):
        print(self.name, ": Привет, я", self._type)

    def Eat(self, foodTypes):
        if (foodTypes in self.foodTypes):
            print(self.name, ": Спасибо, я покушал", foodTypes)
        else:
            print(self.name, ": Фу, я не ем", foodTypes)

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

    @property
    def Type(self):
        return "Пинвин"

    @property
    def Age(self):
        return self.__age

    @Age.setter
    def Age(self, value):
        if value is int and value >= 0:
            self.__age = value
        else:
            print("Так нельзя.")

    @property
    def KogoEst(self):
        return self.__kogoest

    @KogoEst.setter
    def KogoEst(self, value):
        if value is str:
            self.__kogoest = value
        else:
            print("Так нельзя.")