"""
https://leetcode.com/problems/linked-list-cycle/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def hasCycle(head: ListNode) -> bool:

    # 0) Using HashSet: TC = O(n); SC = O(n)

    """
    occurred = set()

    while head not in occurred:  # TC of "in" = O(1) because HashSet
        occurred.add(head)  # store this node
        try:
            head = head.next  # go to next node
        except AttributeError:  # reached end of the list
            return False  # no cycle

    return True  # node was in occurred => cycle is there
    """

    # 1) Floyd's Slow and Fast Pointer Approach <3 (https://en.wikipedia.org/wiki/Cycle_detection#Floyd's_tortoise_and_hare): TC = O(n); SC = O(1)

    slow = fast = head  # at first both pointing at head

    while fast and fast.next:  # while not reached the end of the linked list

        slow = slow.next  # 1 move
        fast = fast.next.next  # 2 moves

        if fast == slow:  # if they end up on some same node anytime
            return True  # loop is there

    return False  # else not

    # Also read: https://leetcode.com/problems/linked-list-cycle/discuss/44494/Except-ionally-fast-Python 👌
