#!/bin/python3
# https://leetcode.com/problems/replace-all-digits-with-characters


class Solution:
    def replaceDigits(self, s: str) -> str:
        res = []
        for i in range(0, len(s), 2):
            letter = chr(ord(s[i]) + int(s[i + 1])) if i + 1 < len(s) else ""
            res.append(s[i])
            res.append(letter)

        return "".join(res)


if __name__ == "__main__":

    def test_solution(s: str, expected: str):
        solution = Solution()
        result = solution.replaceDigits(s)
        assert result == expected, f"{result} != {expected}"

    test_solution("a1c1e1", "abcdef")
    test_solution("a1b2c3d4e", "abbdcfdhe")
