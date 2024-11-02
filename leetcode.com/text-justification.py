#!/bin/python3
# https://leetcode.com/problems/text-justification

from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def pad_right(line: List[str]) -> str:
            line_parts = [line[0]]
            for i in range(1, len(line)):
                line_parts.append(" ")
                line_parts.append(line[i])

            line = "".join(line_parts)
            right_pad = " " * (maxWidth - len(line))

            return line + right_pad

        def pad(line: List[str]) -> str:
            if len(line) == 1:
                return pad_right(line)

            line_length = sum([len(word) for word in line])
            diff_to_fill = maxWidth - line_length

            number_of_spaces = len(line) - 1
            equal_width_space = diff_to_fill // number_of_spaces
            space_reminder = diff_to_fill - (equal_width_space * number_of_spaces)

            output_line = [line[0]]
            for i in range(1, len(line)):
                output_line.append(" " * equal_width_space)
                if space_reminder:
                    output_line.append(" ")
                    space_reminder -= 1
                output_line.append(line[i])

            return "".join(output_line)

        result_text = []
        line = []
        current_line_length_with_spaces = 0

        for word in words:
            if current_line_length_with_spaces + len(word) > maxWidth:
                output_line = pad(line)
                result_text.append(output_line)
                line = []
                current_line_length_with_spaces = 0

            line.append(word)
            current_line_length_with_spaces += len(word) + 1

        result_text.append(pad_right(line))

        return result_text


def test(expected: List[str], words: List[str], maxWidth: int):
    solution = Solution()
    result = solution.fullJustify(words, maxWidth)
    assert result == expected, f"Expected {expected}, but got {result}"


def main():
    test(
        [
            "ask   not   what",
            "your country can",
            "do  for  you ask",
            "what  you can do",
            "for your country",
        ],
        [
            "ask",
            "not",
            "what",
            "your",
            "country",
            "can",
            "do",
            "for",
            "you",
            "ask",
            "what",
            "you",
            "can",
            "do",
            "for",
            "your",
            "country",
        ],
        16,
    )

    test(
        ["This    is    an", "example  of text", "justification.  "],
        ["This", "is", "an", "example", "of", "text", "justification."],
        16,
    )
    test(
        ["What   must   be", "acknowledgment  ", "shall be        "],
        ["What", "must", "be", "acknowledgment", "shall", "be"],
        16,
    )


if __name__ == "__main__":
    main()
