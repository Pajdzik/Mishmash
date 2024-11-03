#!/bin/python3
# https://leetcode.com/problems/hash-divided-string


class Solution:
    def stringHash(self, s: str, k: int) -> str:
        result = []

        for start in range(0, len(s), k):
            substring_sum = 0
            for i in range(start, start + k):
                substring_sum += ord(s[i]) - ord("a")

            hashed_char = chr((substring_sum % 26) + ord("a"))
            result.append(hashed_char)

        return "".join(result)


def main():
    solution = Solution()

    # Test case 1
    s = "abcdef"
    k = 2
    expected = "c"
    assert (
        solution.stringHash(s, k) == expected
    ), f"Test case 1 failed: expected {expected}, got {solution.stringHash(s, k)}"

    # Test case 2
    s = "zzzzzz"
    k = 3
    expected = "z"
    assert (
        solution.stringHash(s, k) == expected
    ), f"Test case 2 failed: expected {expected}, got {solution.stringHash(s, k)}"

    # Test case 3
    s = "abcabcabc"
    k = 3
    expected = "c"
    assert (
        solution.stringHash(s, k) == expected
    ), f"Test case 3 failed: expected {expected}, got {solution.stringHash(s, k)}"

    print("All test cases passed!")


if __name__ == "__main__":
    main()
