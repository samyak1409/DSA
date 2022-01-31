"""
https://leetcode.com/problems/merge-two-sorted-lists/
"""


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

    # TC = O(n); SC = O(n)

    head = l = ListNode()  # head -> saving ref (coz singly linked list)

    while l1 and l2:  # while both linked lists have nodes left

        if l1.val < l2.val:
            l.next = l1
            l1 = l1.next  # inc

        else:
            l.next = l2
            l2 = l2.next  # inc

        l = l.next  # inc

    l.next = l1 or l2  # remaining node(s) from either l1 or l2

    return head.next
