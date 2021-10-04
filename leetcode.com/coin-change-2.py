#!/bin/python3
# https://leetcode.com/problems/coin-change-2/

class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        memory = [ [ 0 for _ in range(amount + 1) ] for _ in range(len(coins) + 1) ]

        for coin_row in range(len(coins) + 1):
            memory[coin_row][0] = 1

        for coin_row in range(1, len(coins) + 1):
            coin = coins[coin_row - 1]
            for max_amount in range(amount + 1):
                if max_amount >= coin:
                    memory[coin_row][max_amount] = memory[coin_row - 1][max_amount] + memory[coin_row][max_amount - coin]
                else:
                    memory[coin_row][max_amount] = memory[coin_row - 1][max_amount]

        return memory[-1][-1]

if __name__ == "__main__":
    Solution().change(5, [1,2,5])