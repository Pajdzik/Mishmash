#!/bin/python3
# https://leetcode.com/problems/time-needed-to-buy-tickets

class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        result = 0
        while tickets[k] > 0:
            for i, el in enumerate(tickets):
                if el > 0:
                    result += 1
                    tickets[i] -= 1
                if i == k and tickets[k] == 0:
                    break

        return result
