#!/usr/bin/env python3
# https://adventofcode.com/2022/day/6

import io
from collections import Counter

def find_marker(file: io.TextIOWrapper, capacity: int) -> int:
    input = file.readline()
    last_n = list(input[0:capacity])
    counter = Counter(last_n)

    for i in range(4, len(input)):
        c = input[i]
        if len(counter) == capacity:
            return i
        
        last_letter = last_n[i % capacity]
        last_char = counter[last_letter]

        if last_char == 1:
            del counter[last_letter]
        else:
            counter[last_letter] -= 1

        last_n[i % capacity] = c
        counter[c] += 1

    return -1

if __name__ == "__main__":
    input = open("day6.txt", "r")
    result_part1 = find_marker(input, 4)
    print(f'Part 1: {result_part1}')
    input.close()

    input = open("day6.txt", "r")
    result_part2 = find_marker(input, 14)
    print(f'Part 2: {result_part2}')
    input.close()