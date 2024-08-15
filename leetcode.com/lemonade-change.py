#!/bin/python3
# https://leetcode.com/problems/lemonade-change

from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        bill_counter = {5: 0, 10: 0, 20: 0}

        for bill in bills:
            bill_counter[bill] += 1
            change = bill - 5

            while change:
                for denomination in [20, 10, 5]:
                    actioned = False
                    if bill_counter[denomination] and change >= denomination:
                        change -= denomination
                        bill_counter[denomination] -= 1
                        actioned = True
                        break

                if not actioned:
                    return False

        return True


if __name__ == "__main__":

    def test(expected: list[int], bills: list[int]):
        result = Solution().lemonadeChange(bills)
        assert expected == result, f"Expected {expected} but got {result}"

    # test(False, [5, 5, 10, 10, 20])
    test(True, [5, 5, 5, 10, 20])
