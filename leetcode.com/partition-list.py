#!/bin/python3
# https://leetcode.com/problems/


from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        smaller = ListNode(None)
        larger = ListNode(None)

        current_smaller = smaller
        current_larger = larger

        current = head

        while current:
            next = current.next
            current.next = None

            if current.val >= x:
                current_larger.next = current
                current_larger = current
            else:
                current_smaller.next = current
                current_smaller = current

            current = next

        current_smaller.next = larger.next
        return smaller.next


if __name__ == "__main__":

    def list_from_array(nums: List[int]) -> ListNode:
        dummy = ListNode(None)
        current = dummy
        for num in nums:
            next = ListNode(num)
            current.next = next
            current = next
        return dummy.next

    Solution().partition(list_from_array([1, 4, 3, 2, 5, 2]), 3)
