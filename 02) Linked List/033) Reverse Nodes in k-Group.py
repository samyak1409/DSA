"""
https://leetcode.com/problems/reverse-nodes-in-k-group
"""


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_


def reverse_k_group(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    """"""

    # Follow-up: Can you solve the problem in O(1) extra memory space?
