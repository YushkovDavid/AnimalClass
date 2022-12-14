class Giraffe:

    def __init__(self, name, dayWeightEat, age):
        self.name = name
        self.dayWeightEat = dayWeightEat
        self.__age = age
        self._type = "Жираф"
        self.biome = "Тропики"
        self.area = 50
        self.foodTypes = ["Сено", "Фрукты", "Листва"]
        self.__kogoest = "Веган"

    def DoSound(self):
        print(self.name, ": Привет, я", self._type)

    def Eat(self, foodTypes):
        if (foodTypes in self.foodTypes):
            print(self.name, ": Спасибо, я покушал", foodTypes)
        else:
            print(self.name, ": Фу, я не ем", foodTypes)

    def Play(self):
        print(self.name, ": Значит играем в копьютер!")
        print("*2 Часа спустя*")
        print("Рашим B!!")

    @property
    def Type(self):
        return "Жираф"

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