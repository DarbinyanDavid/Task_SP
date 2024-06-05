class Dessert:
    def __init__(self, name: str = "", calories: int = 0):
        self._name = name
        self._calories = int(calories)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def calories(self):
        return self._calories

    @calories.setter
    def calories(self, value):
        self._calories = int(value)

    def is_healthy(self) -> bool:
        return self.calories < 200

    @staticmethod
    def is_delicious() -> bool:
        return True


class JellyBean(Dessert):
    def __init__(self, name: str = "", calories: int = 0, flavor: str = ""):
        super().__init__(name, calories)
        self.flavor = flavor

    @property
    def flavor(self):
        return self._flavor

    @flavor.setter
    def flavor(self, value):
        self._flavor = value

    def is_delicious(self) -> bool:
        if self.flavor == "black licorice":
            return False
        return True


while True:
    try:
        calories = int(input("Enter the number of calories: "))
        if calories < 0:
            raise ValueError("Calories cannot be negative.")
        break  # Если пользователь ввел корректное значение, выходим из цикла
    except ValueError as e:
        print("Please enter a valid integer value for calories.")
        print(e)

dessert = Dessert(name=input("Enter the name of the dessert: "), calories=calories)



