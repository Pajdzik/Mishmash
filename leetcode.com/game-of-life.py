#!/bin/python3
# https://leetcode.com/problems/game-of-life/

class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        dying = []
        reproducing = []

        def count_live_neighbors(r: int, c: int) -> int:
            count = 0
            for (delta_r, delta_c) in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                if 0 <= r + delta_r < len(board) and 0 <= c + delta_c < len(board[r + delta_r]):
                    if board[r + delta_r][c + delta_c] == 1:
                        count += 1

            return count

        for r in range(len(board)):
            for c in range(len(board[r])):
                live_neighbors = count_live_neighbors(r, c)
                if board[r][c] == 0:
                    if live_neighbors == 3:
                        reproducing.append((r, c))
                else:
                    if live_neighbors < 2 or live_neighbors > 3:
                        dying.append((r, c))

        for (r, c) in dying:
            board[r][c] = 0

        for (r, c) in reproducing:
            board[r][c] = 1

if __name__ == "__main__":
    Solution().gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]])