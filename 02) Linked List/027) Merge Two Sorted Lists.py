"""
https://leetcode.com/problems/merge-two-sorted-lists
"""


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_


def merge_two_lists(node1: Optional[ListNode], node2: Optional[ListNode]) -> Optional[ListNode]:
    """"""

    # Similar to what we did here:
    # https://github.com/samyak1409/DSA/blob/main/01%29%20Arrays/009%29%20Merge%20Sorted%20Array.py

    # NOTE: "Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the
    # first two lists." means IN-PLACE.
    # Wrong: https://youtu.be/Xb4slcp1U38 (Both approaches discussed in the video are "in-place" only.)
    # Don't watch any videos or read any articles, following covers all the approaches (needed to be covered) with
    # explanations.

    # 2) Time-Optimal (Recursive: Traverse & Compare): TC = O(n); SC = O(n) {recursion stack}
    # https://leetcode.com/problems/merge-two-sorted-lists/discuss/9735/Python-solutions-(iteratively-recursively-iteratively-in-place).

    """
    if not node1 or not node2:  # base case: reached at the end node of either (or both) LLs
        return node1 or node2  # start to recurse out

    if node1.val < node2.val:
        node1.next = merge_two_lists(node1=node1.next, node2=node2)  # recurse in
        return node1
    else:  # (node1.val >= node2.val)
        node2.next = merge_two_lists(node1=node1, node2=node2.next)  # recurse in
        return node2
    """

    # 1) Optimal (Iterative: Traverse & Compare): TC = O(n); SC = O(1)
    # https://leetcode.com/problems/merge-two-sorted-lists/discuss/9735/Python-solutions-(iteratively-recursively-iteratively-in-place).

    # 1.1) Without using a dummy node:
    """
    if not node1 or not node2:  # edge case: either or both LL are empty
        return node1 or node2

    # Assigning head node:
    if node1.val < node2.val:
        head = node1
        node1 = node1.next  # ++
    else:  # (node1.val >= node2.val)
        head = node2
        node2 = node2.next  # ++

    node = head  # not using head for traversing because we've to return head

    # Assigning next nodes one by one:
    while node1 and node2:  # while both LLs have nodes left
        if node1.val < node2.val:
            node.next = node1  # changing ptr
            node1 = node1.next  # ++
        else:  # (node1.val >= node2.val)
            node.next = node2  # changing ptr
            node2 = node2.next  # ++
        node = node.next  # ++

    node.next = node1 or node2  # remaining node(s)

    return head
    """
    # 1.2) Using a dummy node made it easier:
    to_head = node = ListNode()  # `to_head` -> dummy node whose next will be the head of our merged LL
    # `node` -> not using head for traversing because we've to return it

    while node1 and node2:  # while both LLs have nodes left
        if node1.val < node2.val:
            node.next = node1  # changing ptr
            node1 = node1.next  # ++
        else:  # (node1.val >= node2.val)
            node.next = node2  # changing ptr
            node2 = node2.next  # ++
        node = node.next  # ++

    node.next = node1 or node2  # remaining node(s)

    return to_head.next


# Similar Question: https://leetcode.com/problems/merge-sorted-array
