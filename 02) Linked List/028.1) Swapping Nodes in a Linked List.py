"""
https://leetcode.com/problems/swapping-nodes-in-a-linked-list
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_


def swap_nodes(head: ListNode | None, k: int) -> ListNode | None:
    """"""

    # All the solutions are (modifications of the solutions) from
    # https://github.com/samyak1409/DSA/blob/main/02%29%20Linked%20List/028%29%20Remove%20Nth%20Node%20From%20End%20of%20List.py.

    # 0.1) Brute-force (To Array): TC = O(n+n); SC = O(n)
    # We can transform the linked list to an array this should ease things up
    # After transforming the linked list to an array it becomes as easy as swapping two integers in an array then
    # rebuilding the linked list

    # 0.2) Brute-force (Calc Len): TC = O(n+n); SC = O(1)

    """
    # kth node from the beginning:
    node1 = head
    for _ in range(k-1):
        node1 = node1.next
    # Calc Len (n) of LL:
    node = head  # not using head for traversing because we've to return head
    n = 1
    while node := node.next:
        n += 1
    # kth node from the end:
    node2 = head
    for _ in range(n-k):
        node2 = node2.next
    # Swap Values:
    node1.val, node2.val = node2.val, node1.val
    return head
    """

    # 1) Optimal (Two Pointers): TC = O(n); SC = O(1)
    # https://leetcode.com/problems/swapping-nodes-in-a-linked-list/discuss/1054370/Python-3-or-Swapping-NODES-or-Swapping-Values-or-One-Pass-or-Fully-explained
    # This question can be very easily solved if we only swap the value in the nodes. Follow the bellow steps to swap
    # the values :-
    # Find the k-th node from the front.
    # Find the k-th last element using two pointers method.
    # Swap their values.
    # Return the head of the Linked List

    # kth node from the beginning:
    node1 = head
    for _ in range(k-1):
        node1 = node1.next
    # kth node from the end:
    node2, none_checker = head, node1
    while none_checker := none_checker.next:
        node2 = node2.next
    # Swap Values:
    node1.val, node2.val = node2.val, node1.val
    return head
