#!/bin/python3
# https://leetcode.com/problems/sudoku-solver

board_size = 9
square_size = board_size // 3

class Solution:
    def check_elements(self, elements: list[str]) -> bool:
        used = set()

        for element in elements:
            if element != "." and element in used:
                return False
            else:
                used.add(element)

        return True

    def check_rows(self, board: list[list[str]], row: int) -> bool:
        if not 0 <= row < board_size:
            return False

        return self.check_elements(board[row])

    def check_columns(self, board: list[list[str]], column: int) -> bool:
        if not 0 <= column < board_size:
            return False
        
        column_elements = [ board[x][column] for x in range(board_size)]
        return self.check_elements(column_elements)
    
    def check_squares(self, board: list[list[str]], x: int, y: int) -> bool:
        if not (0 <= x <= board_size // square_size and 0 <= y <= board_size // square_size):
            return False
        
        square_elements = []
        for i in range(square_size * x, square_size * (x + 1)):
            for j in range(square_size * y, square_size * (y + 1)):
                square_elements.append(board[i][j])
        return self.check_elements(square_elements)

    def check_board(self, board: list[list[str]], row: int, column: int, number: str) -> bool:
        board[row][column] = number
        result = self.check_rows(board, row) \
             and self.check_columns(board, column) \
             and self.check_squares(board, row // 3, column // 3)
        board[row][column] = "."
        return result

    def backtrack(self, board: list[list[str]], row: int, column: int) -> bool:
        if row >= board_size:
            return True
        if column == board_size:
            return self.backtrack(board, row + 1, 0)
        if board[row][column] != ".":
            return self.backtrack(board, row, column + 1)

        for i in range(1, 10):
            if self.check_board(board, row, column, str(i)):
                board[row][column] = str(i)
                completed = self.backtrack(board, row, column + 1)
                if completed:
                    return True
                else:
                    board[row][column] = "."

    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.backtrack(board, 0, 0)

Solution().solveSudoku([
    ["5", "3", ".", ".", "7",".",".",".","."],
    ["6", ".", ".", "1", "9","5",".",".","."],
    [".", "9", "8", ".", ".",".",".","6","."],
    ["8", ".", ".", ".", "6",".",".",".","3"],
    ["4", ".", ".", "8", ".","3",".",".","1"],
    ["7", ".", ".", ".", "2",".",".",".","6"],
    [".", "6", ".", ".", ".",".","2","8","."],
    [".", ".", ".", "4", "1","9",".",".","5"],
    [".", ".", ".", ".", "8",".",".","7","9"]])
