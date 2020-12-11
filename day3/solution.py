from utils.parse_input import fetch_input
from typing import List, Callable
from utils.timer import time_me, benchmark
from functools import reduce


def part1(field_map: List[str], right: int, down: int) -> int:
    """
    for a map that looks like

    ..#.#..# -->
    .#.##.## -->
    ..##..## -->

    where the '.' is open space and '#' are trees, how many trees will you hit if you kept
    going 3 to the right and one down (starting from the top left). Assume the map repeates
    infinitely to the right but has a bottom row

    :return: int
    """
    row_idx, col_idx = 0, 0
    num_trees = 0
    map_width = len(field_map[0]) - 1
    map_length = len(field_map) - 1
    while True:
        col_idx += right
        row_idx += down
        if row_idx > map_length:
            break

        if col_idx > map_width:
            col_idx = col_idx - (map_width + 1)  # wrap around

        element = field_map[row_idx][col_idx]
        if element == '#':
            num_trees += 1

    return num_trees


@benchmark(100)
def part2(field_map: List[str]) -> int:
    """
    do the same for part 1 but given a whole set of instructions of right and down paths, find
    the product of all the number of trees you would encounter
    """
    inputs = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    ]

    return reduce(lambda x, y: x * y, [1] + [part1(field_map, right=_input[0], down=_input[1]) for _input in inputs])


def main():
    field_map = fetch_input('day3-input.txt')
    print("part 1 solution: {}".format(part1(field_map, right=3, down=1)))
    print("part 2 solution: {}".format(part2(field_map)))


if __name__ == '__main__':
    main()
