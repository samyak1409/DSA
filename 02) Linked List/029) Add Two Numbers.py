"""
https://leetcode.com/problems/add-two-numbers
"""


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_


def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    """"""

    # 1) Optimal (Traverse and Add): TC = O(max(m, n)); SC = O(max(m, n))
    # https://leetcode.com/problems/add-two-numbers/solution
    # https://leetcode.com/problems/add-two-numbers/discuss/1835535/JavaC%2B%2B-A-very-beautiful-explanation-EVER-exists

    head = node = ListNode()  # init head node; `head` -> save ref to head to return
    carry = 0
    while True:  # do while loop
        sum_ = carry
        if l1:
            sum_ += l1.val
            l1 = l1.next  # ++
        if l2:
            sum_ += l2.val
            l2 = l2.next  # ++
        node.val = sum_ % 10  # assign 1 digit sum (sum without carry)
        carry = sum_ // 10  # save (update) carry
        if l1 or l2 or carry:
            node.next = ListNode()  # init next node
            node = node.next  # ++
        else:
            return head


# Similar Questions:
# https://leetcode.com/problems/multiply-strings
# https://leetcode.com/problems/add-binary
# https://leetcode.com/problems/sum-of-two-integers
# https://leetcode.com/problems/add-strings
# https://leetcode.com/problems/add-two-numbers-ii
# https://leetcode.com/problems/add-to-array-form-of-integer
