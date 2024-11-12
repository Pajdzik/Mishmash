#!/bin/python3
# https://leetcode.com/problems/most-beautiful-item-for-each-query

import bisect
from typing import List


class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        get_first_element = lambda x: x[0]
        sorted_items = sorted(items, key=get_first_element)

        max_beauty = sorted_items[0][1]
        for item in sorted_items:
            max_beauty = max(item[1], max_beauty)
            item[1] = max_beauty

        result = []
        for query in queries:
            index = bisect.bisect_right(sorted_items, query, key=get_first_element)
            if index:
                result.append(sorted_items[index - 1][1])
            else:
                result.append(0)

        return result


def invoke():
    def test(expected, items, queries):
        sol = Solution()
        result = sol.maximumBeauty(items, queries)
        assert result == expected, f"Expected {expected}, but got {result}"
        print(f"Test passed for queries: {queries}")

    test(
        [
            962,
            962,
            962,
            962,
            746,
            962,
            962,
            962,
            946,
            962,
            962,
            919,
            746,
            746,
            962,
            962,
            962,
            919,
            962,
        ],
        [
            [193, 732],
            [781, 962],
            [864, 954],
            [749, 627],
            [136, 746],
            [478, 548],
            [640, 908],
            [210, 799],
            [567, 715],
            [914, 388],
            [487, 853],
            [533, 554],
            [247, 919],
            [958, 150],
            [193, 523],
            [176, 656],
            [395, 469],
            [763, 821],
            [542, 946],
            [701, 676],
        ],
        [
            885,
            1445,
            1580,
            1309,
            205,
            1788,
            1214,
            1404,
            572,
            1170,
            989,
            265,
            153,
            151,
            1479,
            1180,
            875,
            276,
            1584,
        ],
    )

    test([0], [[10, 1000]], [5])
    test(
        [2, 4, 5, 5, 6, 6], [[1, 2], [3, 2], [2, 4], [5, 6], [3, 5]], [1, 2, 3, 4, 5, 6]
    )


if __name__ == "__main__":
    invoke()
