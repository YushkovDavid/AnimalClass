class BaseAnimale:
    def __init__(self, name, dayWeightEat, age):
        self.name = name
        self.dayWeightEat = dayWeightEat
        self.__age = age

        self._type = ""
        self.biome = ""
        self.area = 0
        self.foodTypes = []
        self.__kogoest = ""

    def DoSound(self):
        print(self.name, ": Привет, я", self._type)

    def Eat(self, foodTypes):
        if (foodTypes in self.foodTypes):
            print(self.name, ": Спасибо, я покушал", foodTypes)
        else:
            print(self.name, ": Фу, я не ем", foodTypes)

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