lines = list()

with open("data") as FILE:
    lines = [line.strip() for line in FILE.readlines()]


def calc_cards_won(line) -> int:
    body = line.split(":")[1].strip()
    winning, numbers = body.split("|")
    winning = set([int(number)
                  for number in winning.strip().split(" ") if number.isdigit()])
    numbers = set([int(number)
                  for number in numbers.strip().split(" ") if number.isdigit()])

    return len(winning.intersection(numbers))


points = list()

for line in lines:
    won = calc_cards_won(line)
    if won == 0:
        continue
    points.append(2 ** (won - 1))

print("Part 1: ", sum(points))


card_number_to_card_wins = dict()
cards = dict()

for card_number, line in enumerate(lines):
    card_number_to_card_wins[card_number] = calc_cards_won(line)
    cards[card_number] = 1

for card_number, cards_won in card_number_to_card_wins.items():
    if cards_won == 0:
        continue

    for new_card_number in range(card_number + 1, card_number + 1 + cards_won):
        cards[new_card_number] += cards[card_number]

print("Part 2: ", sum(cards.values()))
