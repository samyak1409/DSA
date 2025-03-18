"""
https://leetcode.com/problems/rotate-list
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_


def rotate_right(head: ListNode | None, k: int) -> ListNode | None:
    """"""

    # 0) [TLE] Brute-force (Rotate One by One k Times): TC = O(k*n); SC = O(1)

    # 1) Optimal (Directly Go to Required Nodes (2) and Change Pointers): TC = O(n); SC = O(1)

    # 1.1) Calc len, Make cycle, Fix k (if required), Go to (n-k-1)-th node, and Unlink the next ptr:
    # TC = O(n + n-k`) {k` = k % n}
    # https://youtu.be/9VPm6nEbVPA?t=242
    # https://leetcode.com/problems/rotate-list/discuss/348197/96-faster-Simple-python-solution-with-explanation

    """
    if not head:  # edge case
        return None

    # Calc len:
    node = head  # copy for traversing
    n = 1
    while node.next:
        n += 1
        node = node.next  # ++

    # Now the `node` will be the last node in our LL, linking it to the first node (this will make a cycle):
    node.next = head

    # Fix k if required (basically remove duplicate rotations):
    k %= n

    # Move `head` to (n-k-1)-th node:
    for _ in range(n-k-1):
        head = head.next  # ++
    
    # Unlink, new head:
    head.next, head = None, head.next

    return head
    """

    # 1.2) Assume k < n and continue solving for this case, meanwhile calc the length, and if reach end, call function
    # again with fixed k:
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

    # Note - `1.1)` is better in general as it's straight-forward. `1.2)` is a bit advanced version of that.


# Similar Questions:
# https://leetcode.com/problems/rotate-array
# https://leetcode.com/problems/split-linked-list-in-parts
