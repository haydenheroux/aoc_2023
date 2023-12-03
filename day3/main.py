from typing import NamedTuple, List
import re

ROWS = 0
COLUMNS = 0


class Symbol(NamedTuple):
    row: int
    column: int
    symbol: str


def get_symbols(lines: List[str]) -> List[Symbol]:
    symbols = list()

    for row, line in enumerate(lines):
        line = line.replace(".", " ")

        for column, symbol in enumerate(line):
            if not symbol.isdigit() and not symbol.isspace():
                symbols.append(Symbol(row, column, symbol))

    return symbols


class Part(NamedTuple):
    row: int
    start_column: int
    number: int
    length: int


def get_parts(lines: List[str]) -> List[Part]:
    parts = list()

    for row, line in enumerate(lines):
        line = line.replace(".", " ")

        part_numbers = {match.start(0): match.group(0)
                        for match in re.finditer(r"\d+", line)}
        for start_column, part_number in part_numbers.items():
            parts.append(Part(row, start_column, int(
                part_number), len(part_number)))

    return parts


def is_good_part(part: Part, symbols: List[Symbol]) -> bool:
    top = max(part.row - 1, 0)
    bottom = min(part.row + 1, ROWS)
    left = max(part.start_column - 1, 0)
    right = min(part.start_column + part.length, COLUMNS)

    for symbol in symbols:
        if symbol.column >= left and symbol.column <= right and symbol.row >= top and symbol.row <= bottom:
            return True

    return False


def get_nearby_parts(symbol: Symbol, parts: List[Part]) -> List[Part]:
    nearby_parts = list()

    for part in parts:
        top = max(part.row - 1, 0)
        bottom = min(part.row + 1, ROWS)
        left = max(part.start_column - 1, 0)
        right = min(part.start_column + part.length, COLUMNS)
        if symbol.column >= left and symbol.column <= right and symbol.row >= top and symbol.row <= bottom:
            nearby_parts.append(part)

    return nearby_parts


with open("data", "r") as FILE:
    lines = FILE.readlines()

    ROWS = len(lines)
    COLUMNS = len(lines[0])

    symbols = get_symbols(lines)
    parts = get_parts(lines)

    parts = [part for part in parts if is_good_part(part, symbols)]

    print("Part 1: ", sum([part.number for part in parts]))

    gear_candidates = [symbol for symbol in symbols if symbol.symbol == "*"]
    print(gear_candidates)

    gears = [get_nearby_parts(gear_candidate, parts)
             for gear_candidate in gear_candidates]
    gears = [gear for gear in gears if len(gear) == 2]

    print("Part 2: ", sum([gear[0].number * gear[1].number for gear in gears]))
