#!/bin/python3
# https://leetcode.com/problems/word-ladder/

from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        def is_diff_single_letter(word: str, other_word: str) -> bool:
            diff_char = False
            for i in range(len(word)):
                if word[i] != other_word[i]:
                    if diff_char:
                        return False
                    else:
                        diff_char = True

            return True

        def add_connections(word: str, start_index: int = 0) -> None:
            for j in range(start_index, len(wordList)):
                other_word = wordList[j]
                if is_diff_single_letter(word, other_word):
                    connections[word].append(other_word)
                    connections[other_word].append(word)

        connections = { word: [] for word in wordList }
        connections[beginWord] = []

        add_connections(beginWord)

        for i, word in enumerate(wordList):
            add_connections(word, i + 1)

        visited = set()
        queue = deque([ (beginWord, 1) ])
        
        while queue:
            node, distance = queue.popleft()
            visited.add(node)

            if node == endWord:
                return distance

            for target_node in connections[node]:
                if target_node in visited:
                    continue

                queue.append((target_node, distance + 1))

        return 0

if __name__ == "__main__":
    assert(Solution().ladderLength(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]) == 5)