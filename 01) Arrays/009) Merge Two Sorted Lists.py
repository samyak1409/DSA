"""
https://leetcode.com/problems/merge-two-sorted-lists
"""


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.nxt = nxt


def merge_two_lists(ln1: Optional[ListNode], ln2: Optional[ListNode]) -> Optional[ListNode]:
    """"""

    # https://github.com/samyak1409/DSA/blob/main/01%29%20Arrays/009%29%20Merge%20Sorted%20Array.py#L16

    # Brute-force = Optimal (Traverse & Compare): TC = O(n); SC = O(1)
    # https://leetcode.com/problems/merge-two-sorted-lists/discuss/1826693/Python3-MERGING-Explained

    head = ln = ListNode()  # head -> saving ref (coz singly linked list)

    while ln1 and ln2:  # while both linked lists have nodes left
        if ln1.val < ln2.val:
            ln.nxt = ln1
            ln1 = ln1.nxt  # inc
        else:
            ln.nxt = ln2
            ln2 = ln2.nxt  # inc
        ln = ln.nxt  # inc

    ln.nxt = ln1 or ln2  # remaining node(s) from ln1 if ln1 else ln2

    return head.nxt
