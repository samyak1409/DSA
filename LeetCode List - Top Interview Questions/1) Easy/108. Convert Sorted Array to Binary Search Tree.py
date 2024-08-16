"""
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sorted_array_to_bst(nums: list[int]) -> TreeNode | None:

    # Recursive Binary Search Algorithm: 
    # TC = O(n); SC = O(h) (height of BST) = O(n) in worst case and O(log2(n)) in best case
    # https://en.wikipedia.org/wiki/Binary_search_algorithm#Procedure

    def construct(lt: int = 0, rt: int = len(nums)-1) -> TreeNode | None:  # recursive function

        if lt > rt:  # base condition: if no more elements are left
            return

        m = (lt + rt) // 2  # mid index
        node = TreeNode(nums[m])  # node init
        node.left = construct(lt, m-1)  # left subtree construction by recursion
        node.right = construct(m+1, rt)  # right subtree construction by recursion
        return node  # root node

    return construct()
