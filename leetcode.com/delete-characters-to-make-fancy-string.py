#!/bin/python3
# https://leetcode.com/problems/delete-characters-to-make-fancy-string


class Solution:
    def makeFancyString(self, s: str) -> str:
        arr = list(s)

        for i in range(1, len(arr) - 1):
            if arr[i - 1] == arr[i] == arr[i + 1]:
                arr[i - 1] = ""

        return "".join(arr)


if __name__ == "__main__":

    def test(expected: str, s: str):
        solution = Solution()
        result = solution.makeFancyString(s)
        assert result == expected, f"{result=}, {expected=}, {s=}"

    test("leetcode", "leeetcode")
