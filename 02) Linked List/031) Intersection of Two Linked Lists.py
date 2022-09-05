"""
https://leetcode.com/problems/intersection-of-two-linked-lists
"""


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def get_intersection_node(head1: ListNode, head2: ListNode) -> Optional[ListNode]:
    """"""

    # All the 4 Solutions:
    # https://youtu.be/u4FWXfgS8jw
    # https://leetcode.com/problems/intersection-of-two-linked-lists/discuss/1093014/C++-Four-different-solutions

    # 0) [TLE] Brute-force (Nested Loop): TC = O(m*n); SC = O(1)
    # For every node of LL1: Traverse LL2.

    """
    while head1:
        head2_ = head2  # copy ref for traversals
        while head2_:
            if head1 == head2_:
                return head1  # or return head2_
            head2_ = head2_.next  # ++
        head1 = head1.next  # ++
    """

    # 1) Better (HashSet): TC = O(m+n); SC = O(m) or O(n)

    """
    nodes = set()  # set for O(1) lookup
    while head1:
        nodes.add(head1)
        head1 = head1.next  # ++

    while head2:  # O(n)
        if head2 in nodes:  # O(1)
            return head2
        head2 = head2.next  # ++
    """

    # Follow up: Could you write a solution that runs in O(m+n) time and use only O(1) memory?

    # 2.1) Optimal (Calc. Lengths): TC = O(m+n); SC = O(1)
    # https://leetcode.com/problems/intersection-of-two-linked-lists/discuss/49792/Concise-JAVA-solution-O(1)-memory-O(n)-time

    """
    # Helper Function:
    def get_len(head: ListNode) -> int:
        length = 1  # len will be at least one as per the Q. constraint
        while head := head.next:
            length += 1
        return length

    # Calculating lengths m and n:
    m, n = get_len(head=head1), get_len(head=head2)

    # Skipping the nodes which are extra in the longer list:
    if m > n:
        for _ in range(m-n):
            head1 = head1.next  # ++
    elif m < n:
        for _ in range(n-m):
            head2 = head2.next  # ++

    # Now len(list1) = len(list2); so now comparing them to find the intersection:
    while head1:  # or while head2 (doesn't matter coz len is same now)
        if head1 == head2:
            return head1  # or return head2
        head1, head2 = head1.next, head2.next  # ++
    """

    # 2.2) Optimal (Swap LL at End): TC = O(m+n); SC = O(1)
    # Traverse till the end of LLs and then continue traverse with swapped heads till intersection is not found!
    # Proof: `a, b += b, a` equates a & b
    # https://leetcode.com/problems/intersection-of-two-linked-lists/discuss/49785/Java-solution-without-knowing-the-difference-in-len!
    # https://leetcode.com/problems/intersection-of-two-linked-lists/discuss/49785/Java-solution-without-knowing-the-difference-in-len!/165648

    node1, node2 = head1, head2  # copy ref for traversal
    while node1 != node2:
        node1 = node1.next if node1 else head2
        node2 = node2.next if node2 else head1
    return node1  # or return node2


# Similar Question: https://leetcode.com/problems/minimum-index-sum-of-two-lists
