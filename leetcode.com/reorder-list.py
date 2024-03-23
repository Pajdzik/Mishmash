#!/bin/python3
# https://leetcode.com/problems/reorder-list
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, node: Optional[ListNode]) -> None:
        if not node or not node.next:
            return

        one_but_last = node.next
        while one_but_last.next and one_but_last.next.next:
            one_but_last = one_but_last.next

        to_connect = one_but_last.next
        next_node = node.next
        one_but_last.next = None
        if to_connect:
            to_connect.next = next_node
            node.next = to_connect
        else:
            node.next = one_but_last

        self.reorderList(next_node)


if __name__ == "__main__":
    def list_to_linked_list(values: list[int]) -> ListNode:
        head = ListNode(values[0])
        node = head
        for value in values[1:]:
            node.next = ListNode(value)
            node = node.next
        return head

    def test(expected: list[int], values: list[int]):
        head = list_to_linked_list(values)
        Solution().reorderList(head)
        node = head
        result = []
        while node:
            result.append(node.val)
            node = node.next
        assert result == expected, f"Expected: {expected}, but got: {result}"

    # test([1, 5, 2, 4, 3], [1, 2, 3, 4, 5])
    test([1, 4, 2, 3], [1, 2, 3, 4])
