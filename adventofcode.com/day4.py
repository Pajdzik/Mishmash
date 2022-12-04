#!/usr/bin/env python3
# https://adventofcode.com/2022/day/4

def is_included(one_range: tuple[int, int], second_range: tuple[int, int]) -> bool:
    if one_range[0] < second_range[0]:
        return one_range[1] >= second_range[1]
    elif second_range[0] < one_range[0]:
        return second_range[1] >= one_range[1]
    else:
        return True
        

def parse_range(range: str) -> tuple[int, int]:
    start, end = range.split("-")
    return (int(start), int(end))

def parse_ranges(line: str):
    first_range_str, second_range_str = line.split(",")
    first_range = parse_range(first_range_str)
    second_range = parse_range(second_range_str)
    return first_range, second_range

def count_overlaps(input) -> int:
    result = 0

    for line in input:
        first_range, second_range = parse_ranges(line)
        included = is_included(first_range, second_range)
        if included:
            result += 1
        
    return result

if __name__ == "__main__":
    input = open("day4.txt", "r")
    result = count_overlaps(input)
    print(result)
    input.close()
