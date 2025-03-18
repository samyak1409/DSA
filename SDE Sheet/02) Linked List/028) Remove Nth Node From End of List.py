"""
https://leetcode.com/problems/remove-nth-node-from-end-of-list
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_


def remove_nth_from_end(head: ListNode | None, n: int) -> ListNode | None:
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

    """
    # Send one pointer to nth node:
    n_ahead = head  # not using head for traversing because we've to return head
    for _ in range(n):
        n_ahead = n_ahead.next

    # Handle Edge Case: Node to delete is head:
    if n_ahead is None:
        return head.next

    # Go to the node before the node to delete:
    node = head
    while n_ahead.next:
        node, n_ahead = node.next, n_ahead.next

    # Change Pointer:
    node.next = node.next.next
    return head
    """

    # Or we can do this (without handling that one edge case explicitly) by using a dummy prev of head ptr:

    # Start with prev of head (by making `head` = next of our newly created dummy node):
    to_head = n1 = n2 = ListNode(next_=head)

    # Move fast ptr:
    for _ in range(n):
        n2 = n2.next

    # Move both till fast is not at last node:
    while n2.next:
        n1, n2 = n1.next, n2.next

    # Change the ptr in order to delete, and return the saved head:
    n1.next = n1.next.next
    return to_head.next


# Similar Questions:
# https://leetcode.com/problems/swapping-nodes-in-a-linked-list
# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list
