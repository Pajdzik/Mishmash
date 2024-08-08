#!/bin/python3
# https://leetcode.com/problems/merge-nodes-in-between-zeros

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        result_node = dummy

        input_node = head.next
        acc = 0
        while input_node:
            if input_node.val == 0:
                node = ListNode(acc)
                acc = 0
                result_node.next = node
                result_node = node
            else:
                acc += input_node.val

            input_node = input_node.next

        return dummy.next
