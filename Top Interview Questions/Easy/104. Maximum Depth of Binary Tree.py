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

    # Iterative:
    # TC = O(n) (we are just going through each and every node in the tree one time)
    # SC = O(n) (last level of the binary tree have (n+1)/2 nodes at most)

    """
    queue = [root]
    height = -1

    while queue:  # will loop h times, h: height of binary tree

        height += 1

        queue_copy = queue.copy()  # "queue.copy()" / "queue[:]" -> new copy ✔

        queue.clear()

        for node in queue_copy:  # will loop 1, 2, 4, 8, ... (n+1)/2 times
            if node:
                queue.extend([node.left, node.right])

    return height
    """

    # Recursive: TC = O(n); SC = O(h) (height of the binary tree) = O(n) in worst case and O(log n) in best case

    if not root:  # base condition
        return 0

    return max(maxDepth(root.left), maxDepth(root.right)) + 1
