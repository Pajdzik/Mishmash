#!/bin/python3
# https://leetcode.com/problems/


from typing import List, Optional

""" 
001011
000124
11.85310
"""


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        split_boxes = list(boxes)

        count = 0
        previous = 0

        result = [0] * len(boxes)
        for i in range(len(boxes)):
            result[i] = previous
            if split_boxes[i] == "1":
                count += 1

            previous += count

        count = 0
        previous = 0

        for i in range(len(boxes) - 1, -1, -1):
            result[i] += previous
            if split_boxes[i] == "1":
                count += 1

            previous += count

        return result


if __name__ == "__main__":
    assert Solution().minOperations("001011") == [11, 8, 5, 4, 3, 4]
    assert Solution().minOperations("110") == [1, 1, 3]
