from utils.parse_input import fetch_input_raw
from typing import List, Callable
from functools import reduce
from utils.timer import time_me, benchmark
from os.path import expanduser, join
from typing import List

home_dir = expanduser("~")

_base_path = join(home_dir, 'advent_of_code')


def test_input() -> str:
    return """abc

a
b
c

ab
ac

a
a
a
a

b
c

ab
ab
ab
ab"""


@time_me
def part2(groups: List[List[str]]) -> int:
    """
    find occurrences of letters in each group that are repeated for all elements in the group
    ex: groups: [ ['abc', 'ab', 'ad'] , ['ab', 'abc']] --> 1 (a) + 2 (a,b) = 3
    """
    return reduce(lambda x, y: x + y,
                  [len(reduce(lambda set_1, set_2: set_1.intersection(set_2), [set(word) for word in g if word])) for g
                   in groups])


@time_me
def part1(groups: List[List[str]]) -> int:
    """
    find unique occurrences of each letter in each group of strings and find the sum

    ex: groups: [ ['abc', 'ab', 'd'] , ['ab', 'a']] --> 4 (a,b,c,d) + 2 (a,b) = 6
    """
    return sum([len(set([s for word in g for s in word])) for g in groups])


def modify_input(problem_input: str) -> List[List[str]]:
    return [group.split('\n') for group in problem_input.split('\n\n')]


@time_me
def part1_new(input_path: str):
    return sum(
        [
            len(set([s for word in g for s in word])) for g in
            [group.split('\n') for group in open(input_path).read().split('\n\n')]
        ])


@time_me
def part2_new(input_path: str):
    return sum(
        [
            len(reduce(lambda set_1, set_2: set_1.intersection(set_2), [set(word) for word in g if word])) for g in
            [group.split('\n') for group in open(input_path).read().split('\n\n')]
        ])


def main():
    prob_input = fetch_input_raw('day6-input.txt')
    # ti = test_input()
    print("part 1 solution is {}".format(part1(modify_input(prob_input))))
    print("part 2 solution is {}".format(part2(modify_input(prob_input))))

    print(part1_new(join(_base_path, 'day6-input.txt')))
    print(part2_new(join(_base_path, 'day6-input.txt')))


if __name__ == '__main__':
    main()
