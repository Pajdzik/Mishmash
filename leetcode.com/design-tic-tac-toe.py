#!/bin/python3
# https://leetcode.com/problems/design-tic-tac-toe/

class TicTacToe:
    def __init__(self, n: int):
        self.finished = False
        self.n = n
        self.board = [ [ None for _ in range(n) ] for _ in range(n) ]

    def move(self, row: int, col: int, player: int) -> int:
        if self.finished:
            return None

        if self.board[row][col] == None:
            self.board[row][col] = player

        result = self.validate(row, col, player)
        if result:
            self.finished = True
            return 1
        else:
            return 0

    def validate(self, row: int, col: int, player: int) -> int:
        return all([ self.board[row][x] == player for x in range(self.n)]) \
            or all([ self.board[x][col] == player for x in range(self.n)]) \
            or all([ self.board[x][x] == player for x in range(self.n)]) \
            or all([ self.board[self.n- x - 1][x] == player for x in range(self.n)]) 


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)