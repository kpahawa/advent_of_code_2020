from utils.parse_input import fetch_input
from typing import List, Tuple, Dict, Optional
from utils.timer import time_me, benchmark
from functools import reduce


_file = 'day11-input.txt'


def test_input() -> str:
    return """#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##"""


def at(seats: List[str], coord: Tuple[int, int]) -> Optional[str]:
    row, col = coord
    if row < 0 or row >= len(seats):
        return None

    if col < 0 or col >= len(seats[0]):
        return None

    return seats[row][col]


def _get_neighbors(seat_row, seat_col, seats: List[str]) -> List[str]:
    s = []
    for row_diff in [-1, 0, 1]:
        for col_diff in [-1, 0, 1]:
            if row_diff == 0 and col_diff == 0:
                continue
            s.append(at(seats, (seat_row + row_diff, seat_col + col_diff)))

    return s


def _get_visible_neighbors(seat_row, seat_col, seats: List[str]) -> List[str]:
    """
    similar to get_neighbors but in this case, it keeps going in each direction until it hits a seat or the edge
    """
    s = []

    for row_diff in [-1, 0, 1]:
        for col_diff in [-1, 0, 1]:
            if row_diff == 0 and col_diff == 0:
                continue
            srd, scd = seat_row + row_diff, seat_col + col_diff
            potential_seat = at(seats, (srd, scd))
            while potential_seat == '.':
                srd += row_diff
                scd += col_diff
                potential_seat = at(seats, (srd, scd))

            s.append(potential_seat)

    return s


@time_me
def part1(seats: List[str]) -> int:
    while True:
        new_seats = []
        row_changes = False
        for row_idx, row in enumerate(seats):
            new_row = ''
            row_has_change = False
            for col_idx, seat in enumerate(row):
                if seat == '.':
                    new_row += '.'
                    continue

                neighbors = _get_neighbors(row_idx, col_idx, seats)
                token = seat
                if seat == 'L' and all(map(lambda x: x != '#', neighbors)):
                    token = '#'
                    row_has_change = True
                elif seat == '#' and neighbors.count('#') >= 4:
                    token = 'L'
                    row_has_change = True

                new_row += token
            row_changes = row_changes or row_has_change
            new_seats.append(new_row)

        seats = new_seats
        if not row_changes:
            break
    return reduce(lambda x, y: x + y.count('#'), [0] + seats)


def part2(seats: List[str]) -> int:
    while True:
        new_seats = []
        row_changes = False
        for row_idx, row in enumerate(seats):
            new_row = ''
            row_has_change = False
            for col_idx, seat in enumerate(row):
                if seat == '.':
                    new_row += '.'
                    continue

                neighbors = _get_visible_neighbors(row_idx, col_idx, seats)
                token = seat
                if seat == 'L' and all(map(lambda x: x != '#', neighbors)):
                    token = '#'
                    row_has_change = True
                elif seat == '#' and neighbors.count('#') >= 5:
                    token = 'L'
                    row_has_change = True

                new_row += token
            row_changes = row_changes or row_has_change
            new_seats.append(new_row)

        seats = new_seats
        if not row_changes:
            break
    return reduce(lambda x, y: x + y.count('#'), [0] + seats)


def main():
    prob_input = fetch_input(_file)
    ti = test_input().split('\n')

    print("part 1 solution is {}".format(part1(prob_input)))
    print("part 2 solution is {}".format(part2(prob_input)))


if __name__ == '__main__':
    main()
