from typing import Dict, List, Callable, Any
from abc import abstractmethod

_position_key = 'position'
_accumulator_key = 'accumulator'


class Instruction:
    _name: str
    _arg1: Any

    @abstractmethod
    def execute(self, memory: Dict[str, int]) -> Dict[str, int]: pass

    @property
    def name(self):
        return self._name

    @property
    def arg(self):
        return self._arg1

    @abstractmethod
    def __str__(self): pass

    @abstractmethod
    def __repr__(self): pass

    def __eq__(self, other):
        if isinstance(other, str):
            return other == self._name
        if not isinstance(other, Instruction):
            return False

        return self.name == other.name

    def __ne__(self, other):
        if isinstance(other, str):
            return other != self._name
        if not isinstance(other, Instruction):
            return True

        return self.name != other.name


class Jmp(Instruction):
    def __init__(self, *args):
        self._arg1 = args[0]
        self._name = 'jmp'

    def execute(self, memory):
        memory[_position_key] += self._arg1
        return memory

    def __str__(self):
        return "Jmp {}".format(self._arg1)

    def __repr__(self):
        return self.__str__()


class Acc(Instruction):
    def __init__(self, *args):
        self._arg1 = args[0]
        self._name = 'acc'

    def execute(self, memory):
        memory[_accumulator_key] += self._arg1
        memory[_position_key] += 1
        return memory

    def __str__(self):
        return "Acc {}".format(self._arg1)

    def __repr__(self):
        return self.__str__()


class Nop(Instruction):
    def __init__(self, *args):
        self._arg1 = 0
        self._name = 'nop'

    def execute(self, memory):
        memory[_position_key] += 1
        return memory

    def __str__(self):
        return "Nop {}".format(self._arg1)

    def __repr__(self):
        return self.__str__()


INSTRUCTIONS = {
    'acc': Acc,
    'nop': Nop,
    'jmp': Jmp
}
