def coincidence(lst: list, rng: range) -> list:
    """
    Определяет элементы из массива list, значения которого входят в указанный диапазон range.
    Если не передан хотя бы один из параметров, то должен вернуться пустой массив.

    :param lst: исходный список
    :param rng: диапазон для проверки
    :return: список элементов из lst, которые входят в диапазон rng
    """
    if not lst or not rng:
        return []

    result = []
    for item in lst:
        if isinstance(item, (int, float)) and rng.start <= item <= rng.stop:
            result.append(item)
        elif isinstance(item, str) and item.isnumeric() and rng.start <= int(item) <= rng.stop:
            result.append(int(item))

    return sorted(result)  # Отсортировать результат в порядке возрастания

# Тесты
print(coincidence([None, 1, 'foo', 4, 2, 2.5], range(1, 4)))  # => [1, 2, 2.5]
