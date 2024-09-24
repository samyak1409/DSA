"""
https://leetcode.com/problems/binary-tree-inorder-traversal
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder_traversal(root: TreeNode | None) -> list[int]:
    """"""

    # 1) Optimal: TC = O(n); SC = O(h) {height of the tree = O(n) in worst case due to degenerate tree}
    # Types of binary trees with colourful illustrations: https://images.app.goo.gl/4pZvqA9xWmkdvo3dA
    # https://en.wikipedia.org/wiki/Binary_tree#Types_of_binary_trees

    # 1.1) Recursive:

    """
    # Recursive Function:
    def inorder(node: TreeNode | None) -> None:
        if node:  # only if current node is not None
            inorder(node.left)  # first go all the left
            vals.append(node.val)  # then append val of the most left node (which is in the top of the stack currently)
            inorder(node.right)  # then check for it's right child nodes
        # And recursion does the remaining job.

    vals = []
    inorder(root)
    return vals
    """

    # [Just for fun] This can also be done in just one line:
    # https://leetcode.com/problems/binary-tree-inorder-traversal/solutions/283746/all-dfs-traversals-preorder-inorder-postorder-in-python-in-1-line

    # 1.2) Iterative (Stack):
    # How to approach this? Just try to build the exact same program flow (like recursion algo) using iteration! (not
    # hard)

    # First try:
    """
    # Handle edge case:
    if not root:
        return []

    st = [root]
    vals = []

    # First go all the way left and push to stack:
    while lt := st[-1].left:
        st.append(lt)

    # Then repeat following while stack is not empty:
    # Pop the top and append it's val to the ans., then check if this node has a right child, if it has, first push
    # itself to the stack, and then all the left child nodes of it as well.
    while st:
        curr = st.pop()
        vals.append(curr.val)
        if rt := curr.right:
            st.append(rt)
            while lt := st[-1].left:
                st.append(lt)

    return vals
    """

    # https://leetcode.com/problems/binary-tree-inorder-traversal/solutions/31381/python-recursive-and-iterative-solutions
    # https://leetcode.com/problems/binary-tree-inorder-traversal/editorial/#approach-2-iterating-method-using-stack
    st, vals = [], []
    while True:
        while root:  # traverse till the most left node
            st.append(root)
            root = root.left
        if st:  # if any left nodes are there
            root = st.pop()  # take last left node
            vals.append(root.val)  # add its value to ans.
            root = root.right  # check for its right node now
        else:  # no nodes left to traverse
            return vals
