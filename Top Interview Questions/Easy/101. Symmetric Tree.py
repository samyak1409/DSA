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

    # Recursion <3: TC = O(n); SC = O(h), h being the height of the binary tree

    def are_symmetric(l_node, r_node):
        """Returns whether l_node and r_node are symmetric."""

        if not l_node and not r_node:
            return True

        if (l_node and r_node) and (l_node.val == r_node.val):
            return are_symmetric(l_node.left, r_node.right) and are_symmetric(l_node.right, r_node.left)

        return False

    return are_symmetric(root.left, root.right)
