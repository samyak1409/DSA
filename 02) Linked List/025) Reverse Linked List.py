"""
https://leetcode.com/problems/reverse-linked-list
"""


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """"""

    # 0) Brute-force (Changing the Values): TC = O(n); SC = O(n)

    """
    # Saving:
    curr = head  # copying head coz singly LL
    vals = []
    while curr:
        vals.append(curr.val)
        curr = curr.next  # ++

    # Changing:
    curr = head
    for i in range(-1, -len(vals)-1, -1):  # reverse traverse the saved vals
        curr.val = vals[i]
        curr = curr.next  # ++

    return head
    """

    # 1) Optimal (Changing the Direction of Pointers): TC = O(n); SC = O(1)
    # https://media.geeksforgeeks.org/wp-content/cdn-uploads/RGIF2.gif
    # https://leetcode.com/problems/reverse-linked-list/discuss/58127/Python-Iterative-and-Recursive-Solution

    # 1.2) It can also be done Recursively: TC = O(n); SC = O(n) {recursion stack}
    # O(n) space, still writing, why? For Recursion practice!
    """
    def reverse(curr, prev=None):
        # '''Recursively reverses a singly LL and returns the head node.'''
        if not curr:  # base case: traversed whole LL
            return prev  # as the direction of pointers are reversed, `prev` (last node) basically is head now!
        next_curr = curr.next  # save ref to the next of curr node for updating in the end
        curr.next = prev  # reverse the pointer direction from next to prev node
        return reverse(curr=next_curr, prev=curr)  # recurse with updated `curr` & `prev`

    return reverse(curr=head)
    """

    # 1.1) Iteratively:
    """
    prev = None  # at first (as the end of LL is `None`)

    while head:  # iterate till the end

        next_head = head.next  # save ref to the next of curr node (`head`) for updating in the end
        head.next = prev  # reverse the pointer direction from next to prev node

        prev = head  # update the prev node
        head = next_head  # move the head node to the next

    return prev  # as the direction of pointers are reversed, `prev` (last node) basically is head now!
    """
    # In short:
    prev = None  # at first (as the end of LL is `None`)
    while head:  # iterate till the end
        head.next, head, prev = prev, head.next, head  # reverse ptr direction + update `head` + update `prev`
    return prev  # as the direction of pointers are reversed, `prev` (last node) basically is head now!


# Similar Questions:
# https://leetcode.com/problems/reverse-linked-list-ii
# https://leetcode.com/problems/palindrome-linked-list
