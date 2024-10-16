"""
https://leetcode.com/problems/symmetric-tree
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_symmetric(root: TreeNode | None) -> bool:
    """"""

    # Follow up: Could you solve it both recursively and iteratively?

    # 1) Time-Optimal (Iterative: Level Order Traversal and Palindrome):
    # TC = O(n) {where n is the total number of nodes in the tree};
    # SC = O(n) {because the no. of nodes in the last level = O(n//2 + 1)}

    """
    level = [root.left, root.right]

    # Loop levels one by one:
    while True:

        # print([node.val if node else None for node in level])  # debug

        # Check if current level is a palindrome:
        # `node.val if node else None`: check val if node is not None, else compare "no node" only.
        if [node.val if node else None for node in level] != [node.val if node else None for node in level[::-1]]:
            # Stop if not, meaning tree not symmetric:
            return False

        # Add the next level to the list:
        level_copy = level[:]
        level.clear()
        for node in level_copy:
            if node:
                level.extend([node.left, node.right])

        # If no nodes are there in next level:
        if not level:
            # Tree is symmetric:
            return True
    """

    # 2) Optimal (Recursive): TC = O(n); SC = O(log(n)) {not O(n) (skewed tree), think why}

    # Recursive Function:
    def are_symmetric(l_node: TreeNode | None, r_node: TreeNode | None) -> bool:

        if not (l_node or r_node):  # base case: parent is a leaf node
            return True  # recurse out

        # If both nodes are there, and have equal vals:
        if l_node and r_node and l_node.val == r_node.val:
            # Recurse with the next two sub-tress, and return the `and` operation of both:
            return are_symmetric(l_node.left, r_node.right) and are_symmetric(l_node.right, r_node.left)  # recurse in

        # If not returned above, means either there is only one node, or the two nodes have diff vals:
        # Tree not symmetric in either case:
        return False  # recurse out

    return are_symmetric(root.left, root.right)
