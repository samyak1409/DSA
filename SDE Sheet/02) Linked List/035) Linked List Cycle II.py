"""
https://leetcode.com/problems/linked-list-cycle-ii
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def detect_cycle(head: ListNode | None) -> ListNode | None:
    """"""

    # All the solutions are (modifications of the solutions) from
    # https://github.com/samyak1409/DSA/blob/main/02%29%20Linked%20List/032%29%20Linked%20List%20Cycle.py.

    # 1) Time-Optimal (HashSet): TC = O(n); SC = O(n)

    """
    seen = set()  # for O(1) lookup
    while head:  # while not reached at the end of LL
        seen.add(head)  # store this node
        if (head := head.next) in seen:
            return head
    # return None  # reached at the end of LL => no cycle
    """
    # In Python, it's EAFP:
    """
    seen = set()  # for O(1) lookup
    while True:
        seen.add(head)  # store this node
        try:
            if (head := head.next) in seen:
                return head
        except AttributeError:
            return  # reached at the end of LL => no cycle
    """

    # Follow up: Can you solve it using O(1) (i.e. constant) memory?
    # 2) Optimal (Floyd's Cycle-Finding Algorithm <3): TC = O(n); SC = O(1)
    # https://youtu.be/QfbOhn0WZ88?t=324
    # https://en.wikipedia.org/wiki/Cycle_detection#Floyd%27s_tortoise_and_hare

    """
    # Checking whether the LL have cycle:
    slow = fast = head  # init
    while fast and fast.next:  # while not reached at the end of LL
        slow, fast = slow.next, fast.next.next  # +1, +2
        if fast == slow:  # if they end up on a same node anytime, cycle is there
            # Finding the start of cycle:
            while head != slow:
                head, slow = head.next, slow.next  # +1, +1
            return head  # or slow (they're =)
    # return None  # reached at the end of LL => no cycle
    """
    # In Python, it's EAFP:
    # Checking whether the LL have cycle:
    slow = fast = head  # init
    while True:
        try:
            slow, fast = slow.next, fast.next.next  # +1, +2
        except AttributeError:
            return  # reached at the end of LL => no cycle
        if fast == slow:  # if they end up on a same node anytime, cycle is there
            # Finding the start of cycle:
            while head != slow:
                head, slow = head.next, slow.next  # +1, +1
            return head  # or slow (they're =)

    # However, the main question arises here is, how can you prove that head & slow are bound to meet on the start of
    # the cycle?
    # Proof using Maths:
    # Let the distance b/w LL start & cycle start be `x`,
    #     the distance b/w cycle start & the node where the slow & fast meet be `y`,
    #     the total number of rounds completed by the fast pointer before slow & fast met be `n`
    # (slow and fast would meet for sure on the first round of slow on the cycle, so for slow, n = 0),
    # and the length of cycle be `c`.
    #
    # Then, the total distance covered by slow = x + y,
    #   and the total distance covered by fast = x + y + n*c
    # As fast was travelling at 2x speed of slow, we can say
    # 2 * distance(slow) = distance(fast)
    # => 2 * (x + y) = x + y + n*c
    # => x + y = n*c
    # => x = n*c - y
    # We can see that `n*c - y` gives us the distance b/w the node where the slow & fast meet and cycle start.
    # Hence, proved!


# Similar Questions:
# https://leetcode.com/problems/linked-list-cycle
# https://leetcode.com/problems/find-the-duplicate-number
