"""
https://leetcode.com/problems/symmetric-tree/
"""


from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSymmetric(root: Optional[TreeNode]) -> bool:

    # Recursion <3:

    def are_symmetric(node1, node2):
        """Returns whether node1 and node2 are symmetric."""

        if not node1 and not node2:
            return True

        if (node1 and node2) and (node1.val == node2.val):
            return are_symmetric(node1.left, node2.right) and are_symmetric(node1.right, node2.left)

        return False

    return are_symmetric(root.left, root.right)
