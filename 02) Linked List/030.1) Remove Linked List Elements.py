"""
https://leetcode.com/problems/remove-linked-list-elements
"""


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_


def remove_elements(head: Optional[ListNode], val: int) -> Optional[ListNode]:
    """"""

    # 1) Time-Optimal (Recursion): TC = O(n); SC = O(n) {recursion stack}
    # https://leetcode.com/problems/remove-linked-list-elements/discuss/57306/3-line-recursive-solution

    # 2) Optimal (Dummy Node & Iterate): TC = O(n); SC = O(1)
    # Must read:
    # https://leetcode.com/problems/remove-linked-list-elements/discuss/158651/Simple-Python-solution-with-explanation-(single-pointer-dummy-head).

    to_head = node = ListNode(next_=head)  # `to_head` -> dummy node whose next will be the head of our final LL
    while node.next:
        if node.next.val == val:
            node.next = node.next.next  # delete the node with .val == val
        else:
            node = node.next  # ++
    return to_head.next
