from utils.parse_input import fetch_input
from typing import List


def part1(parsed_inputs: List[int]) -> int:
    """
    Problem: Find numbers the pairing in a list of numbers which add up to 2020, then return their product
    """
    s = set(parsed_inputs)
    for n in parsed_inputs:
        rem = 2020 - n
        if rem in s:
            return n * rem

    return -1


def part2(parsed_inputs: List[int]) -> int:
    """
    Problem: find 3 numbers in a list where the numbers add up to 2020 and return their product
    """
    s = set(parsed_inputs)
    for i in range(len(parsed_inputs) - 1):
        n = parsed_inputs[i]
        rem = 2020 - n
        for j in range(i, len(parsed_inputs)):
            curr = parsed_inputs[j]
            if (rem - curr) in s:
                return n * curr * (rem - curr)

    return -1


def main():
    parsed_inputs = [int(i) for i in fetch_input('day1-input.txt')]
    print("part 1 solution: {}".format(part1(parsed_inputs)))
    print("part 2 solution: {}".format(part2(parsed_inputs)))


if __name__ == '__main__':
    main()