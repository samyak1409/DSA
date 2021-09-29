"""
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
"""


from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sortedArrayToBST(nums: List[int]) -> Optional[TreeNode]:

    # Using Recursive Binary Search Algorithm:

    def construct(l, h):  # recursive function

        if l <= h:  # elements left

            m = (l+h) // 2  # mid index

            node = TreeNode(nums[m])  # node init

            node.left = construct(l, m-1)  # left subtree construction by recursion

            node.right = construct(m+1, h)  # right subtree construction by recursion

            return node  # root node

    return construct(0, len(nums)-1)
