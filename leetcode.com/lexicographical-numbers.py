#!/bin/python3
# https://leetcode.com/problems/lexicographical-numbers

from typing import List

# 2 -> [1, 2]
# 13 -> [1,10,11,12,13,2,3,4,5,6,7,8,9]

# [0 -> 9] -> all digits in the order
# [10 - 19] -> [1, 10, 11..., 2, 3...]
# [20 - 29] -> [1, 10, 11..., 2, 20, 21..., 3]
# [100 - 120] -> [1, 10, 100, 11]


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = []

        def start_generating_numbers():
            for i in range(1, 10):
                next_number([i])

        def next_number(digits: List[int]) -> bool:
            number = int("".join([str(d) for d in digits]))
            if number > n:
                return True

            result.append(number)
            if len(result) >= n:
                return True

            for d in range(10):
                should_break = next_number([*digits, d])
                if should_break:
                    break

            return False

        start_generating_numbers()
        return result


if __name__ == "__main__":

    def test(expected: List[int], n: int):
        result = Solution().lexicalOrder(n)
        assert result == expected, f"{result = }, {expected = }"

    test([1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9], 13)
