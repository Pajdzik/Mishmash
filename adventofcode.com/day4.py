#!/usr/bin/env python3
# https://adventofcode.com/2022/day/4

from io import TextIOWrapper

def is_included(one_range: tuple[int, int], second_range: tuple[int, int]) -> bool:
    if one_range[0] < second_range[0]:
        return one_range[1] >= second_range[1]
    elif second_range[0] < one_range[0]:
        return second_range[1] >= one_range[1]
    else:
        return True
    
def does_overlap(one_range: tuple[int, int], second_range: tuple[int, int]) -> bool:
    return second_range[0] <= one_range[1] <= second_range[1] \
        or second_range[0] <= one_range[0] <= second_range[1] \
        or one_range[0] <= second_range[1] <= one_range[1] \
        or one_range[0] <= second_range[0] <= one_range[1]

def parse_range(range: str) -> tuple[int, int]:
    start, end = range.split("-")
    return (int(start), int(end))

def parse_ranges(line: str):
    first_range_str, second_range_str = line.split(",")
    first_range = parse_range(first_range_str)
    second_range = parse_range(second_range_str)
    return first_range, second_range

def count_overlaps(input: TextIOWrapper, overlap_logic) -> int:
    result = 0

    for line in input:
        first_range, second_range = parse_ranges(line)
        included = overlap_logic(first_range, second_range)
        if included:
            result += 1
        
    return result

if __name__ == "__main__":
    input = open("day4.txt", "r")
    result_part1 = count_overlaps(input, is_included)
    print(f'Part1: {result_part1}')
    input.close()

    input = open("day4.txt", "r")
    result_part2 = count_overlaps(input, does_overlap)
    print(f'Part2: {result_part2}')
    input.close()
