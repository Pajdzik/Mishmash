#!/bin/python3
# https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        max_value = float('inf')
        memory = [ max_value for _ in range(amount + 1) ]
        memory[0] = 0

        for coin in coins:
            for max_amount in range(coin, amount + 1):
                memory[max_amount] = min(memory[max_amount], memory[max_amount - coin] + 1)

        result = memory[-1]
        return result if result != max_value else -1

if __name__ == "__main__":
    Solution().coinChange([1,2,5], 11)