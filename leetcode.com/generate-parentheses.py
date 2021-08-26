#!/bin/python3
# https://leetcode.com/problems/generate-parentheses/

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
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

Solution().generateParenthesis(2)