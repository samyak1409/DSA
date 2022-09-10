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

    # 1) Optimal (Iteratively Change Pointers): TC = O(n); SC = O(1)

    # OOPS, forgot about last node's next pointer, resulting in WA:
    """
    if not head or not head.next:  # edge cases
        return head

    node, head = head, head.next  # `node`: for traversal, `head`: new head
    while node and node.next:  # while 2 nodes are there
        # node.next, node.next.next = node.next.next, node  # swap nodes by changing pointers
        # Why is pythonic swapping (parallel assignment) not working? Following (normal swapping) works:
        '''
        temp = node.next
        node.next = node.next.next
        temp.next = node
        '''
        # Wait, tried to change the order, and it works! Why exactly if assignment is being done parallely anyway?
        # [Create PR]
        node.next.next, node.next = node, node.next.next  # swap nodes by changing pointers
        # (Looks like we need to assign farther pointers before.)
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
        # Why is pythonic swapping (parallel assignment) not working? Following (normal swapping) works:
        '''
        temp = node.next
        node.next = node.next.next
        temp.next = node
        '''
        # Wait, tried to change the order, and it works! Why exactly if assignment is being done parallely anyway?
        # [Create PR]
        node.next.next, node.next = node, node.next.next  # swap nodes by changing pointers
        # (Looks like we need to assign farther pointers before.)
        # node, node.next = node.next, node.next.next if node.next and node.next.next else node.next  # ++, beforehand
        # change next of last node if 2 nodes are still there (dry run on LL with len 4 at least to understand what's 
        # going on)
        # Why is pythonic swapping (parallel assignment) not working? Following (normal swapping) works:
        '''
        temp = node.next
        if node.next and node.next.next:  # if 2 nodes are still there
            node.next = node.next.next  # beforehand change next of last node
        node = temp  # ++
        '''
        # Wait, tried to change the order, and it works! Why exactly if assignment is being done parallely anyway?
        # [Create PR]
        node.next, node = node.next.next if node.next and node.next.next else node.next, node.next  # ++, beforehand
        # change next of last node if 2 nodes are still there (dry run on LL with len 4 at least to understand what's 
        # going on)
        # (Looks like we need to assign farther pointers before.)
    return head
    """
    # (Without Extra Comments):
    """
    if not head or not head.next:  # edge cases
        return head

    node, head = head, head.next  # `node`: for traversal, `head`: new head
    while node and node.next:  # while 2 nodes are there
        node.next.next, node.next = node, node.next.next  # swap nodes by changing pointers
        node.next, node = node.next.next if node.next and node.next.next else node.next, node.next  # ++, beforehand
        # change next of last node if 2 nodes are still there (dry run on LL with len 4 at least to understand what's
        # going on)
    return head
    """

    # Little easier with a dummy node:
    to_head = node = ListNode(next_=head)  # `to_head`: ptr to new_head; `node`: traverse and change pointers
    while node.next and node.next.next:  # while 2 nodes are there
        node.next.next.next, node.next.next, node.next = node.next, node.next.next.next, node.next.next  # swap nodes by
        # changing pointers (3)
        node = node.next.next  # +2
    return to_head.next
