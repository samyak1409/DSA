"""
https://leetcode.com/problems/middle-of-the-linked-list
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_


def middle_node(head: ListNode | None) -> ListNode | None:
    """"""

    # 0) Brute-force (One Pass: Copying the nodes to an array): TC = O(n); SC = O(n)

    """
    nodes = []
    while head:
        nodes.append(head)
        head = head.next
    return nodes[(len(nodes)//2)]
    """
    # Using Assignment Expression:
    """
    nodes = [head]
    while head := head.next:
        nodes.append(head)
    return nodes[(len(nodes)//2)]
    """

    # 1) Better (Two Pass: Calc Len): TC = O(n); SC = O(1)

    """
    node = head  # copy
    n = 0
    while node:
        n += 1
        node = node.next
    for _ in range(n//2):
        head = head.next
    return head
    """
    # Using Assignment Expression:
    """
    node = head  # copy
    n = 1
    while node := node.next:
        n += 1
    for _ in range(n//2):
        head = head.next
    return head
    """

    # 2) Optimal (One Pass: Slow and Fast Pointer): TC = O(n); SC = O(1)
    # Video Explanation:
    # https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4426

    """
    slow = fast = head
    while fast and fast.next:
        slow = slow.next  # +1
        fast = fast.next.next  # +2
    return slow
    """
    # Using `head` only as slow:
    fast = head
    while fast and fast.next:
        head = head.next  # +1
        fast = fast.next.next  # +2
    return head


# Similar Questions:
# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list
# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list
