from utils.parse_input import fetch_input_ints
from typing import List, Tuple, Dict
from utils.timer import time_me, benchmark
from functools import reduce


_file = 'day10-input.txt'


def test_input_basic() -> str:
    return """16
10
15
5
1
11
7
19
6
12
4"""


def test_input() -> str:
    return """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""


def part1(prob_input: List[int]) -> int:
    diffs = {1: 0, 2: 0, 3: 0}

    diffs[prob_input[0]] += 1
    for i in range(len(prob_input) - 1):
        diffs[prob_input[i + 1] - prob_input[i]] += 1
    diffs[3] += 1

    return diffs[1] * diffs[3]


def part2(prob_input: List[int]) -> int:
    prob_input = [0] + prob_input
    step_memo = {0: 1}

    for idx, s in enumerate(prob_input):
        for i in range(1, 4):
            prev_num = prob_input[idx-i] if idx - i >= 0 else -1
            if prev_num < 0 or s - prev_num > 3:
                break
            step_memo[s] = step_memo.get(s, 0) + step_memo[prev_num]

    return step_memo[prob_input[-1]]


def main():
    prob_input = fetch_input_ints(_file, sort=True)
    ti = sorted([int(i) for i in test_input().split('\n')])
    tib = sorted([int(i) for i in test_input_basic().split('\n')])

    print("part 1 solution is {}".format(part1(prob_input)))
    print("part 2 solution is {}".format(part2(ti)))


if __name__ == '__main__':
    main()
