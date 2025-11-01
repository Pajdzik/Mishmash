#!/bin/python3
# https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array

from typing import List, Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def modifiedList(
        self, nums: List[int], head: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode()
        nums_set = set(nums)

        prev = dummy
        curr = head

        while curr:
            while curr and curr.val in nums_set:
                curr = curr.next

            prev.next = curr
            prev = curr
            curr = curr if not curr else curr.next

        return dummy.next


if __name__ == "__main__":
    # Solution().modifiedList([9, 2, 5], ListNode(2, ListNode(10, ListNode(9))))
    Solution().modifiedList(
        [1, 2, 3], ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    )
