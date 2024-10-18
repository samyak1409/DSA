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
    """"""

    # 1) Optimal (Recursive Binary Search): TC = O(n); SC = O(h) = O(log2(n))

    # Can be shortened to as concise as:
    """
    def construct(lt: int, rt: int) -> TreeNode | None:
        return None if lt > rt else TreeNode(nums[(mid := (lt+rt)//2)], construct(lt, mid-1), construct(mid+1, rt))
    return construct(0, len(nums)-1)
    """

    # Recursive Function:
    def construct(lt: int, rt: int) -> TreeNode | None:

        if lt > rt:  # base condition: if no more elements are left in curr subarray
            return None  # (child node doesn't exist)

        mid = (lt+rt) // 2  # mid index
        node = TreeNode(nums[mid])  # init node
        node.left = construct(lt, mid-1)  # recurse to construct left subtree
        node.right = construct(mid+1, rt)  # recurse to construct right subtree
        return node  # assign to func caller LHS

    root = construct(0, len(nums)-1)
    return root
