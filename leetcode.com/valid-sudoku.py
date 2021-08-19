#!/bin/python3
# https://leetcode.com/problems/valid-sudoku/

def check_rows(board: list[list[str]]) -> bool:
    for i in range(len(board)):
        numbers = set()
        for j in range(len(board)):
            number = board[i][j]
            if number == ".":
                continue
            elif number in numbers:
                return False
            else:
                numbers.add(number)

    return True


def check_columns(board: list[list[str]]) -> bool:
    for i in range(len(board)):
        numbers = set()
        for j in range(len(board)):
            number = board[j][i]
            if number == ".":
                continue
            elif number in numbers:
                return False
            else:
                numbers.add(number)

    return True


def check_squares(board: list[list[str]]) -> bool:
    for i_start in range(0, 8, 3):
        for j_start in range(0, 8, 3):
            numbers = set()

            for i in range(i_start, i_start + 3):
                for j in range(j_start, j_start + 3):
                    number = board[i][j]
                    if number == ".":
                        continue
                    elif number in numbers:
                        return False
                    else:
                        numbers.add(number)

    return True

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        return check_columns(board) and check_rows(board) and check_squares(board)

Solution().isValidSudoku([
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
])