from datetime import datetime, timedelta


def date_in_future(days: int) -> str:

    if not isinstance(days, int):
        return datetime.now().strftime('%d-%m-%Y %H:%M:%S')

    return (datetime.now() + timedelta(days=days)).strftime('%d-%m-%Y %H:%M:%S')


# Тесты
print(date_in_future([]))  # => текущая дата
print(date_in_future(2))  # => текущая дата + 2 дня
