"""
https://leetcode.com/problems/rotate-list
"""


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_


def rotate_right(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    """"""

    # 0) [TLE] Brute-force (Rotate One by One k Times): TC = O(k*n); SC = O(1)

    # 1) Optimal (Directly Go to Required Nodes (2) and Change Pointers): TC = O(n); SC = O(1)

    # 1.1) Calc Len, Make Cycle, Fix k (if required), Go to (n-k)-th Node and Unlink the next Ptr:
    # TC = O(n + n-k`) {k` = k % n}
    # https://youtu.be/9VPm6nEbVPA?t=242
    # https://leetcode.com/problems/rotate-list/discuss/348197/96-faster-Simple-python-solution-with-explanation

    """
    if not head:  # edge case
        return

    # Calc Len:
    node = head  # copy for traversing
    n = 1
    while node.next:
        n += 1
        node = node.next  # ++

    # Now the `node` will be the last node in our LL, linking it to the first node (this will make a cycle):
    node.next = head

    # Fix k (if required) (basically remove duplicate rotations):
    k %= n

    # Go to (n-k)-th node and unlink the next ptr (in order to get the Rotated List):
    for _ in range(n-k):
        node = node.next  # ++
    node.next, head = None, node.next  # unlink, new_head

    return head
    """

    # 1.2) Assume k < n and Continue Solving for this Case, Meanwhile Calc the Length, and if Reach End, Call Function
    # again with Fixed k:
    # TC = O(n) if (k < n) else O(n+n)
    # -> This approach uses Two Pointers.

    if not head or not k:  # edge cases
        return head

    n = 0

    # Assuming k < n:
    try:
        # Go to (k+1)-th node and meanwhile track len:
        old_last = head  # copy for traversing
        for _ in range(k):
            # (if k >= n, AttributeError will be raised here:)
            old_last = old_last.next  # ++
            n += 1

        # Go to (n-k)-th & n-th node using two pointers:
        new_last = head
        while old_last.next:
            new_last, old_last = new_last.next, old_last.next  # ++

        # Change pointers:
        old_last.next, new_last.next, head = head, None, new_last.next  # link, unlink, new_head

        return head

    except AttributeError:  # => k >= n
        # Call again with fixed k:
        return rotate_right(head, k % n)
        # return self.rotateRight(head, k % n)


# Similar Questions:
# https://leetcode.com/problems/rotate-array
# https://leetcode.com/problems/split-linked-list-in-parts
