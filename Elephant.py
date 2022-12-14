class Elephant:

    def __init__(self, name, dayWeightEat, age):
        self.name = name
        self.dayWeightEat = dayWeightEat
        self.__age = age
        self._type = "Слон"
        self.biome = "Тропики"
        self.area = 50
        self.foodTypes = ["Сено", "Фрукты"]
        self.__kogoest = "Веган"

    def DoSound(self):
        print(self.name, ": Привет, я", self._type)

    def Eat(self, foodTypes):
        if (foodTypes in self.foodTypes):
            print(self.name, ": Спасибо, я покушал", foodTypes)
        else:
            print(self.name, ": Фу, я не ем", foodTypes)

    def Play(self):
        print(self.name, ": Давай расскажу анекдот")
        otvet = input("Пользователь : ")
        if otvet == "Да" or otvet == "да" or otvet == "давай":
            print(self.name, ": Гроб карлика-оптимиста наполовину полон.")
            print("Пользователь : Ххахаха")
        else:
            print(self.name, ": Ну и ладно(")

    @property
    def Type(self):
        return "Слон"

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