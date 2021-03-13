#!/usr/bin/env python
# https://www.geeksforgeeks.org/boggle-find-possible-words-board-characters/

class TrieNode():
    def __init__(self, value, children=None, is_terminating=False):
        self.value = value
        self.children = [] if children is None else children
        self.is_terminating = is_terminating

def find_word(words, letters, trie):
    for i in range(len(letters)):
        for j in range(len(letters)):
            visited = set()

            for child in trie.children:
                if child.value == letters[i][j]:
                    result = exists(child, letters, (i, j), visited)
                    print(result)
            

def exists(trie_node, letters, letter_index, visited):
    if letter_index in visited:
        return None

    visited.add(letter_index)

    if trie_node.is_terminating:
        return trie_node.value

    i, j = letter_index

    for child_i in range(i - 1, i + 2):
        for child_j in range(j - 1, j + 2):
            if 0 <= child_i < len(letters) and 0 <= child_j < len(letters):
                for child in trie_node.children:
                    if letters[child_i][child_j] == child.value:
                        return exists(child, letters, (child_i, child_j), visited)

def build_trie(words):
    root = TrieNode("")
    child = None

    for word in words:
        parent = root
        for letter in word:
            node = insert_node(parent, letter)
            parent = node

        child = insert_node(parent, word, True)

    return root
    

def insert_node(parent, letter, is_terminating=False):
    for child in parent.children:
        if child.value == letter:
            return child

    node = TrieNode(letter, [], is_terminating)
    parent.children.append(node)
    return node

def print_trie(root):
    queue = [root]

    while len(queue) > 0:
        node = queue.pop(0)

        print(node.value + ": ", end='')
        for child in node.children:
            print(child.value, end=", ")

        print("\n")

        queue.extend(node.children)

if __name__ == "__main__":
    words = ["GEEK", "GEEKS", "FOR", "QUIZ", "GO"]
    letters = [
        [ "G", "I", "Z" ],
        [ "U", "E", "K" ],
        [ "Q", "S", "E" ]
    ]

    trie = build_trie(words)
    find_word(words, letters, trie)

    # result = find_word(words, letters)
    # print(result)