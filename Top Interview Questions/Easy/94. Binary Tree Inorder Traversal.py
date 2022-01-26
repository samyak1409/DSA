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


def inorderTraversal(root: Optional[TreeNode]) -> List[int]:  # TC = O(n); SC = O(n) (Best Case: O(log n))

    # 1) Using Recursion:

    """
    vals = []

    def inorder(node):
        if node:
            inorder(node.left)
            vals.append(node.val)
            inorder(node.right)

    inorder(root)

    return vals
    """

    # 2) Using Iteration: (How to approach this? Just try to build the exact same program flow (like recursion algo) using iterations! (not hard))

    stack, vals = [], []

    while True:

        while root:  # traversing till the most left node
            stack.append(root)
            root = root.left

        if stack:  # if any left nodes are there
            root = stack.pop()  # taking last left node
            vals.append(root.val)  # considering its value
            root = root.right  # check for its right node now
        else:  # no nodes left to traverse
            return vals
