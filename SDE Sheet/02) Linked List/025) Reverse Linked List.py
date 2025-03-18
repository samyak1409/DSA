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
    node = head  # not using head for traversing because we've to return head
    stack = []
    while node:
        stack.append(node.val)
        node = node.next  # ++

    # Changing:
    node = head
    for i in range(len(stack)):  # traversing the stack
        node.val = stack.pop()
        node = node.next  # ++

    return head
    """

    # 1) Optimal (Changing the Direction of Pointers): TC = O(n); SC = O(1)
    # https://media.geeksforgeeks.org/wp-content/cdn-uploads/RGIF2.gif
    # https://leetcode.com/problems/reverse-linked-list/solutions/58127/python-iterative-and-recursive-solution

    # Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?

    # 1.2) It can also be done Recursively: TC = O(n); SC = O(n) {recursion stack}
    # O(n) space, still writing, why? For Recursion practice!

    """
    # Recursive Function:
    def reverse(node: ListNode | None, prev: ListNode | None) -> ListNode | None:
        # '''Recursively reverses a singly LL and returns the head node.'''
        if not node:  # base case: traversed whole LL
            return prev  # as the direction of pointers are reversed, `prev` (last node) basically is head now!
        nxt = node.next  # save ref to the next of curr node for updating in the end
        node.next = prev  # reverse the pointer direction from next to prev node
        return reverse(node=nxt, prev=node)  # recurse with updated `node` & `prev`

    return reverse(node=head, prev=None)
    """

    # We can also do it this way:
    # MAIN DIFF: Above, we're reversing the ptr direction while recursing in, here we're doing that while recursing out.
    """
    # Recursive Function:
    def reverse(node: ListNode | None, prev: ListNode | None) -> ListNode | None:
        if not node:  # base case: traversed whole LL
            return prev  # return the last node of the LL, it'd be the head of our reversed LL
        ans = reverse(node=node.next, prev=node)  # recurse in with next values, it'd return the head of reversed LL
        node.next = prev  # change the ptr direction; IMP: this is while recursing out
        return ans  # at the end, return the head of reversed LL

    return reverse(node=head, prev=None)
    """

    # 1.1) Iteratively:
    """
    prev = None  # at first (as the end of LL is `None`)
    while head:  # iterate till the end
        nxt = head.next  # save ref to the next of curr node (`head`) for updating in the end
        head.next = prev  # reverse the pointer direction from next to prev node
        prev = head  # update the prev node
        head = nxt  # move the head node to the next
    return prev  # as the direction of pointers are reversed, `prev` (last node) basically is head now!
    """

    # In short:
    prev = None  # at first (as the end of LL is `None`)
    while head:  # iterate till the end
        head.next, prev, head = prev, head, head.next  # reverse ptr direction + update `prev` + update `head`
    return prev  # as the direction of pointers are reversed, `prev` (last node) basically is head now!


# Similar Questions:
# https://leetcode.com/problems/reverse-linked-list-ii
# https://leetcode.com/problems/palindrome-linked-list
# https://leetcode.com/problems/reverse-nodes-in-even-length-groups
# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list
