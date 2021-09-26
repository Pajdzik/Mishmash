#!/bin/python3
# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(None, head)
        prev = dummy
        curr = head

        while curr:
            next = curr.next

            if curr and next and curr.val == next.val:
                while curr and next and curr.val == next.val:
                    curr = next
                    next = next.next
                
                prev.next = next
                curr = next
            else:
                prev = curr
                curr = next

        return dummy.next

root = ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(4, ListNode(4, ListNode(5)))))))
Solution().deleteDuplicates(root)
print(root)