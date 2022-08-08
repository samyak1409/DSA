"""
https://leetcode.com/problems/merge-two-sorted-lists
"""


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.nxt = nxt


def merge_two_lists(node1: Optional[ListNode], node2: Optional[ListNode]) -> Optional[ListNode]:
    """"""

    # https://github.com/samyak1409/DSA/blob/main/01%29%20Arrays/009%29%20Merge%20Sorted%20Array.py#L16

    # Brute-force = Optimal (Traverse & Compare): TC = O(n); SC = O(1)
    # https://leetcode.com/problems/merge-two-sorted-lists/discuss/1826693/Python3-MERGING-Explained

    ptr_to_head = node = ListNode()  # ptr_to_head -> saving ref to return (because singly linked list)

    while node1 and node2:  # while both linked lists have nodes left
        # IMP: not copying the value but assigning the pointer to the existence address because
        # "The list should be made by splicing together the nodes of the first two lists."
        if node1.val < node2.val:
            node.nxt = node1
            node1 = node1.nxt  # move ahead
        else:
            node.nxt = node2
            node2 = node2.nxt  # move ahead
        node = node.nxt  # move ahead

    node.nxt = node1 or node2  # remaining node(s)

    return ptr_to_head.nxt
