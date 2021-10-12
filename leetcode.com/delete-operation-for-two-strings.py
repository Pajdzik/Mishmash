#!/bin/python3
# https://leetcode.com/problems/delete-operation-for-two-strings/

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memory = [ [ None for _ in range(len(word2) + 1) ] for _ in range(len(word1) + 1) ]
        def calculate_longest_common_subsequence(word1: str, i1: int, word2: str, i2: int) -> int:
            if i1 == 0 or i2 == 0:
                return 0

            if memory[i1][i2] != None:
                return memory[i1][i2]
            
            if word1[i1 - 1] == word2[i2 - 1]:
                lcs = 1 + calculate_longest_common_subsequence(word1, i1 - 1, word2, i2 - 1)
                memory[i1][i2] = lcs
            else:
                lcs1 = calculate_longest_common_subsequence(word1, i1 - 1, word2, i2)
                lcs2 = calculate_longest_common_subsequence(word1, i1, word2, i2 - 1)
                memory[i1][i2] = max(lcs1, lcs2)
            
            return memory[i1][i2]

        lcs = calculate_longest_common_subsequence(word1, len(word1), word2, len(word2))
        return len(word1) + len(word2) - 2 * lcs

    def minDistance_dp(self, word1: str, word2: str) -> int:
        memory = [ [ None for _ in range(len(word2) + 1) ] for _ in range(len(word1) + 1) ]

        for i in range(len(word1) + 1):
            memory[i][0] = 0
        for j in range(len(word2) + 1):
            memory[0][j] = 0

        for i1, c1 in enumerate(word1):
            for i2, c2 in enumerate(word2):
                if c1 == c2:
                    memory[i1 + 1][i2 + 1] = memory[i1][i2] + 1
                else:
                    memory[i1 + 1][i2 + 1] = max(memory[i1 + 1][i2], memory[i1][i2 + 1])

        return len(word1) + len(word2) - 2 * memory[-1][-1]

if __name__ == "__main__":
    Solution().minDistance("leetcode", "code")