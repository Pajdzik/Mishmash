#!/usr/bin/env python
# Given two (singly) linked lists, determine if the two lists intersect.
# Return the inter-secting node. Note that the intersection is defined based on reference, not value.
# That is, if the kth node of the first linked list is the exact same node (by reference)
# as the jth node of the second linked list, then they are intersecting

def findMergeNode(head1, head2):
    node1 = head1
    node2 = head2

    while node1 != None:
        while node2 != None:
            if node1 == node2:
                return node1.value

            node2 = node2.next

        node1 = node1.next
        node2 = head2

