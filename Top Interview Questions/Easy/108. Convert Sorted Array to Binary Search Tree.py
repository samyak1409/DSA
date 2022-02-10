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

    # Recursive Binary Search Algorithm: TC = O(n); SC = O(h) (height of BST) = O(n) in worst case and O(log n) in best case

    def construct(l, r):  # recursive function

        if l > r:  # base condition: if no more elements are left
            return None

        m = (l + r) // 2  # mid index
        node = TreeNode(nums[m])  # node init
        node.left = construct(l, m-1)  # left subtree construction by recursion
        node.right = construct(m+1, r)  # right subtree construction by recursion
        return node  # root node

    return construct(l=0, r=len(nums)-1)
