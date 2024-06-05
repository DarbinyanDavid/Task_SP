class Dessert:
    def __init__(self, name: str = '', calories: int = 0):
        self.name = name
        self.calories = int(calories)

    def __get_name(self) -> str:
        return self.__name

    def __set_name(self, name):
        try:
            self.__name = str(name)
        except:
            self.__name = ''

    def __get_calories(self) -> int:
        return self.__calories

    def __set_calories(self, calories):
        try:
            self.__calories = int(calories)
        except:
            self.__calories = 0

    name = property(__get_name, __set_name)
    calories = property(__get_calories, __set_calories)

    def is_healthy(self) -> bool:
        return self.__calories < 200

    @staticmethod
    def is_delicious() -> bool:
        return True


while True:
    try:
        calories = int(input("Введите число калорий : "))
        if calories < 0:
            raise ValueError("Калории не могут быть отрицательными.")
        break  # Если пользователь ввел корректное значение, выходим из цикла
    except ValueError as e:
        print("Пожалуйста, введите правильное целочисленное значение для калорий.")
        print(e)

dessert = Dessert(name=input("Введите название десерта: "), calories=calories)

