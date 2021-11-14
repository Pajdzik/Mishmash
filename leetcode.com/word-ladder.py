#!/bin/python3
# https://leetcode.com/problems/word-ladder/

from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        connections = { }

        def get_word_with_wildcards(word: str) -> list[str]:
            for i in range(len(word)):
                yield word[:i] + "*" + word[i + 1:]

        def add_word(word: str):
            for wildcard_word in get_word_with_wildcards(word):
                if wildcard_word not in connections:
                    connections[wildcard_word] = []
                
                connections[wildcard_word].append(word)

        for i, word in enumerate(wordList):
            add_word(word)

        visited = set()
        queue = deque([ (beginWord, 1) ])
        
        while queue:
            node, distance = queue.popleft()
            visited.add(node)

            for wildcard_word in get_word_with_wildcards(node):
                if wildcard_word not in connections:
                    continue
                
                for target_node in connections[wildcard_word]:
                    if target_node in visited:
                        continue

                    if target_node == endWord:
                        return distance + 1

                    queue.append((target_node, distance + 1))

        return 0

if __name__ == "__main__":
    assert(Solution().ladderLength(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]) == 5)