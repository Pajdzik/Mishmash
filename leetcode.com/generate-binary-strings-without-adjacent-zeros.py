#!/bin/python3
# https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros

from typing import List

# 0     1
# 10   01
# 01


class Solution:
    def validStrings(self, n: int) -> List[str]:
        def generate(m: int, acc: set[str]) -> set[str]:
            if m == 0:
                return acc

            new_acc = set()
            for arr in acc:
                if arr[0] == "1":
                    new_acc.add("0" + arr)
                new_acc.add("1" + arr)

                if arr[-1] == "1":
                    new_acc.add(arr + "0")
                new_acc.add(arr + "1")

            return generate(m - 1, new_acc)

        int_result = generate(n - 1, ["0", "1"])
        str_result = [[str(i) for i in arr] for arr in int_result]
        result = ["".join(arr) for arr in str_result]

        return list(result)


if __name__ == "__main__":

    def test(expected: list[str], n: int):
        result = Solution().validStrings(n)
        assert set(expected) == set(result), f"Expected {expected} but got {result}"

    test(["0", "1"], 1)
    test(["01", "10", "11"], 2)
    test(
        ["010", "011", "101", "110", "111"],
        3,
    )
