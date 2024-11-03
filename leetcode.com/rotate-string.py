#!/bin/python3
# https://leetcode.com/problems/rotate-string


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        def check(goal_start_index: int):
            for i, el in enumerate(s):
                if goal[(goal_start_index + i) % len(goal)] != el:
                    return False
            return True

        if len(s) != len(goal):
            return False

        gi = 0

        while gi < len(goal):
            if goal[gi] == s[0]:
                match = check(gi)
                if match:
                    return True
            gi += 1  # Increment gi to avoid infinite loop

        return False


def main():
    def test():
        solution = Solution()
        assert solution.rotateString("abcde", "cdeab") == True
        assert solution.rotateString("abcde", "abced") == False
        assert solution.rotateString("aa", "a") == False
        assert solution.rotateString("a", "a") == True
        assert solution.rotateString("", "") == True
        print("All tests passed.")

    test()


if __name__ == "__main__":
    main()
