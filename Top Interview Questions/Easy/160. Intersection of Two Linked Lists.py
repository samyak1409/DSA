"""
https://leetcode.com/problems/intersection-of-two-linked-lists/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def getIntersectionNode(head1: ListNode, head2: ListNode) -> ListNode:

    # Method 1 (Normal): TC = O(n); SC = O(1)

    """
    # Calculating lengths m and n:

    copyA = head1
    m = 0
    while copyA:
        m += 1
        copyA = copyA.next

    copyB = head2
    n = 0
    while copyB:
        n += 1
        copyB = copyB.next

    # Skipping the nodes which are extra in the longer list:

    if m > n:
        for _ in range(m-n):
            head1 = head1.next

    elif m < n:
        for _ in range(n-m):
            head2 = head2.next

    # Now len(listA) == len(listB); so now comparing them to find the intersection:

    while head1:  # or "while head2" (doesn't matter coz len is same now)

        if head1 == head2:
            return head1

        head1, head2 = head1.next, head2.next
    """

    # Method 2 (Thug https://leetcode.com/problems/intersection-of-two-linked-lists/discuss/49798/Concise-python-code-with-comments): TC = O(n); SC = O(1)

    """
    if head1 and head2:  # only if both lists are not empty

        A, B = head1, head2  # copy

        while A != B:
            # Traversing till the end of the lists and then swapping the heads and traversing again till intersection is founded! (LOGIC-> "a, b += b, a" equates a and b)
            A = A.next if A else head2
            B = B.next if B else head1

        return A
    """

    # Method 3: TC = O(n); SC = O(n) but still taking nearly same memory, HOW????

    saved = {}

    temp1, temp2 = head1, head2

    while temp1:
        saved[temp1] = None
        temp1 = temp1.next

    while temp2:

        if saved.get(temp2, 0) is None:
            return temp2

        temp2 = temp2.next
