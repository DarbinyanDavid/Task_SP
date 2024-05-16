class Dessert:
    def __init__(self, name: str = "", calories: int = 0):
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
        if isinstance(value, int):
            self._calories = value
        else:
            try:
                self._calories = int(value)
            except ValueError:
                raise ValueError("Calories must be an integer")

    def is_healthy(self) -> bool:
        return self.calories < 200

    @staticmethod
    def is_delicious() -> bool:
        return True


# Пример использования
dessert = Dessert()

print(dessert.name)  # Пустая строка, так как значение по умолчанию
print(dessert.calories)  # 0, так как значение по умолчанию
print(dessert.is_healthy())  # True, так как калорийность меньше 200
print(Dessert.is_delicious())  # True, так как любой десерт считается вкусным

# Тестовые команды
dessert = Dessert()
dessert.name = "test_name"
print(dessert.name)
dessert.name = "test_name2"
print(dessert.name)
if dessert.name != "test_name2":
    raise Exception("Setter for name is not working")

dessert.calories = 150
print(dessert.calories)
dessert.calories = 250
print(dessert.calories)
if dessert.calories != 250:
    raise Exception("Setter for calories is not working")

print(dessert.is_delicious())
if not dessert.is_delicious():
    raise Exception("Invalid method result")

print(dessert.is_healthy())
