#!/usr/bin/env python3
# https://adventofcode.com/2022/day/8

from io import TextIOWrapper

def is_visible(trees: list[list[int]], row: int, col: int) -> bool:
    height = trees[row][col]

    if not 0 < row < len(trees) - 1:
        return True
    if not 0 < col < len(trees[row]) - 1:
        return True
    
    is_visible_from_left = max(trees[row][:col]) < height
    is_visible_from_right = max(trees[row][col + 1:]) < height
    is_visible_from_top = max([x[col] for x in trees[:row]]) < height
    is_visible_from_down = max([x[col] for x in trees[row + 1:]]) < height

    return is_visible_from_left \
            or is_visible_from_right \
            or is_visible_from_top \
            or is_visible_from_down

def count_trees(input: TextIOWrapper) -> int:
    count = 0
    trees = [[int(c) for c in list(line.strip())] for line in input]

    for row in range(len(trees)):
        for col in range(len(trees[row])):
            if is_visible(trees, row, col):
                count += 1
    
    return count

if __name__ == "__main__":
    input = open("day8.txt", "r")
    result = count_trees(input)
    print(result)
    input.close()
