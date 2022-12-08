"""
https://leetcode.com/problems/reverse-nodes-in-even-length-groups
"""


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_


def reverse_even_length_groups(head: Optional[ListNode]) -> Optional[ListNode]:
    """"""

    # All the solutions are (modifications of the solutions) from
    # https://github.com/samyak1409/DSA/blob/main/02%29%20Linked%20List/025%29%20Reverse%20Linked%20List.py.

    # 1) Optimal (Changing the Direction of Pointers): TC = O(n); SC = O(1)
    # -> One Pass

    curr = counter = head  # not using head for traversing because we've to return head;
    # `counter` will go ahead and help checking the length of a group
    expected_len = 1  # "groups whose lengths form the sequence of the natural numbers (1, 2, 3, 4, ...)"
    before = None

    # Loop for/on groups:
    while curr:

        # Checking the length of group:
        real_len = 0
        for _ in range(expected_len):
            try:  # EAFP (Easier to Ask for Forgiveness than Permission)
                counter = counter.next  # ++
            except AttributeError:  # => group length found less
                break
            real_len += 1

        # Main:
        if real_len % 2 == 0:  # => reverse group
            new_before = curr  # save ref for `before`
            # Basic `025 Reverse Linked List.py` Algo:
            prev = counter  # so that the first node in the group to be reversed will directly point to the first node
            # of next group (first node -> REVERSAL HAPPEN -> last node)
            for _ in range(real_len):
                curr.next, curr, prev = prev, curr.next, curr  # reverse ptr direction + update `curr` + update `prev`
            before.next = prev  # connecting the last node of the previous group to the first node (after reversal) of
            # the current group
            before = new_before  # save ref for next group
        else:  # (odd length group)
            # Just moving the `curr` forward:
            for _ in range(real_len-1):
                curr = curr.next  # ++
            before = curr  # save ref for next group
            curr = curr.next  # ++

        expected_len += 1

    return head
