from utils.parse_input import fetch_input
from typing import List, Callable
from utils.timer import time_me, benchmark


@benchmark(2000)
def part2(seats: List[str]) -> int:
    seat_pairs = gen_row_cols(seats)
    ids = sorted(gen_ids(seat_pairs))
    for idx, i in enumerate(ids):
        n = ids[idx + 1]
        if n - i == 2:
            return i+1
    return -1


def gen_row_cols(seats: List[str]) -> List[List[int]]:
    binaries = []
    for inputs in seats:
        replaced = inputs.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1')
        row = replaced[:-3]
        col = replaced[-3:]

        binaries.append([int(row, 2), int(col, 2)])
    return binaries


_2_pow_lookups = {0: 1, 1: 2, 2: 4, 3: 8, 4: 16, 5: 32, 6: 64, 7: 128, 8: 256, 9: 512, 10: 1024}


def pow(base, exp) -> int:
    """too slow still..."""
    i = 0
    s = 1
    while i < exp:
        s *= base
        i += 1
    return s


def gen_row_cols_new(seats: List[str]) -> List[List[int]]:
    binaries = []
    for inputs in seats:
        row = 0
        col = 0
        for i in range(10):
            digit = 0 if inputs[i] == 'F' or inputs[i] == 'L' else 1

            if i < 7:
                pos = 6 - i
                row += digit * _2_pow_lookups[pos]  # guaranteed faster than math.pow and `**` operand
            else:
                pos = 2 - (i - 7)
                col += digit * _2_pow_lookups[pos]

        binaries.append([row, col])
    return binaries


def gen_ids(identifiers: List[List[int]]) -> List[int]:
    return [r * 8 + c for r, c in identifiers]


def part1(seats: List[str]) -> int:
    seat_pairs = gen_row_cols_new(seats)
    return max(gen_ids(seat_pairs))


def test_input() -> List[str]:
    return [
        "FBFBBFFRLR",
        "BFFFBBFRRR",
        "FFFBBBFRRR",
        "BBFFBBFRLL"
    ]


def main():
    seats_inputs = fetch_input('day5-input.txt')
    print("part 1 solution: {}".format(part1(seats_inputs)))
    print("part 2 solution: {}".format(part2(seats_inputs)))


if __name__ == '__main__':
    main()
