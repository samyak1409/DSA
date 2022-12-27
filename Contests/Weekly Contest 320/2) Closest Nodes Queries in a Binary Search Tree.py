"""
https://leetcode.com/problems/closest-nodes-queries-in-a-binary-search-tree
"""


from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def closest_nodes(root: Optional[TreeNode], queries: list[int]) -> list[list[int]]:
    """"""

    # 0) [TLE] Brute-force (Do what's told, for every query, search the BST):
    # TC = O(n*h) where h: height = log(n) {Balanced BT}
    #                             = n      {Unbalanced (Skewed) BT}
    #    = O(n*log(n))     (Average Case)
    #    = O(n*n) = O(n^2) (Worst Case)
    # SC = O(1)
    # 36 / 37 test cases passed.
    # And guess what test case could be failing, SKEWED BINARY TREE!!
    # Problem Description doesn't mention anywhere that the Binary Tree will be BALANCED!!
    # So, we can have a Binary Tree like:
    #                                     5
    #                                      \
    #                                       5
    #                                        \
    #                                         5
    #                                          \
    #                                           5
    # 
    # Which will lead to O(n) Search TC, and not expected O(log(n))!

    """
    for query in queries:

        ans = [float('-inf'), float('inf')]  # ans. to this query

        # Search in BST:
        node = root  # copy for traversal
        while node:
            if (value := node.val) == query:  # => query val itself is present
                ans[:] = [query, query]  # so the ans will be itself only, because if the query is present in the tree,
                # then `largest val <= query` = `smallest val >= query` = query
                break
            if value < query:
                ans[0] = max(ans[0], value)  # `the largest value in the tree that is <= queries[i]`, so update
                node = node.right
            else:  # (value > query)
                ans[1] = min(ans[1], value)  # `the smallest value in the tree that is >= queries[i]`, so update
                node = node.left

        # `If such a value does not exist, add -1 instead.`:
        if ans[0] == float('-inf'):
            ans[0] = -1
        if ans[1] == float('inf'):
            ans[1] = -1

        yield ans
    """

    # So, to solve this problem, what can we do? We can simply make a sorted array from the BST, and then apply BS
    # on that array!
    # 1) Optimal (BST to Sorted Array; For Every Query, BS the Array): TC = O(n*log(n)); SC = O(n)
    # https://leetcode.com/problems/closest-nodes-queries-in-a-binary-search-tree/discuss/2831692/Is-the-tree-balanced

    # Preprocessing: BST to Sorted Array (https://www.geeksforgeeks.org/flatten-bst-to-sorted-list-increasing-order):

    # Helper Function:
    def inorder(node: Optional[TreeNode]) -> None:
        if node:
            inorder(node=node.left)
            arr.append(node.val)
            inorder(node=node.right)

    arr = []
    inorder(node=root)

    # Main: For Every Query, BS the Array:

    for query in queries:

        ans = [float('-inf'), float('inf')]  # ans. to this query

        # Search in BST:
        lo, hi = 0, len(arr)-1
        while lo <= hi:
            mid = (lo+hi) // 2
            if (value := arr[mid]) == query:  # => query val itself is present
                ans[:] = [query, query]  # so the ans will be itself only, because if the query is present in the tree,
                # then `largest val <= query` = `smallest val >= query` = query
                break
            if value < query:
                ans[0] = max(ans[0], value)  # `the largest value in the tree that is <= queries[i]`, so update
                lo = mid + 1
            else:  # (value > query)
                ans[1] = min(ans[1], value)  # `the smallest value in the tree that is >= queries[i]`, so update
                hi = mid - 1

        # `If such a value does not exist, add -1 instead.`:
        if ans[0] == float('-inf'):
            ans[0] = -1
        if ans[1] == float('inf'):
            ans[1] = -1

        yield ans
