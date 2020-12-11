from typing import List, Dict
from functools import reduce


class Bag:
    def __init__(self, color: str, contents: Dict = None):
        self.color = color.strip()
        self.contents = contents if contents else {}  # type: Dict[Bag, int]

    def set_contents(self, contents):
        """
        :type contents: Dict[Bag, int]
        """
        self.contents = contents

    def contains(self, bag) -> bool:
        for b, num in self.contents.items():  # type: Bag, int
            if b == bag:
                return True

            if b.contains(bag):
                return True

        return False

    def num_contains(self) -> int:
        if len(self.contents) == 0:
            return 0

        return reduce(lambda x, y: x + y, [num * (b.num_contains() + 1) for b, num in self.contents.items()])

    def __hash__(self):
        return hash(self.color)

    def __eq__(self, other):
        if not isinstance(other, Bag):
            return False
        return self.color == other.color

    def __ne__(self, other):
        if not isinstance(other, Bag):
            return True
        return self.color != other.color

    def __repr__(self):
        if len(self.contents) == 0:
            return "Bag(color={}, contains: [])".format(self.color)
        s = []
        for b, count in self.contents.items():
            s.append('<{} {}>'.format(count, b.color))

        return "Bag(color={}, contains {}: [{}]))".format(self.color, len(self.contents), ', '.join(s))

    def __str__(self):
        return self.__repr__()
