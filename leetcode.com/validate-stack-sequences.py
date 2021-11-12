#!/bin/python3
# https://leetcode.com/problems/validate-stack-sequences

class Solution:
    def validateStackSequences(self, pushed: list[int], popped: list[int]) -> bool:
        stack = []
        i = 0

        for x in pushed:
            stack.append(x)

            while stack and i < len(popped) and stack[-1] == popped[i]:
                stack.pop()
                i += 1

        return i == len(popped)

if __name__ == "__main__":
    Solution().validateStackSequences([1,2,3,4,5], [4,5,3,2,1])