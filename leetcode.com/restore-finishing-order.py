#!/bin/python3
# https://leetcode.com/problems/restore-finishing-order


from typing import List


class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        friends_set = set(friends)
        result = list(filter(lambda o: o in friends_set, order))
        return result


if __name__ == "__main__":
    assert Solution().recoverOrder(order=[3, 1, 2, 5, 4], friends=[1, 3, 4]) == [
        3,
        1,
        4,
    ]
