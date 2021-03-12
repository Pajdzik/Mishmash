#!/usr/bin/env python
# https://www.geeksforgeeks.org/boggle-find-possible-words-board-characters/

def find_first_letters(word, letters):
    result = []
    length = len(letters)
    for i in range(length):
        for j in range(length):
            if letters[i][j] == word[0]:
                result.append((i, j))

    return result

def check_word(start, word, letters):
    length = len(letters)
    visited = { }
    queue = [ start ]
    letter_index = 0

    while len(queue) > 0:
        index = queue.pop()
        visited.add(index)
        i, j = index

        if letters[i][j] == word[letter_index]:
            if letter_index == len(word):
                return True

            letter_index += 1

            queue.append(i - 1, j - 1)
            queue.append(i - 1, j)
            queue.append(i - 1, j + 1)
            queue.append(i, j - 1)
            queue.append(i, j + 1)
            queue.append(i + 1, j - 1)
            queue.append(i + 1, j)
            queue.append(i + 1, j + 1)
    
    return False


def find_word(words, letters):
    result = []
    for word in words:
        first_letters = find_first_letters(word, letters)
        for first_letter in first_letters:
            if check_word(first_letter, word, letters):
                result.append(word)

    return result


if __name__ == "__main__":
    words = ["GEEKS", "FOR", "QUIZ", "GO"]
    letters = [
        [ "G", "I", "Z" ],
        [ "U", "E", "K" ],
        [ "Q", "S", "E" ]
    ]

    result = find_word(words, letters)
    print(result)