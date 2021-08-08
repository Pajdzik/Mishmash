#!/bin/python3
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        node = head

        while node and node.next != None:
            next = node.next

            while next and node.val == next.val:
                next = next.next

            node.next = next
            
            if next != None:
                node, next = next, next.next
            else:
                node.next = None

        return head


head = ListNode(1)
node = head

for i in [1,2,3,3]:
    node.next = ListNode(i)
    node = node.next

Solution().deleteDuplicates(head)