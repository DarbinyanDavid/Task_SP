class WrongNumberOfPlayersError(Exception):
    pass


class NoSuchStrategyError(Exception):
    pass


def rps_game_winner(players: list) -> tuple:
    """
    Функция определяет победителя в игре "Камень-ножницы-бумага".

    :param players: список игроков и их ходов в формате [["игрок1", "ход1"], ["игрок2", "ход2"]]
    :return: имя и ход победителя в формате "игрок ход"
    """

    # Проверка количества игроков
    if len(players) != 2:
        raise WrongNumberOfPlayersError("Неверное количество игроков")

    # Проверка корректности ходов
    for player, move in players:
        if move not in ["R", "P", "S"]:
            raise NoSuchStrategyError("Некорректный ход")

    # Определение победителя
    player1, move1 = players[0]
    player2, move2 = players[1]

    if move1 == move2:
        return player1, move1
    elif move1 == "R" and move2 == "S":
        return player1, move1
    elif move1 == "P" and move2 == "R":
        return player1, move1
    elif move1 == "S" and move2 == "P":
        return player1, move1
    else:
        return player2, move2


# Тесты
try:
    print(rps_game_winner([['player1', 'P'], ['player2', 'S'], ['player3', 'S']]))  # => WrongNumberOfPlayersError
except WrongNumberOfPlayersError:
    print("Ошибка: неверное количество игроков")

try:
    print(rps_game_winner([['player1', 'P'], ['player2', 'A']]))  # => NoSuchStrategyError
except NoSuchStrategyError:
    print("Ошибка: некорректный ход")

print(rps_game_winner([['player1', 'P'], ['player2', 'S']]))  # => 'player2 S'
print(rps_game_winner([['player1', 'P'], ['player2', 'P']]))  # => 'player1 P'
