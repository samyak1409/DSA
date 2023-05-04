"""
https://leetcode.com/problems/kth-largest-sum-in-a-binary-tree
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def kth_largest_level_sum(root: TreeNode | None, k: int) -> int:
    """"""

    # Find the sum of values of nodes on each level and return the kth largest one.
    # To find the sum of the values of nodes on each level, you can use a DFS or BFS algorithm to traverse the tree and
    # keep track of the level of each node.

    # 1) Optimal (BFS (Level Order Traversal) + Sorting): TC = O(n*log(n)); SC = O(n)

    sums = []

    # BFS: TC = O(n) {we're traversing all the nodes in the tree}
    # SC = O(n) {queue will be storing ~ n//2 nodes at last level for a perfect binary tree}
    queue = [root]
    while queue:
        sum_ = 0
        nodes = queue.copy()  # or `queue[:]`; `nodes`: nodes on this level
        queue.clear()  # for next level
        for node in nodes:
            sum_ += node.val
            queue.extend(filter(None, (node.left, node.right)))
        sums.append(sum_)

    # Sort the sums: TC = O(n*log(n)); SC = O(n) {for a degenerated binary tree, levels == n}
    return sorted(sums, reverse=True)[k-1] if k <= len(sums) else -1
    # in the contest, got penalty here for not considering else case


# BT BFS (LOT) Templates:
# https://en.wikipedia.org/wiki/Tree_traversal
# https://en.wikipedia.org/wiki/Breadth-first_search

# 1) Using `list` (useful where level distinction is needed):
"""    
queue = [root]
while queue:
    nodes = queue.copy()  # or `queue[:]`; `nodes`: nodes on this level
    queue.clear()  # for next level
    for node in nodes:
        print(node.val)
        '''
        if node_l := node.left:
            queue.append(node_l)
        if node_r := node.right:
            queue.append(node_r)
        '''
        # One liner:
        queue.extend(filter(None, (node.left, node.right)))
"""

# 2) Using `collections.deque` (useful where level distinction is not needed, and we just need to search/traverse the
# tree in level order):
"""
from collections import deque
queue = deque()
queue.append(root)
while queue:
    node = queue.popleft()
    print(node.val)
    '''
    if node_l := node.left:
        queue.append(node_l)
    if node_r := node.right:
        queue.append(node_r)
    '''
    # One liner:
    queue.extend(filter(None, (node.left, node.right)))
"""
