"""
https://leetcode.com/problems/root-equals-sum-of-children
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def check_tree(root: TreeNode | None) -> bool: return root.val == root.left.val + root.right.val
