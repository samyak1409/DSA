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

    # 1.1) Calculate Len, Fix k, Go to (k+1)-th Node & Change Pointer, and from there, Go to Last Node & Change Pointer:
    """
    if not head or not k or not head.next:  # edge cases
        return head

    # Find the len of LL:
    node = head
    n = 0
    while node:
        n += 1
        node = node.next  # ++

    k %= n  # remove duplicate rotations
    if not k:
        return head

    # Go to the required nodes and change the pointers:
    new_head = head
    for _ in range(n-k-1):
        new_head = new_head.next  # ++
    new_head.next, new_head = None, new_head.next
    last_node = new_head
    while last_node.next:
        last_node = last_node.next  # ++
    last_node.next = head

    return new_head
    """
    # 1.2) Calculate Len and Save Ref to Last Node, Fix k, Change Old Last Node Pointer, Go to (k+1)-th Node & Change
    #      New Last Node Pointer:
    # https://youtu.be/9VPm6nEbVPA?t=242
    # https://leetcode.com/problems/rotate-list/discuss/348197/96-faster-Simple-python-solution-with-explanation
    """
    if not head or not k or not head.next:  # edge cases
        return head

    # Find the len of LL and save ref to last node:
    last_node = head
    n = 1
    while last_node.next:
        n += 1
        last_node = last_node.next  # ++

    k %= n  # remove duplicate rotations
    if not k:
        return head

    # Change old last pointer, go to (n-k)-th node, and change new last pointer:
    last_node.next = head
    for _ in range(n-k-1):
        head = head.next  # ++
    head.next, head = None, head.next

    return head
    """
    # 1.3) Assume k < n and Continue Solving for this Case, Meanwhile Calculating the Length, and if We Reach End, Call
    #      the Function Again with Fixed k:
    if not head or not k or not head.next:  # edge cases
        return head

    n = 0  # for k >= n cases
    # Assuming k < n:
    try:
        # Go to (k+1)-th node and meanwhile track len:
        last_node = head
        for _ in range(k):
            last_node = last_node.next  # ++
            n += 1
        # Go to (n-k)-th & last node using two pointers:
        new_head = head
        while last_node.next:
            new_head, last_node = new_head.next, last_node.next  # ++
        # Change pointers:
        new_head.next, new_head, last_node.next = None, new_head.next, head
        return new_head
    except AttributeError:
        # k >= n, calling again with fixed k:
        return rotate_right(head, k % n)
