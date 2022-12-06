#!/usr/bin/env python3
# https://adventofcode.com/2022/day/5

import io

def parse_stacks(input: io.TextIOWrapper) -> dict[str, list[str]]:
    line = input.readline()
    raw_stacks = []
    while line != "\n":
        raw_stacks.append(line)
        line = input.readline()

    stacks = {}

    for c, stack_id in enumerate(raw_stacks[-1]):
        if not '0' <= stack_id <= '9':
            continue

        stack = []
        for i in range(len(raw_stacks) - 2, -1, -1):
            if raw_stacks[i][c] != " ":
                stack.append(raw_stacks[i][c])

        stacks[stack_id] = stack

    return stacks

def parse_move(command: str) -> tuple[int, str, str]:
    parts = command.split("\n")[0].split(" ")
    return (int(parts[1]), parts[3], parts[5])

def move(stacks: dict[str, list[str]], command: str) -> None:
    how_many, from_stack, to_stack = parse_move(command)

    for _ in range(how_many):
        el = stacks[from_stack].pop()
        stacks[to_stack].append(el)

def get_stack_tops(input: io.TextIOWrapper) -> str:
    stacks = parse_stacks(input)

    for line in input:
        move(stacks, line)

    result = [stack[-1] for stack in stacks.values()]
    return "".join(result)

if __name__ == "__main__":
    input = open("day5.txt", "r")
    result = get_stack_tops(input)
    print(result)
    input.close()