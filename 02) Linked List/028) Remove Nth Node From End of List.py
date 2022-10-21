"""
https://leetcode.com/problems/remove-nth-node-from-end-of-list
"""


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_


def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    """"""

    # https://leetcode.com/problems/remove-nth-node-from-end-of-list/discuss/1164537/Short-and-Simple-One-Pass-Solution-w-Explanation-or-Beats-100-or-No-dummy-node-required!

    # 0) Brute-force (Calc Len): TC = O(n+n); SC = O(1)

    """
    # Calc Len of LL:
    node = head  # not using head for traversing because we've to return head
    l = 1
    while node := node.next:
        l += 1
    # Handle Edge Case: Node to delete is head:
    if n == l:
        return head.next
    # Go to the node before the node to delete:
    node = head
    for _ in range(l-n-1):
        node = node.next
    # Change Pointer:
    node.next = node.next.next
    return head
    """

    # Follow up: Could you do this in one pass?
    # 1) Optimal (Two Pointers): TC = O(n); SC = O(1)
    # Maintain two pointers and update one with a delay of n steps.

    # Send one pointer to nth node:
    n_ahead = head  # not using head for traversing because we've to return head
    for _ in range(n):
        n_ahead = n_ahead.next
    # Handle Edge Case: Node to delete is head:
    if n_ahead is None:
        return head.next
    # Go to the node before the node to delete:
    node = head
    while n_ahead := n_ahead.next:  # while `n_ahead.next` is not None
        node = node.next
    # Change Pointer:
    node.next = node.next.next
    return head


# Similar Questions:
# https://leetcode.com/problems/swapping-nodes-in-a-linked-list
# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list
