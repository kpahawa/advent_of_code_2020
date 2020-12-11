from utils.parse_input import fetch_input_raw, fetch_input
from typing import List, Callable, Set, Dict
from utils.timer import time_me, benchmark
from typing import List
from day7.bag_structs import Bag


def test_input() -> str:
    return """shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags."""


@time_me
def part2(bag_list: List[Bag], want='shiny gold') -> int:
    want_bag = Bag(color=want)
    for b in bag_list:
        if b == want_bag:
            return b.num_contains()
    return -1


@time_me
def part1(bag_list: List[Bag], want='shiny gold') -> int:
    want_bag = Bag(color=want)
    return len(list(filter(lambda x: x.contains(want_bag), bag_list)))


def parse_input_naive(problem_input: List[str]) -> List[Bag]:
    bag_lookup = {}  # type: Dict[str, Bag]
    for row in problem_input:
        parent, children = row.strip('.').split('bags contain')  # type: str, str
        parent = parent.strip()
        parent_bag = Bag(color=parent)
        if 'no other' in children:
            bag_lookup[parent] = parent_bag
            continue

        children_bags = {}  # type: Dict[Bag, int]
        for child_bag in children.split(', '):
            count, color = child_bag.strip().replace(' bags', '').replace(' bag', '').split(' ', 1)
            count = int(count)
            color = color.strip()
            b = bag_lookup.get(color, Bag(color=color))
            bag_lookup[color] = b
            children_bags[b] = count

        parent_bag.set_contents(children_bags)
        bag_lookup[parent] = parent_bag

    ret = []
    for bag in bag_lookup.values():
        updated_contents = {}
        for b, count in bag.contents.items():
            updated_contents[bag_lookup.get(b.color)] = count
        bag.set_contents(updated_contents)
        ret.append(bag)
    return ret


def main():
    prob_input = fetch_input('day7-input.txt')

    # Naive implementation
    bag_list = parse_input_naive(prob_input)
    test_bag_list = parse_input_naive(test_input().split('\n'))
    print("part 1 solution is {}".format(part1(bag_list)))
    print("part 1 solution is {}".format(part2(bag_list)))


if __name__ == '__main__':
    main()
