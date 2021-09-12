#!/bin/python3
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def removeNthFromEnd(self, node: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = node
        front_node = dummy
        back_node = dummy

        while front_node and n >= 0:
            front_node = front_node.next
            n -= 1

        while front_node:
            front_node = front_node.next
            back_node = back_node.next

        back_node.next = back_node.next.next if back_node.next else None
        return dummy.next

    def removeNthFromEnd_recursive(self, node: Optional[ListNode], n: int) -> Optional[ListNode]:
        if node.next == None:
            return 0
        else:
            dist = self.removeNthFromEnd(node.next, n) + 1
            if dist == n:
                node.next = node.next.next if node.next else None
            return dist

# root = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
root = ListNode(1, ListNode(2))
# root = ListNode(1)
node = Solution().removeNthFromEnd(root, 2)
print(node)