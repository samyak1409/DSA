"""
https://leetcode.com/problems/linked-list-cycle/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def hasCycle(head: ListNode) -> bool:

    # Slow and Fast Pointer Approach <3 (https://en.wikipedia.org/wiki/Cycle_detection#Floyd's_tortoise_and_hare): TC = O(n); SC = O(1)

    slow = fast = head  # at first both pointing at head

    while fast and fast.next:  # while not reached the end of the linked list

        slow = slow.next  # 1 move
        fast = fast.next.next  # 2 moves

        if fast == slow:  # if they end up on some same node anytime
            return True  # loop is there

    return False  # else not
