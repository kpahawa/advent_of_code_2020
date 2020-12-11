from utils.parse_input import fetch_input
from typing import List, Tuple
from utils.timer import time_me, benchmark

_file = 'day9-input.txt'


def has_pair(nums: List[int], to_sum: int) -> bool:
    s = set(nums)
    for n in nums:
        rem = to_sum - n
        if rem in s:
            return True

    return False


def part1(prob_input: List[int], preamble_length=25) -> Tuple[int, int]:
    idx = preamble_length
    while idx < len(prob_input):
        curr = prob_input[idx]
        if not has_pair(prob_input[idx - preamble_length: idx], curr):
            return curr, idx

        idx += 1
    return -1, -1


@benchmark
def part2(prob_input: List[int], preamble_length=25) -> int:
    num, idx = part1(prob_input, preamble_length)
    if idx == -1:
        return -1

    for i in range(idx):
        acc = []
        s = prob_input[i]
        acc.append(s)
        for j in range(i+1, idx):
            s += prob_input[j]
            acc.append(prob_input[j])

            if s == num:
                return max(acc) + min(acc)

    return -1


def test_input() -> str:
    return """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""


def main():
    prob_input = [int(i) for i in fetch_input(_file)]
    ti = [int(i) for i in test_input().split('\n')]
    print("part 1 solution is {}".format(part1(prob_input)))
    print("part 2 solution is {}".format(part2(prob_input)))


if __name__ == '__main__':
    main()
