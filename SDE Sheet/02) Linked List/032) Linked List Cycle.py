"""
https://leetcode.com/problems/linked-list-cycle
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def has_cycle(head: ListNode | None) -> bool:
    """"""

    # 1) Time-Optimal (HashSet): TC = O(n); SC = O(n)

    """
    seen = set()  # for O(1) lookup
    while head:  # while not reached at the end of LL
        seen.add(head)  # store this node
        if (head := head.next) in seen:
            return True
    return False  # reached at the end of LL => no cycle
    """
    # In Python, it's EAFP:
    """
    seen = set()  # for O(1) lookup
    while True:
        seen.add(head)  # store this node
        try:
            if (head := head.next) in seen:
                return True
        except AttributeError:
            return False  # reached at the end of LL => no cycle
    """

    # Follow up: Can you solve it using O(1) (i.e. constant) memory?

    # 2) Optimal (Floyd's Cycle-Finding Algorithm <3): TC = O(n); SC = O(1)
    # https://youtu.be/354J83hX7RI?t=253 (Striver)
    # https://en.wikipedia.org/wiki/Cycle_detection#Floyd%27s_tortoise_and_hare

    """
    slow = fast = head  # init
    while fast and fast.next:  # while not reached at the end of LL
        slow, fast = slow.next, fast.next.next  # +1, +2
        if fast == slow:  # if they end up on a same node anytime
            return True  # cycle is there
    return False  # reached at the end of LL => no cycle
    """
    # In Python, it's EAFP (https://leetcode.com/problems/linked-list-cycle/solutions/44494/Except-ionally-fast-Python):
    slow = fast = head  # init
    while True:
        try:
            slow, fast = slow.next, fast.next.next  # +1, +2
        except AttributeError:
            return False  # reached at the end of LL => no cycle
        if fast == slow:  # if they end up on a same node anytime
            return True  # cycle is there


# Similar Questions:
# https://leetcode.com/problems/linked-list-cycle-ii
# https://leetcode.com/problems/happy-number
