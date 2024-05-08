class Dessert:
    def __init__(self, name: str, calories: int = 0):
        self.name = name
        self.calories = calories

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
        if not isinstance(value, int):
            raise TypeError("Должно быть числовое значение.")
        self._calories = value

    def is_healthy(self) -> bool:
        return self.calories < 200

    def is_delicious(self) -> bool:
        return True


class JellyBean(Dessert):
    def __init__(self, name: str = "", calories: int = 0, flavor: str = ""):
        super().__init__(name, calories)
        self.flavor = flavor
        if not isinstance(calories, int):
            raise TypeError("Должно быть числовое значение.")

    @property
    def flavor(self):
        return self._flavor

    @flavor.setter
    def flavor(self, value):
        self._flavor = value

    def is_delicious(self) -> bool:
        return super().is_delicious() and self.flavor != "black licorice"


# Тесты
dessert = JellyBean()

if not issubclass(dessert.__class__, JellyBean):
    raise Exception("Invalid inheritance")

dessert.name = "test_name"
print(dessert.name)

dessert.name = "test_name2"
print(dessert.name)

if dessert.name != "test_name2":
    raise Exception("Setter for name is not working")

dessert.calories = 100
print(dessert.calories)

dessert.calories = 200
print(dessert.calories)

if dessert.calories != 200:
    raise Exception("Setter for calories is not working")

print(dessert.is_delicious())

if not dessert.is_delicious():
    raise Exception("Invalid method result")

dessert.flavor = "test_flavor"
print(dessert.flavor)
print(dessert.is_healthy())
