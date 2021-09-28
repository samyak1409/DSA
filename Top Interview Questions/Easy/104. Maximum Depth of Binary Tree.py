"""
https://leetcode.com/problems/maximum-depth-of-binary-tree/
"""


from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxDepth(root: Optional[TreeNode]) -> int:

    # Using Queue:

    queue = [root]
    height = -1

    while queue:

        height += 1
        temp = []

        for node in queue:
            if node:
                temp.extend([node.left, node.right])

        queue = temp

    return height
