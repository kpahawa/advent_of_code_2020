from utils.parse_input import fetch_input
from typing import List, Callable
from utils.timer import time_me, benchmark


class Password:
    def __init__(self, line: str):
        policy, letter, password = line.split()  # type: str, str, str
        self.policy = policy

        letter = letter.strip(':')
        p = policy.split('-')

        self.min, self.max = int(p[0]), int(p[1])
        self.letter = letter
        self.password = password

    def validate_old(self) -> bool:
        occ = 0
        for l in self.password:
            occ += 1 if l == self.letter else 0
        return self.min <= occ <= self.max

    def validate_new(self) -> bool:
        first = self.min - 1
        second = self.max - 1
        if len(self.password) < first:
            return False

        char_in_second_pos = len(self.password) >= second and self.password[second] == self.letter
        char_in_first_pos = self.password[first] == self.letter

        return char_in_first_pos ^ char_in_second_pos


@benchmark
def part1(parsed_inputs: List[str]) -> int:
    """
    Problem: Find all valid passwords from the list of policies, letters and given password
    """
    passwords = [Password(line) for line in parsed_inputs]
    validator: Callable[[Password], bool] = lambda p: p.validate_old()
    return len(list(filter(validator, passwords)))


@benchmark(100)
def part2(parsed_inputs):
    passwords = [Password(line) for line in parsed_inputs]
    validator: Callable[[Password], bool] = lambda p: p.validate_new()
    return len(list(filter(validator, passwords)))


def main():
    parsed_inputs = fetch_input('day2-input.txt')
    print("part 1 solution: {}".format(part1(parsed_inputs)))
    print("part 2 solution proper: {}".format(part2(parsed_inputs)))


def generate_test_input() -> List[str]:
    return [
        '1-3 a: abcde',
        '1-3 b: cdefg',
        '2-9 c: ccccccccc',
    ]


if __name__ == '__main__':
    main()
