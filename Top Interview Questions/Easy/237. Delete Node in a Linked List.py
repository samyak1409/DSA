"""
https://leetcode.com/problems/delete-node-in-a-linked-list/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def deleteNode(node):
    """
    :type node: ListNode
    :rtype: void Do not return anything, modify node in-place instead.
    """

    # Naive 🤦‍♂️: TC = O(n); SC = O(1)

    """
    while True:
        node.val = node.next.val
        if node.next.next:
            node = node.next
        else:
            break
    node.next = None
    """

    # 👌: TC = O(1); SC = O(1)

    node.val = node.next.val  # copying value
    node.next = node.next.next  # changing pointer
