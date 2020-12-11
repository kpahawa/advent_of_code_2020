from utils.parse_input import fetch_input
from typing import List, Tuple
from utils.timer import time_me, benchmark
from utils.virutal_machine import VirtualMachine, InfiniteLoopError
from utils.instructions import Instruction, Acc, Jmp, Nop


_file = 'day8-input.txt'


def test_input() -> str:
    return """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""


def _change_instruction_set(index: int, instructions: List[Instruction]) -> Tuple[int, List[Instruction]]:
    s = instructions[:index]
    while index < len(instructions):
        ins = instructions[index]
        if ins == 'acc':
            s.append(ins)
            index += 1
            continue

        if ins == 'nop':  # type: Nop
            s.append(Jmp(ins.arg))
            break
        elif ins == 'jmp':
            s.append(Nop(ins.arg))
            break

    if index + 1 <= len(instructions):
        s.extend(instructions[index + 1:])
    return index + 1, s


@time_me
def part2(instructions: List[str]) -> int:
    vm = VirtualMachine(instructions)
    try:
        vm.execute_instructions(inspect=False)
        return vm.accumulator
    except InfiniteLoopError:
        prev_ins_index = vm.previous_instruction[0]
        print("changing instruction set at pos {}".format(prev_ins_index))
        _, vm.instructions = _change_instruction_set(prev_ins_index, vm.instructions)
        vm.execute_instructions()
        return vm.accumulator


@time_me
def part2_naive(instructions: List[str]) -> int:
    """
    This naive solution changes one instruction at a time until the program works...there's gotta be a smarter way...
    """
    vm = VirtualMachine(instructions)
    initial_instructions = vm.instructions
    i = 0
    while True:
        try:
            vm.execute_instructions(inspect=False)
            break
        except InfiniteLoopError:
            i, new_instructions = _change_instruction_set(i, initial_instructions)
            vm.instructions = new_instructions
            if i >= len(initial_instructions):
                raise IndexError("surpassed total number of instructions possible to change")
    return vm.accumulator


def part1(instructions: List[str]) -> int:
    vm = VirtualMachine(instructions)
    try:
        vm.execute_instructions(inspect=False)
    except InfiniteLoopError as ile:
        print(ile)
        return vm.accumulator
    return vm.accumulator


def main():
    prob_input = fetch_input(_file)
    ti = test_input().split('\n')
    print("part 1 solution is {}".format(part1(prob_input)))
    print("part 2 naive solution is {}".format(part2_naive(prob_input)))
    # print("part 2 solution is {}".format(part2(prob_input)))


if __name__ == '__main__':
    main()
