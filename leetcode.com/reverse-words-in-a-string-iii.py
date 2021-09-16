#!/bin/python3
# https://leetcode.com/problems/reverse-words-in-a-string-iii/

class Solution:
    def reverseWords(self, s: str) -> str:
        i = 0
        result = []

        while i < len(s):
            if s[i] != " ":
                j = 0
                while i + j < len(s) and s[i + j] != " ":
                    j += 1

                j -= 1
                for c in range(i + j, i - 1, -1):
                    result.append(s[c])
                
                i += j
            else:
                result.append(" ")

            i += 1

        return "".join(result)

result = Solution().reverseWords("Let's take LeetCode contest")
print(result)