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

    # Using Queue: TC = O(n); SC = O(log n)

    queue = [root]
    height = -1

    while queue:  # O(h), h being the height of the binary tree

        height += 1

        queue_copy = queue.copy()  # will run {no. of nodes on a particular level in the binary tree} times; "queue.copy()" / "queue[:]" -> new copy ✔

        queue.clear()

        for node in queue_copy:
            if node:
                queue.extend([node.left, node.right])

    return height
