"""
https://leetcode.com/problems/reverse-linked-list-ii
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_


def reverse_between(head: ListNode | None, left: int, right: int) -> ListNode | None:
    """"""

    # All the solutions are (modifications of the solutions) from
    # https://github.com/samyak1409/DSA/blob/main/02%29%20Linked%20List/025%29%20Reverse%20Linked%20List.py.

    # NOTE: `left` & `right` are 1-indexed!

    # 0) Brute-force (Changing the Values using Stack): TC = O(n); SC = O(n)

    """
    # Saving:
    curr = head  # not using head for traversing because we've to return head
    for _ in range(left-1):  # skipping nodes in the left
        curr = curr.next  # ++
    start = curr  # saving the start point (from where the nodes need to be reversed)
    stack = []
    for _ in range(right-left+1):  # saving the values in the range [left, right]
        stack.append(curr.val)
        curr = curr.next  # ++

    # Changing:
    for i in range(len(stack)):  # traversing the stack
        start.val = stack.pop()
        start = start.next  # ++

    return head
    """

    # Follow up: Could you do it in one pass?
    # 1) Optimal (Changing the Direction of Pointers): TC = O(n); SC = O(1)
    # It's Easy, just have to take care of the two different cases in which the algo will be a little different:
    # i) left is not at the start, e.g. (head=[1,2,3,4,5], left=2, right=4)
    # ii) left is at the start, e.g. (head=[1,2,3,4,5], left=1, right=3)
    # Dry run on paper to understand!
    # https://leetcode.com/problems/reverse-linked-list-ii/solution

    curr = head  # not using head for traversing because we've to return head
    # Skipping to the correct position:
    for _ in range(left-2):  # moving `curr` to the node just before `left`
        curr = curr.next  # ++

    # Saving required references:
    before = None
    if left != 1:  # (if `left` is not start of the list)
        before = curr  # saving ref to the node just before `left`
        curr = curr.next  # ++; now `curr` is at `left`
    first = curr  # saving ref to the first node from `left`
    # after reversal, this would be the last node among reversed ones

    # Basic `025 Reverse Linked List.py` Algo:
    prev = None
    for _ in range(right-left+1):
        curr.next, curr, prev = prev, curr.next, curr  # reverse ptr direction + update `curr` + update `prev`

    # Making required connections:
    if left != 1:  # (if `left` is not start of the list)
        before.next = prev  # connecting the node just before `left` to the last node whose pointer was reversed
    else:  # (list reversed right from the beginning)
        head = prev  # => we need to change the `head`, it will be the last node whose pointer was reversed
    first.next = curr  # connecting the first node which after reversing the pointers has become the last node among the
    # reversed ones to the node just after `right`

    return head
