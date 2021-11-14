#!/bin/python3
# https://leetcode.com/problems/generate-parentheses/

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []

        def generate(chain: list[str], left_count: int, right_count: int) -> None:
            if left_count > n or right_count > n or right_count > left_count:
                return
            if left_count == right_count == n:
                result.append(''.join(chain))


            generate(chain + ["("], left_count + 1, right_count)
            generate(chain + [")"], left_count, right_count + 1)

        generate([], 0, 0)

        return result

    def generateParenthesis_set(self, n: int) -> list[str]:
        queue = set(["()"])

        nn = 1
        while nn < n:
            nn += 1

            new_queue = set()
            for s in queue:
                for i in range(len(s)):
                    new_s = s[:i] + "()" + s[i:]
                    new_queue.add(new_s)

            queue = new_queue

        return list(queue)

if __name__ == "__main__":
    Solution().generateParenthesis(2)