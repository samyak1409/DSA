"""
https://leetcode.com/problems/cousins-in-binary-tree-ii
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def replace_value_in_tree(root: TreeNode | None) -> TreeNode | None:
    """"""

    # Use DFS two times.
    # For the first time, find the sum of values of all the levels of the binary tree.
    # For the second time, update the value of the node with the sum of the values of the current level - sibling node’s
    # values.

    # 1) Optimal (BFS (aka LOT), One Pass): TC = O(n); SC = O(n)
    # BT BFS (LOT) Template from:
    # https://github.com/samyak1409/DSA/blob/main/Contests/27%29%20Weekly%20Contest%20335/2%29%20Kth%20Largest%20Sum%20in%20a%20Binary%20Tree.py

    queue = {root: root.val}  # k:v :: node:sum(node + it's sibling)
    next_level_sum = root.val  # sum of all the nodes in the next level (level to be traversed next)

    while queue:  # while not traversed all the levels

        nodes = queue.copy()  # or `queue[:]`; `nodes`: nodes on this level
        queue.clear()  # for next level
        level_sum, next_level_sum = next_level_sum, 0

        for node, sibling_sum in nodes.items():

            # "replace the value of each node in the tree with the sum of all its cousins' values":
            node.val = level_sum - sibling_sum

            children = list(filter(None, (node.left, node.right)))

            # Calc sums for next level:
            child_sum = sum(child.val for child in children)
            next_level_sum += child_sum

            # Enqueue nodes:
            # https://docs.python.org/3.11/library/stdtypes.html#dict.update:
            '''
            queue.update({child: child_sum for child in filter(None, (node.left, node.right))})
            '''
            # https://docs.python.org/3.11/library/stdtypes.html#dict.setdefault:~:text=d%20%7C%3D%20other:
            queue |= {child: child_sum for child in children}

    return root
