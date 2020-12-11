from typing import Dict, List, Union, Tuple, Optional
from utils.instructions import Instruction, INSTRUCTIONS


class InfiniteLoopError(RuntimeError):
    pass


class VirtualMachine:
    _position_key = 'position'
    _accumulator_key = 'accumulator'
    _instruction_key = 'instruction'

    def __init__(self, instruction_set: List[str]):
        self.instructions = self.compile(instruction_set)
        self.memory = {
            self._position_key: 0,
            self._accumulator_key: 0,
        }
        self.visited = set()
        self.previous_instruction: Tuple[int, Optional[Instruction]] = (0, None)

    def initialize_state(self):
        self.memory = {
            self._position_key: 0,
            self._accumulator_key: 0,
        }
        self.visited = set()
        self.previous_instruction = (0, None)

    def tick(self, inspect=False) -> bool:
        if self.position == len(self.instructions):
            return False

        if self.position in self.visited:
            raise InfiniteLoopError("memory state: {}".format(self.memory))

        instruction_at_pos = self.instructions[self.position]
        self.previous_instruction = (self.position, instruction_at_pos)

        if inspect:
            print("memory state {} | next instruction: {}".format(self.memory, instruction_at_pos))

        self.visited.add(self.position)

        self.memory = instruction_at_pos.execute(self.memory)
        return True

    def execute_instructions(self, max_stack=5000, inspect=False):
        running = True
        num_run = 0
        self.initialize_state()
        while running:
            running = self.tick(inspect)
            num_run += 1
            if num_run > max_stack:
                raise OverflowError("your stack overfloweth.... Memory state: {}".format(self.memory))

    @property
    def position(self):
        return self.memory[self._position_key]

    @property
    def accumulator(self):
        return self.memory[self._accumulator_key]

    @staticmethod
    def compile(instruction_set: List[str]) -> List[Instruction]:
        return [VirtualMachine.parse_instruction(i) for i in instruction_set]

    @staticmethod
    def parse_instruction(instruction: str) -> Instruction:
        ins, amount_str = instruction.split()  # type: str, str
        if not amount_str[1:].isdigit():
            raise RuntimeError("un-parsable amount input")

        amount = int(amount_str.strip())
        kls = INSTRUCTIONS.get(ins)
        if not kls:
            raise RuntimeError("unknown instruction {}".format(ins))

        return kls(amount)
