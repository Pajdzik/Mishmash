#!/bin/python3
# https://leetcode.com/problems/word-break/

class Solution:
    def wordBreak(self, s: str, word_dict: list[str]) -> bool:
        words = set(word_dict)
        possible = [False] *(len(word_dict) + 1)
        possible[0] = True

        for end in range(1, len(word_dict) + 1):
            for start in range(end):
                if possible[start] and s[start:end] in words:
                    possible[end] = True
                    break

        return possible[-1]

    def wordBreak_bfs(self, s: str, word_dict: list[str]) -> bool:
        words = set(word_dict)
        queue = [ "" ]
        visited = [ False ] * (len(s) + 1)

        while queue:
            word = queue.pop(0)

            if visited[len(word)]:
                continue

            if word == s:
                return True

            start = len(word)
            for end in range(len(word) + 1, len(s) + 1):
                if s[start:end] in words:
                    queue.append(word + s[start:end])

            visited[len(word)] = True

        return False

    def wordBreak_bottom_up_brute_force(self, final_word: str, word_dict: list[str], word: str = "") -> bool:
        if final_word == word:
            return True

        for part in word_dict:
            if len(word) + len(part) <= len(final_word):
                result = self.wordBreak(final_word, word_dict, word + part)
                if result:
                    return True
                
        return False
        

if __name__ == "__main__":
    assert(Solution().wordBreak("leetcode", ["leet","code"]))
    assert(Solution().wordBreak("applepenapple", ["apple","pen"]))
    assert(not Solution().wordBreak("catsandog", ["cats","dog","sand","and","cat"]))
    assert(not Solution().wordBreak("ccbb", ["bc","cb"]))
