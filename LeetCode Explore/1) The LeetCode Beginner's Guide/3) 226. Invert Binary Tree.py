"""
https://leetcode.com/problems/invert-binary-tree
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert_tree(root: TreeNode | None) -> TreeNode | None:
    """"""

    # https://leetcode.com/problems/invert-binary-tree/solutions/127840/invert-binary-tree

    # 1) Optimal (Recursive (DFS)): TC = O(n); SC = O(h) {height of the tree}
    #                                             = O(log2(n)) in best case: full binary tree
    #                                             = O(n) in worst case: skewed (degenerated) tree

    # 1.1) Using Recursion:

    """
    if not root:
        return  # recurse out

    root.left, root.right = root.right, root.left  # swap

    invert_tree(root.left), invert_tree(root.right)  # recurse in

    return root
    """
    # We can just:
    """
    if not root:
        return  # recurse out

    # Since `invert_tree` returns the `root` anyway:
    root.left, root.right = invert_tree(root.right), invert_tree(root.left)  # recurse in; swap

    return root
    """
    # Or:
    # https://leetcode.com/problems/invert-binary-tree/solutions/62714/3-4-lines-python
    """
    if root:
        root.left, root.right = invert_tree(root.right), invert_tree(root.left)  # recurse in; swap
        return root
    """

    # 1.2) Using Stack Explicitly:
    # "The above solution is correct, but it is also bound to the application stack, which means that it's no so much
    # scalable - (you can find the problem size that will overflow the stack and crash your application), so more robust
    # solution would be to use stack data structure."
    # -https://leetcode.com/problems/invert-binary-tree/solutions/62707/straightforward-dfs-recursive-iterative-bfs-solutions

    """
    pass
    """

    # 2) Optimal (Iterative (BFS aka Level Order Traversal)):
    # TC = O(n); SC = O(n) {max nodes on a level}
    #               = O(1) in best case: skewed (degenerated) tree
    #               = O(n/2) = O(n) in worst case: full binary tree

    # 2.1) Using Array:
    """
    queue = [root]  # init

    while queue:

        queue_ = queue[:]  # copy
        queue.clear()

        for node in queue_:
            if node:
                node.left, node.right = node.right, node.left  # swap
                queue.extend((node.left, node.right))  # enqueue

    return root
    """

    # 2.2) Using Queue:

    from collections import deque
    queue = deque((root, ))

    while queue:

        if node := queue.popleft():  # deque
            node.left, node.right = node.right, node.left  # swap
            queue.extend((node.left, node.right))  # enqueue

    return root
