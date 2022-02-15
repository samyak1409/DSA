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

    # 1) Straightforward: TC = O(n); SC = O(n)

    """
    vals = []
    node = head
    while node:
        vals.append(node.val)
        node = node.next
    n = len(vals)
    return vals[:n//2] == vals[(n//2)+(n%2):][::-1]  # (n % 2) = (0 if n % 2 == 0 else 1)
    # or simply:
    # return vals == vals[::-1]  # (O(n/2) = O(n))
    """

    # 2) Reversing 1st-half linked list: TC = O(n); SC = O(1)

    # https://leetcode.com/problems/palindrome-linked-list/discuss/64500/11-lines-12-with-restore-O(n)-time-O(1)-space

    # Step 1: Traversing half of the nodes and reversing the pointers!

    slow = fast = head
    prev = None

    while fast and fast.next:  # using a fast pointer ✔

        fast = fast.next.next  # +2

        # https://leetcode.com/problems/reverse-linked-list:

        n = slow.next  # saving ref to the next of cur node
        slow.next = prev  # changing the pointer direction from next to prev node (reversing)

        prev = slow  # updating the prev node
        slow = n  # +1; moving the slow node to the next

    # after this loop, "1 -> 2 -> 2 -> 1 -> None" will convert into "None <- 1 <- 2 and 2 -> 1 -> None"
    # and prev will be pointing to left linked list and slow to right!

    if fast:  # if linked list has odd number of nodes
        slow = slow.next  # skipping the middle node

    # Step 2: Matching the values!

    while prev:  # or slow (len is same)

        if prev.val != slow.val:
            return False

        prev, slow = prev.next, slow.next

        # NOTE: if it was given in the Q. that "without modifying the linked list", that's also possible, we can just reverse the half-reversed linked list back here while matching the values!

    return True
