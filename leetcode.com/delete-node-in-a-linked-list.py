#!/bin/python3
# https://leetcode.com/problems/delete-node-in-a-linked-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int, next: 'ListNode'=None):
        self.val = val
        self.next = next

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        curr = node
        next = node.next

        while next.next:
            curr.val = next.val
            curr = next
            next = next.next

        curr.val = next.val
        curr.next = None

root = ListNode(4, ListNode(5, ListNode(1, ListNode(9))))
node = Solution().deleteNode(root.next)
print(node)