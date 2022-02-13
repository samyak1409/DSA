"""
https://leetcode.com/problems/intersection-of-two-linked-lists/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def getIntersectionNode(head1: ListNode, head2: ListNode) -> ListNode:

    # 0) Brute-force (TLE): TC = O(mn); SC = O(1)

    """
    while head1:
        while head2:
            if head1 == head2:
                return head1
            head2.next = head2
        head1.next = head1
    """

    # 1) Time-optimized Brute-force (AC): TC = O(m+n); SC = O(m)

    """
    saved = set()  # WHY SET? -> allows lookup in O(1) on an avg!
    while head1:
        saved.add(head1)
        head1 = head1.next

    while head2:
        if head2 in saved:  # O(1)
            return head2
        head2 = head2.next
    """

    # 2) Efficient: TC = O(n); SC = O(1)

    """
    # Calculating lengths m and n:
    copy1 = head1
    m = 0
    while copy1:
        m += 1
        copy1 = copy1.next
    copy2 = head2
    n = 0
    while copy2:
        n += 1
        copy2 = copy2.next

    # Skipping the nodes which are extra in the longer list:
    if m > n:
        for _ in range(m-n):
            head1 = head1.next
    elif m < n:
        for _ in range(n-m):
            head2 = head2.next

    # Now len(listA) = len(listB); so now comparing them to find the intersection:
    while head1:  # or "while head2" (doesn't matter coz len is same now)
        if head1 == head2:
            return head1
        head1, head2 = head1.next, head2.next
    """

    # 3) Thug https://leetcode.com/problems/intersection-of-two-linked-lists/discuss/49785/Java-solution-without-knowing-the-difference-in-len!: TC = O(n); SC = O(1)

    if head1 and head2:  # if both lists are not empty

        copy1, copy2 = head1, head2

        while copy1 != copy2:
            # Traversing till the end of the lists and then swapping the heads and traversing again till intersection is founded! (LOGIC-> "a, b += b, a" equates a and b):
            copy1 = copy1.next if copy1 else head2
            copy2 = copy2.next if copy2 else head1

        return copy1
