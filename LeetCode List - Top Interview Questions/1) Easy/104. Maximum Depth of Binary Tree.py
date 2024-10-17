"""
https://leetcode.com/problems/maximum-depth-of-binary-tree
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root: TreeNode | None) -> int:
    """"""

    # 1) Optimal (Iterative: Level order traversal, +1 count on each level):
    # TC = O(n) (going through every node)
    # SC = O(n) (last level of binary tree have (n//2 + 1) nodes at most)

    """
    level = [root]
    depth = -1

    while level:  # will loop h times, h: height of binary tree

        depth += 1

        level_copy = level.copy()
        level.clear()
        for node in level_copy:  # will loop 1, 2, 4, 8, ... (n//2 + 1) times
            if node:
                level.extend([node.left, node.right])

    return depth
    """

    # 2) Optimal (Recursive): TC = O(n); SC = O(h) {avg. case: O(log(n)); worst case: O(n)}
    # Recurse on each node left and right, and +1 each time.

    # 2.1) Intuitive:
    """
    # Recursive Function:
    def recurse(node: TreeNode | None , curr_depth: int) -> None:
        if node is None:  # base case of recursion: if node is None, return
            return
        # Else, update the ans:
        ans[0] = max(ans[0], curr_depth)
        # And then recurse further in:
        recurse(node.left, curr_depth+1), recurse(node.right, curr_depth+1)

    ans = [0]  # list for mutability
    recurse(root, 1)
    return ans[0]
    """

    # 2.2) "Pro recursion" / "Power of recursion":
    # https://leetcode.com/problems/maximum-depth-of-binary-tree/solutions

    if not root:  # base case
        return 0
    # Just return the max of max_depths of left and right subtree, and recursion will solve the sub-subtrees:
    return max(max_depth(root.left), max_depth(root.right)) + 1

    # (While submitting on LC: `max_depth` -> `self.maxDepth`)
