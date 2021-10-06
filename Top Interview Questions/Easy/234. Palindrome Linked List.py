"""
https://leetcode.com/problems/palindrome-linked-list/
"""


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def isPalindrome(head: Optional[ListNode]) -> bool:

    # Step 1: Traversing half of the nodes and reversing the pointers!

    slow = fast = head
    prev = None

    while fast and fast.next:  # using a fast pointer ✔

        fast = fast.next.next  # +2

        # https://leetcode.com/problems/reverse-linked-list/:
        copy = slow
        slow = slow.next  # +1
        copy.next = prev
        prev = copy

    # after this loop, "1 -> 2 -> 2 -> 1 -> None" will convert into "None <- 1 <- 2 and 2 -> 1 -> None"
    # and prev will be pointing to left linked list and slow to right!

    if fast:  # if linked list has odd number of nodes
        slow = slow.next  # skipping the middle node

    # Step 2: Matching the values!

    while prev:  # or slow (len is same)

        if prev.val != slow.val:
            return False

        prev, slow = prev.next, slow.next

        # note that if it was given in the Q. that "without modifying the linked list", that's is also possible, we would have been just reversed the half reversed linked list back here while matching the values!

    return True
