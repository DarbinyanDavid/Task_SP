class Dessert:
    def __init__(self, name: str, calories: int = 0):
        self._name = None
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

    @staticmethod
    def is_delicious() -> bool:
        return True

# Пример использования
dessert = Dessert(name="Cake", calories=300)

print(dessert.name)  # Cake
print(dessert.calories)  # 300
print(dessert.is_healthy())  # False
print(Dessert.is_delicious())  # True