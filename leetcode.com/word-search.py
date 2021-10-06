#!/bin/python3
# https://leetcode.com/problems/word-search/

class Solution:
    def backtrack(self, board: list[list[str]], row: int, column: int, suffix: str) -> bool:
        if len(suffix) == 0:
            return True

        if not 0 <= row < len(board):
            return False

        if not 0 <= column < len(board[row]):
            return False

        if board[row][column] != suffix[0]:
            return False

        board[row][column] = '.'

        for delta_r, delta_c in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            result = self.backtrack(board, row + delta_r, column + delta_c, suffix[1:])
            if result:
                return True
        
        board[row][column] = suffix[0]

        return False
        

    def exist(self, board: list[list[str]], word: str) -> bool:
        for row in range(len(board)):
            for column in range(len(board[0])):
                if board[row][column] == word[0]:
                    result = self.backtrack(board, row, column, word)
                    if result:
                        return True

        return False

# result = Solution().exist(
#     [
#         ["A","B","C","E"],
#         ["S","F","C","S"],
#         ["A","D","E","E"]
#     ],
#     "ABCB")

result = Solution().exist([
    ["C","A","A"],
    ["A","A","A"],
    ["B","C","D"]],
    "AAB")
print(result)