"""
https://leetcode.com/problems/reverse-linked-list
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_


def reverse_list(head: ListNode | None) -> ListNode | None:
    """"""

    # 0) Brute-force (Changing the Values using Stack): TC = O(n); SC = O(n)

    """
    # Saving:
    curr = head  # not using head for traversing because we've to return head
    stack = []
    while curr:
        stack.append(curr.val)
        curr = curr.next  # ++

    # Changing:
    curr = head
    for i in range(len(stack)):  # traversing the stack
        curr.val = stack.pop()
        curr = curr.next  # ++

    return head
    """

    # 1) Optimal (Changing the Direction of Pointers): TC = O(n); SC = O(1)
    # https://media.geeksforgeeks.org/wp-content/cdn-uploads/RGIF2.gif
    # https://leetcode.com/problems/reverse-linked-list/discuss/58127/Python-Iterative-and-Recursive-Solution

    # Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?

    # 1.2) It can also be done Recursively: TC = O(n); SC = O(n) {recursion stack}
    # O(n) space, still writing, why? For Recursion practice!
    """
    # Recursive Function:
    def reverse(curr, prev=None) -> ListNode | None:
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
# https://leetcode.com/problems/reverse-nodes-in-even-length-groups
# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list
