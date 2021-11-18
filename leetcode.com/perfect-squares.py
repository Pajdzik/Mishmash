#!/bin/python3
# https://leetcode.com/problems/perfect-squares/

from math import sqrt

class Solution:
    def numSquares(self, n: int) -> int:
        numbers = [ i*i for i in range(1, int(sqrt(n)) + 1) ]

        memory = [ n + 1 ] * (n + 1)
        memory[0] = 0

        for i in range(1, n + 1):
            local_min = i + 1
            for square in numbers:
                if square > i:
                    break
                
                local_min = min(local_min, memory[i - square] + 1)

            memory[i] = local_min

        return memory[-1]

    def numSquares_recursive(self, n: int) -> int:
        numbers = [ i*i for i in range(1, int(sqrt(n)) + 1) ]
        numbers_set = set(numbers)
        cache = {}

        def find_min_squares(k):
            if k in numbers_set:
                return 1

            if k in cache:
                return cache[k]

            minimum = k + 1

            for square in numbers:
                if k < square:
                    break

                local_min = find_min_squares(k - square) + 1
                minimum = min(minimum, local_min)

            cache[k] = minimum
            return minimum

        return find_min_squares(n)

if __name__ == "__main__":
    assert(Solution().numSquares(12) == 3)