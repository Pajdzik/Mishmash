#!/bin/python3
# https://leetcode.com/problems/


from typing import List, Optional


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        seen_a = set()
        seen_b = set()
        overlap = 0
        result = [0] * len(A)

        for i in range(len(A)):
            a = A[i]
            b = B[i]

            seen_a.add(a)
            seen_b.add(b)

            if a in seen_b:
                overlap += 1
            if a != b and b in seen_a:
                overlap += 1

            result[i] = overlap

        return result


if __name__ == "__main__":
    pass
