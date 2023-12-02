from typing import NamedTuple, List


class Round(NamedTuple):
    red_pull: int
    green_pull: int
    blue_pull: int


class Game(NamedTuple):
    game_id: int
    rounds: List[Round]


def parse(line: str) -> Game:
    header, body = line.split(":")

    # TODO
    game_id = int(header.split(" ")[1])

    rounds = list()

    for round_str in body.split(";"):
        red_pull = 0
        green_pull = 0
        blue_pull = 0

        for pull_str in round_str.split(","):
            score, color = pull_str.strip().split(" ")
            score = int(score)

            match color:
                case "red":
                    red_pull = score
                case "green":
                    green_pull = score
                case "blue":
                    blue_pull = score

        rounds.append(Round(red_pull, blue_pull, green_pull))

    return Game(game_id, rounds)


FILE = open("data", "r")
games: List[Game] = [parse(line) for line in FILE]
FILE.close()

RED_MAX = 12
GREEN_MAX = 13
BLUE_MAX = 14

possible_games: List[Game] = list()

for game in games:
    possible = True

    for round in game.rounds:
        if round.red_pull > RED_MAX or round.green_pull > GREEN_MAX or round.blue_pull > BLUE_MAX:
            possible = False
            break

    if possible:
        possible_games.append(game)

print("Part 1: ", sum([game.game_id for game in possible_games]))

powers = list()

for game in games:
    min_red = 0
    min_green = 0
    min_blue = 0

    for round in game.rounds:
        min_red = max(round.red_pull, min_red)
        min_green = max(round.green_pull, min_green)
        min_blue = max(round.blue_pull, min_blue)

    power = min_red * min_green * min_blue
    powers.append(power)

print("Part 2: ", sum(powers))
