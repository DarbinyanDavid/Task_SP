from typing import Dict


def connect_dicts(dict1: Dict[str, int], dict2: Dict[str, int]) -> Dict[str, int]:
    # Суммируем значения ключей в каждом словаре
    sum1 = sum(dict1.values())
    sum2 = sum(dict2.values())

    if sum1 > sum2:
        priority_dict = dict1
        secondary_dict = dict2
    else:
        priority_dict = dict2
        secondary_dict = dict1

    filtered_priority_dict = {key: value for key, value in priority_dict.items() if value >= 10}
    filtered_secondary_dict = {key: value for key, value in secondary_dict.items() if value >= 10}
    combined_dict = {**filtered_priority_dict, **filtered_secondary_dict}

    sorted_dict = dict(sorted(combined_dict.items(), key=lambda item: item[1]))

    return sorted_dict


# Тесты
print(connect_dicts({"a": 2, "b": 12}, {"c": 11, "e": 5}))  # => {"c": 11, "b": 12}
print(connect_dicts({"a": 13, "b": 9, "d": 11}, {"c": 12, "a": 15}))  # => {"d": 11, "c": 12, "a": 13}
print(connect_dicts({"a": 14, "b": 12}, {"c": 11, "a": 15}))  # => {"c": 11, "b": 12, "a": 15}
