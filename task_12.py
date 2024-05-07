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
        self._calories = value

    def is_healthy(self) -> bool:
        return self.calories < 200

    def is_delicious(self) -> bool:
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
        return super().is_delicious() and self.flavor != "black licorice"


# Пример использования
jelly_bean = JellyBean("Black Licorice", 100, "black licorice")
print(jelly_bean.name)  # Black Licorice
print(jelly_bean.calories)  # 100
print(jelly_bean.flavor)  # black licorice
print(jelly_bean.is_healthy())  # True
print(jelly_bean.is_delicious())  # False
