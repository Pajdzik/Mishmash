#!/usr/bin/env python3
# https://adventofcode.com/2022/day/9

from io import TextIOWrapper

def move_head(direction: str, row: int, col: int) -> tuple[int, int]:
    if direction == "R":
        return (row, col + 1)
    elif direction == "L":
        return (row, col - 1)
    elif direction == "U":
        return (row + 1, col)
    elif  direction == "D":
        return (row - 1, col)
    
    raise ValueError()

def move_tail(head_row: int, head_col: int, tail_row: int, tail_col: int) -> tuple[int, int]:
    diff_row = head_row - tail_row
    diff_col = head_col - tail_col

    if abs(diff_row) <= 1 and abs(diff_col) <= 1:
        return (tail_row, tail_col)
    
    move_row = 0 if diff_row == 0 else (-1 if diff_row < 0 else 1)
    move_col = 0 if diff_col == 0 else (-1 if diff_col < 0 else 1)

    return (tail_row + move_row, tail_col + move_col)

def count_moves(input: TextIOWrapper) -> int:
    head_row, head_col = 0, 0
    tail_row, tail_col = 0, 0

    visited = set()

    for line in input:
        direction, steps = line.strip().split()
        for _ in range(int(steps)):
            head_row, head_col = move_head(direction, head_row,  head_col)
            tail_row, tail_col = move_tail(head_row, head_col, tail_row, tail_col)
            visited.add((tail_row, tail_col))
        
    return len(visited)

if __name__ == "__main__":
    input = open("day9.txt", "r")
    result = count_moves(input)
    print(result)
    input.close()
