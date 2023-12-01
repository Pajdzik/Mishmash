#!/usr/bin/env python3
# https://adventofcode.com/2022/day/3

from io import TextIOWrapper

def get_priority(c: str) -> int:
    if 'a' <= c <= 'z':
        return ord(c) - ord('a') + 1
    else:
        return ord(c) - ord('A') + 27
    
def get_common_item(backpack: str) -> str:
    half_len = len(backpack) // 2
    first_compartment = set(backpack[:half_len])
    two_compartment = set(backpack[half_len:])

    common = first_compartment.intersection(two_compartment)
    return list(common)[0]

def count_priorities(input) -> int:
    result = 0
    for line in input:
        common_item = get_common_item(line)
        result += get_priority(common_item)
    return result

def count_priorities_part2(input: TextIOWrapper) -> int:
    result = 0

    while input:
        lines = [input.readline().strip() for _ in range(3)]
        line_sets = [set(line) for line in lines]
        common = line_sets[0].intersection(line_sets[1], line_sets[2])
        if not common:
            break
        result += get_priority(list(common)[0])

    return result

if __name__ == "__main__":
    input = open('day3.txt', 'r')
    result_part1 = count_priorities(input)
    print(f'Part1: {result_part1}')
    input.close()

    input = open('day3.txt', 'r')
    result_part2 = count_priorities_part2(input)
    print(f'Part2: {result_part2}')
    input.close()
