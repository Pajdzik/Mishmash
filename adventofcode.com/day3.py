#!/usr/bin/env python3
# https://adventofcode.com/2022/day/3

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

if __name__ == "__main__":
    input = open('day3.txt', 'r')
    result = count_priorities(input)
    print(result)
    input.close()
