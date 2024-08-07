#!/bin/python3
# https://leetcode.com/problems/integer-to-english-words

digits = [
    "",
    "One",
    "Two",
    "Three",
    "Four",
    "Five",
    "Six",
    "Seven",
    "Eight",
    "Nine",
]


class Solution:
    def two_digits_to_word(self, num: int) -> str:
        assert num < 100
        if 11 <= num <= 19:
            teens = [
                "",
                "Eleven",
                "Twelve",
                "Thirteen",
                "Fourteen",
                "Fifteen",
                "Sixteen",
                "Seventeen",
                "Eighteen",
                "Nineteen",
            ]
            return teens[num - 10]

        single_digit = num % 10
        single_digit_str = digits[single_digit] if num > 0 else ""

        tens = [
            "",
            "Ten",
            "Twenty",
            "Thirty",
            "Forty",
            "Fifty",
            "Sixty",
            "Seventy",
            "Eighty",
            "Ninety",
        ]
        tens_digit = (num // 10) % 10
        tens_digit_str = tens[tens_digit] if tens_digit > 0 else ""

        return (tens_digit_str + " " + single_digit_str).strip()

    def three_digits_to_word(self, num: int) -> str:
        assert num < 1000

        hundreds_digit = (num // 100) % 10
        hundreds_digit_str = (
            digits[hundreds_digit] + " Hundred" if hundreds_digit > 0 else ""
        )

        two_digits = self.two_digits_to_word(num % 100)
        non_empty_strings = filter(lambda s: s != "", [hundreds_digit_str, two_digits])
        return (" ".join(non_empty_strings)).strip()

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        suffixes = ["", "Thousand", "Million", "Billion"]
        suffix_index = 0

        words = []

        while num:
            number = self.three_digits_to_word(num % 1000)
            suffix = suffixes[suffix_index]
            num //= 1000
            suffix_index += 1
            if number != "":
                words.append(number + " " + suffix)

        return (" ".join(reversed(words))).strip()


if __name__ == "__main__":

    def test_three_digits_to_word():
        def test_case(num, expected):
            s = Solution()
            result = s.three_digits_to_word(num)
            assert result == expected, f"{result} != {expected}"

        test_case(0, "")
        test_case(1, "one")
        test_case(10, "ten")
        test_case(11, "eleven")
        test_case(20, "twenty")
        test_case(21, "twenty one")
        test_case(100, "one hundred")
        test_case(101, "one hundred one")
        test_case(110, "one hundred ten")
        test_case(111, "one hundred eleven")
        test_case(200, "two hundred")
        test_case(201, "two hundred one")
        test_case(210, "two hundred ten")
        test_case(211, "two hundred eleven")
        test_case(999, "nine hundred ninety nine")

    def test_solution():
        def test_case(num, expected):
            s = Solution()
            result = s.numberToWords(num)
            assert result == expected, f"{num}: {result} != {expected}"

        test_case(1000010, "One Million Ten")
        test_case(123, "One Hundred Twenty Three")
        test_case(12345, "Twelve Thousand Three Hundred Forty Five")
        test_case(
            1234567,
            "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven",
        )
        test_case(
            1234567891,
            "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One",
        )

    test_solution()
