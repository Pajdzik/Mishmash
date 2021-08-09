#!/bin/python3
# https://leetcode.com/problems/odd-even-linked-list/

from operator import is_
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
            
        odd_node = head
        even_node = head.next
        even_head = even_node

        while even_node and even_node.next:
            odd_node.next = odd_node.next.next
            even_node.next = even_node.next.next
            odd_node = odd_node.next
            even_node = even_node.next

        odd_node.next = even_head

        return head

head = node = ListNode(1)
for i in [2,3,4,5,6,7,8]:
    node.next = ListNode(i)
    node = node.next

Solution().oddEvenList(head)