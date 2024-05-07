class WrongNumberOfPlayersError(Exception):
    pass


class NoSuchStrategyError(Exception):
    pass


def rps_game_winner(players):
    if len(players) != 2:
        raise WrongNumberOfPlayersError("Неправильное количество игроков")

    strategies = set(['R', 'P', 'S'])
    for player, strategy in players:
        if strategy not in strategies:
            raise NoSuchStrategyError("Несуществующая стратегия")

    player1, strategy1 = players[0]
    player2, strategy2 = players[1]

    if strategy1 == strategy2:
        return f"{player1} {strategy1}"

    if (strategy1 == 'R' and strategy2 == 'S') or \
            (strategy1 == 'S' and strategy2 == 'P') or \
            (strategy1 == 'P' and strategy2 == 'R'):
        return f"{player1} {strategy1}"
    else:
        return f"{player2} {strategy2}"


# Примеры тестов
try:
    print(rps_game_winner([['player1', 'P'], ['player2', 'S'], ['player3', 'S']]))  # => WrongNumberOfPlayersError
except WrongNumberOfPlayersError as e:
    print(e)

try:
    print(rps_game_winner([['player1', 'P'], ['player2', 'A']]))  # => NoSuchStrategyError
except NoSuchStrategyError as e:
    print(e)

print(str(rps_game_winner([['player1', 'P'], ['player2', 'S']])))  # => 'player2 S'
print(str(rps_game_winner([['player1', 'P'], ['player2', 'P']])))  # => 'player1 P'
