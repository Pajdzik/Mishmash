#!/bin/python3
# https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals

from collections import Counter
from operator import itemgetter


class Solution:
    def findLeastNumOfUniqueInts(self, arr: list[int], k: int) -> int:
        counter = Counter(arr)
        sorted_count_to_number = sorted(counter.items(), key=itemgetter(1))

        to_be_removed = k
        for [number, count] in sorted_count_to_number:
            if count <= to_be_removed:
                del counter[number]
                to_be_removed -= count
            else:
                break

        return len(counter)


if __name__ == "__main__":
    def check(expected: int, numbers: list[int], k: int):
        s = Solution()
        result = s.findLeastNumOfUniqueInts(numbers, k)
        if result != expected:
            print(f"expected: {expected}, result: {result}")
            assert False

    check(1, [5, 5, 4], 1)
