"""
https://leetcode.com/problems/binary-tree-inorder-traversal/
"""


from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorderTraversal(root: Optional[TreeNode]) -> List[int]:

    # Recursion:

    values = []

    def inorder_traverse(node):
        if node:
            inorder_traverse(node.left)
            values.append(node.val)
            inorder_traverse(node.right)

    inorder_traverse(root)

    return values
