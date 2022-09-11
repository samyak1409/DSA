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
        node.next.next, node.next = node, node.next.next  # swap nodes by changing pointers
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
        '''
        temp = node.next
        node.next = node.next.next
        temp.next = node
        '''
        node.next.next, node.next = node, node.next.next  # swap nodes by changing pointers
        # SO, HERE WE LEARNT A VERY IMPORTANT LESSON, THAT HOW `A, B = C, D` WORKS.
        # I USED TO THINK ASSIGNMENT TAKES PLACE PARALLELY BECAUSE OF THE FACT THAT USING THIS STRUCTURE, WE CAN SWAP
        # DATA OF TWO OBJECTS IN PYTHON (`A, B = B, A`). BUT NO, ASSIGNMENT DOESN'T TAKE PLACE PARALLELY. 😶
        # {MY WHOLE LIFE (2 YEARS OF PYTHON) WAS A LIE} THEN HOW DOES IT FREAKING WORK? LET'S SEE!
        # FIRST OF ALL THE RHS GETS EXECUTED (AS WE ALREADY KNOW), COPY OF EVERY OBJECT (IN OUR CASE `C` & `D`) TAKES 
        # PLACE (COPY MEANS NEW ADDRESS AND SO NEW MEMORY IS ASSIGNED), AND THEN THEIR TUPLE IS FORMED.
        # THEN, TUPLE UNPACKING ASSIGNMENT TAKES PLACE, I.E., ONE BY ONE (FROM LEFT TO RIGHT TO BE EXTRA-DEFINITIVE) ALL
        # THE OBJECTS ON THE LHS ARE ASSIGNED TO THE CORRESPONDING RHS TUPLE DATA.
        # AND THAT'S HOW IT WORKS!
        # node, node.next = node.next, node.next.next if node.next and node.next.next else node.next  # ++, beforehand
        # change next of last node if 2 nodes are still there (dry run on LL with len 4 at least to understand what's 
        # going on)
        '''
        temp = node.next
        if node.next and node.next.next:  # if 2 nodes are still there
            node.next = node.next.next  # beforehand change next of last node
        node = temp  # ++
        '''
        node.next, node = node.next.next if node.next and node.next.next else node.next, node.next  # ++, beforehand
        # change next of last node if 2 nodes are still there (dry run on LL with len 4 at least to understand what's 
        # going on)
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
