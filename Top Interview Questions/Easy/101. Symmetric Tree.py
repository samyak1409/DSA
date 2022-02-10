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

    # Recursive <3:
    # TC = O(n)
    # SC = O(h) (height of the binary tree)
    # = O(n) in worst case (https://leetcode.com/problems/symmetric-tree/discuss/33050/Recursively-and-iteratively-solution-in-Python/1261395)
    # and = O(log n) in best case

    def are_symmetric(l_node, r_node):

        if not (l_node or r_node):  # base condition: no more nodes are there
            return True

        if l_node and r_node and l_node.val == r_node.val:
            return are_symmetric(l_node.left, r_node.right) and are_symmetric(l_node.right, r_node.left)

        # return False  # optional, because None is returned by default

    return are_symmetric(root.left, root.right)
