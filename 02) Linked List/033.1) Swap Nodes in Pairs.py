"""
https://leetcode.com/problems/swap-nodes-in-pairs
"""


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_


def swap_pairs(head: Optional[ListNode]) -> Optional[ListNode]:
    """"""

    # You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be
    # changed).

    # 1) Optimal (Change Pointers): TC = O(n); SC = O(1)

    # OOPS, forgot about last node's next pointer, resulting in WA:
    """
    if not head or not head.next:  # edge cases
        return head

    node, head = head, head.next  # `node`: for traversal, `head`: new head
    while node and node.next:  # while 2 nodes are there
        # node.next, node.next.next = node.next.next, node  # swap nodes by changing pointers
        # WHY IS PYTHONIC SWAPPING (PARALLEL ASSIGNMENT) NOT WORKING? 😶 [Create PR]
        temp = node.next
        node.next = node.next.next
        temp.next = node
        node = node.next  # ++
    return head
    """
    # Fixed:
    """
    if not head or not head.next:  # edge cases
        return head

    node, head = head, head.next  # `node`: for traversal, `head`: new head
    while node and node.next:  # while 2 nodes are there
        # node.next, node.next.next = node.next.next, node  # swap nodes by changing pointers
        # WHY IS PYTHONIC SWAPPING (PARALLEL ASSIGNMENT) NOT WORKING? 😶 [Create PR]
        temp = node.next
        node.next = node.next.next
        temp.next = node
        # node, node.next = node.next, node.next.next if node.next and node.next.next else node.next  # ++, beforehand
        # change next of last node if 2 nodes are still there
        # WHY IS PYTHONIC SWAPPING (PARALLEL ASSIGNMENT) NOT WORKING? 😶 [Create PR]
        temp = node.next
        if node.next and node.next.next:  # if 2 nodes are still there
            node.next = node.next.next  # beforehand change next of last node
        node = temp  # ++
    return head
    """
    # Becomes easier with a dummy node:
    to_head = node = ListNode(next_=head)  # `to_head`: ptr to new_head; `node`: traverse and change pointers
