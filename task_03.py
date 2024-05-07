def max_odd(array):
    """
    Определяет максимальный нечетный элемент в списке.
    Возвращает None, если таких элементов нет.

    :param array: исходный список
    :return: максимальный нечетный элемент или None
    """
    max_odd = None
    for item in array:
        if isinstance(item, (int, float)) and item % 2 != 0:
            if max_odd is None or item > max_odd:
                max_odd = item

    return max_odd


# Тесты
print(max_odd([1, 2, 3, 4, 4]))  # => 3
print(max_odd([21.0, 2, 3, 4, 4]))  # => 21
print(max_odd(['ololo', 2, 3, 4, [1, 2], None]))  # => 3
print(max_odd(['ololo', 'fufufu']))  # => None
print(max_odd([2, 2, 4]))  # => None
