def connect_dicts(dict1, dict2):
    """
    Соединяет два словаря, значениями ключей в которых являются числа, и возвращает новый словарь по заданным правилам.

    Args:
        dict1 (dict): Первый словарь.
        dict2 (dict): Второй словарь.

    Returns:
        dict: Новый словарь, полученный по правилам.
    """

    # Складываем значения ключей в обоих словарях.
    dict1_sum = sum(dict1.values())
    dict2_sum = sum(dict2.values())

    # Определяем приоритетный словарь.
    if dict1_sum > dict2_sum:
        priority_dict = dict1
        secondary_dict = dict2
    else:
        priority_dict = dict2
        secondary_dict = dict1

    # Создаем новый словарь для хранения результата.
    result = {}

    # Добавляем ключи из приоритетного словаря в результирующий словарь.
    for key, value in priority_dict.items():
        if value >= 10:
            result[key] = value

    # Добавляем ключи из вторичного словаря в результирующий словарь, если они не существуют в приоритетном словаре.
    for key, value in secondary_dict.items():
        if key not in result and value >= 10:
            result[key] = value

    # Сортируем результирующий словарь по значениям ключей в порядке возрастания.
    result = dict(sorted(result.items(), key=lambda item: item[1]))

    # Возвращаем результирующий словарь.
    return result


# Тесты
print(connect_dicts({"a": 2, "b": 12}, {"c": 11, "e": 5}))  # =>
# { "c": 11, "b": 12 }
print (connect_dicts({"a": 13, "b": 9, "d": 11}, {"c": 12, "a": 15}) ) # =>
# { d: 11, "c": 12, "a": 13 }
print (connect_dicts({"a": 14, "b": 12}, {"c": 11, "a": 15}))  # =>
# "c": 11, "b": 12, "a": 15 }
