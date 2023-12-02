FILE = open("data", "r")

RED_MAX = 12
GREEN_MAX = 13
BLUE_MAX = 14

possible_game_ids = list()

for game in FILE:
    game_and_all_rounds = game.split(":")
    game = game_and_all_rounds[0]
    all_rounds = game_and_all_rounds[1]

    game_id = game.split(" ")[1]

    possible_rounds = 0

    rounds = all_rounds.split(";")
    for round in rounds:
        reds = 0
        greens = 0
        blues = 0

        pulls = round.split(",")
        for pull in pulls:
            score_and_color = pull.strip().split(" ")

            score = int(score_and_color[0])
            color = score_and_color[1]

            if color == "red":
                reds += score
            elif color == "green":
                greens += score
            elif color == "blue":
                blues += score

        if reds <= RED_MAX and greens <= GREEN_MAX and blues <= BLUE_MAX:
            possible_rounds += 1

    if possible_rounds == len(rounds):
        possible_game_ids.append(int(game_id))

print("Part 1: ", sum(possible_game_ids))

powers = list()

FILE = open("data", "r")

for game in FILE:
    game_and_all_rounds = game.split(":")
    game = game_and_all_rounds[0]
    all_rounds = game_and_all_rounds[1]

    game_id = game.split(" ")[1]

    red_max = 0
    green_max = 0
    blue_max = 0

    rounds = all_rounds.split(";")
    for round in rounds:

        pulls = round.split(",")
        for pull in pulls:
            score_and_color = pull.strip().split(" ")

            score = int(score_and_color[0])
            color = score_and_color[1]

            if color == "red":
                red_max = max(score, red_max)
            elif color == "green":
                green_max = max(score, green_max)
            elif color == "blue":
                blue_max = max(score, blue_max)

    powers.append(red_max * blue_max * green_max)

print("Part 2: ", sum(powers))
