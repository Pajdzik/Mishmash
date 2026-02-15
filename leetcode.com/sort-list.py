#!/bin/python3
# https://leetcode.com/problems/sort-list


from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def print_list(head: ListNode):
            node = head
            while node:
                print(node.val, end=", ")
                node = node.next

        sorted = True
        dummy = ListNode(-1000000, head)

        prev = dummy
        curr = head
        next = head.next if head else None

        while True:
            # print()
            # print_list(dummy)

            if not curr:  # reset
                if sorted:
                    break

                sorted = True
                prev = dummy
                curr = dummy.next
                next = curr.next

            if next and curr.val > next.val:
                sorted = False

                # prev -> curr -> next -> nnext
                # prev -> next -> curr -> nnext

                next_next = next.next
                prev.next = next
                curr.next = next_next
                next.next = curr

                curr, next = next, curr
            else:
                prev = curr
                curr = next
                next = next.next if next else None

        return dummy.next


if __name__ == "__main__":
    Solution().sortList(ListNode(4, ListNode(2, ListNode(1, ListNode(3)))))
