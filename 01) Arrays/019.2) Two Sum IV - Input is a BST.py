"""
https://leetcode.com/problems/two-sum-iv-input-is-a-bst
"""


from typing import Optional, Generator


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_target(root: Optional[TreeNode], k: int) -> bool:
    """"""

    # 0) Brute-force (For each node, search other node in BST): TC = O(n*log(n)); SC = O(log(n))
    # "Method 3." in:
    # https://leetcode.com/problems/two-sum-iv-input-is-a-bst/solutions/106059/java-c-three-simple-methods-choose-one-you-like

    # 0.1) TC = O(n*log(n)); SC = O(n) {by queue}
    """
    # BFS (aka Level Order Traverse) (uses Queue):
    q = [root]
    while q:
        q_copy = q[:]
        q.clear()
        for node1 in q_copy:
            if node1:
                # print(node1.val)  #debugging
                # Now BS the Tree to check if `k-node1.val` exists: O(log(n)) (aka O(h))
                req_val = k - node1.val
                node2 = root  # copy for traverse
                while node2:
                    val = node2.val
                    if node2 != node1 and val == req_val:  # `node2 != node1` handles selecting same node as node1 & 2
                        return True
                    elif val < req_val:
                        node2 = node2.right
                    else:  # (val > req_val)
                        node2 = node2.left
                q.extend([node1.left, node1.right])
    # return False  # optional as bool(None) == False
    """
    # 0.2) TC = O(n*log(n)); SC = O(log(n)) {by stack}
    """
    # Recursive Function: DFS (uses Stack):
    def dfs(node1: Optional[TreeNode]) -> bool:
        if node1:
            # print(node1.val)  #debugging
            # Now BS the Tree to check if `k-node1.val` exists: O(log(n)) (aka O(h))
            req_val = k - node1.val
            node2 = root  # copy for traverse
            while node2:
                val = node2.val
                if node2 != node1 and val == req_val:  # `node2 != node1` handles selecting same node as node1 & 2
                    return True
                elif val < req_val:
                    node2 = node2.right
                else:  # (val > req_val)
                    node2 = node2.left
            return dfs(node1.left) or dfs(node1.right)
    return dfs(root)
    """
    # => DFS IS BETTER THAN BFS: Less LOC and Uses Less Memory!

    # We can clearly see the main issue here is we're again and again searching for the vals in the BST.
    # Can we save the data in a format which will allow faster lookup? Yes! O(1) using HashSet

    # 1.1) Better (Save vals to HashSet): TC = O(n); SC = O(n)
    # "Method 1." in:
    # https://leetcode.com/problems/two-sum-iv-input-is-a-bst/solutions/106059/java-c-three-simple-methods-choose-one-you-like

    """
    # Recursive Function: DFS: O(n)
    def dfs(node: Optional[TreeNode]) -> bool:
        if node:
            val = node.val
            # print(val)  #debugging
            if k-val in hs:  # lookup: O(1)
                return True
            hs.add(val)  # save
            return dfs(node.left) or dfs(node.right)
    hs = set()
    return dfs(root)
    """

    # But we didn't benefit from the fact that it's BST and not just BT.

    # 1.2) Better (BST to Sorted Array using In-order; then Two Pointers): TC = O(n); SC = O(n)
    # "Method 2." in:
    # https://leetcode.com/problems/two-sum-iv-input-is-a-bst/solutions/106059/java-c-three-simple-methods-choose-one-you-like

    """
    # Step 1) BST to Sorted Array using In-order:
    # Helper Function:
    def inorder(node: Optional[TreeNode]) -> None:
        if node:
            inorder(node.left)
            # print(node.val)  #debugging
            arr.append(node.val)
            inorder(node.right)
    arr = []
    inorder(root)
    # Step 2) Finding the 2 nums using Two-Pointers:
    # "2) Optimal (Two-Pointers)" in:
    # https://github.com/samyak1409/DSA/blob/main/01%29%20Arrays/019.1%29%20Two%20Sum%20II%20-%20Input%20Array%20Is%20Sorted.py
    lt, rt = 0, len(arr)-1  # init
    while lt < rt:
        if (two_sum := arr[lt]+arr[rt]) == k:
            return True
        elif two_sum < k:
            lt += 1
        else:  # (if two_sum > k)
            rt -= 1
    # return False  # optional as bool(None) == False
    """

    # But, we applied the algo on Array, but the interviewer asked this question expecting algo on the BST only!
    # Is there a way we can traverse the BST like we traverse the sorted array from the two ends using Two Pointers?

    # 2) Optimal (Two Pointers on BST): TC = O(n); SC = O(log(n))
    # Came up with this myself! Very similar to the correct & expected solution: "Solution 2" in:
    # https://leetcode.com/problems/two-sum-iv-input-is-a-bst/solutions/1420711/c-java-python-3-solutions-hashset-stack-python-yield-solutions-o-h-space

    """
    # Helper Functions:

    def traverse_lt(node: Optional[TreeNode]) -> None:
        if node:
            stack_lt.append(node)
            traverse_lt(node.left)

    def traverse_rt(node: Optional[TreeNode]) -> None:
        if node:
            stack_rt.append(node)
            traverse_rt(node.right)

    # Main: Same paradigm as "2) Optimal (Two-Pointers)" of:
    # https://github.com/samyak1409/DSA/blob/main/01%29%20Arrays/019.1%29%20Two%20Sum%20II%20-%20Input%20Array%20Is%20Sorted.py
    stack_lt, stack_rt = [], []  # to track parent nodes
    traverse_lt(root), traverse_rt(root)  # start
    lt, rt = stack_lt.pop(), stack_rt.pop()  # init with min and max val
    while lt.val < rt.val:
        if (two_sum := lt.val+rt.val) == k:
            return True
        elif two_sum < k:
            traverse_lt(lt.right)  # traverse right child of current node
            lt = stack_lt.pop()  # get next node
            traverse_lt(lt.right)  # traverse right child of current node
        else:  # (if two_sum > k)
            traverse_rt(rt.left)  # traverse left child of current node
            rt = stack_rt.pop()  # get next node
            traverse_rt(rt.left)  # traverse left child of current node
    # return False  # optional as bool(None) == False
    """

    # Optimized:

    """
    # Helper Functions:

    def traverse_lt(node: Optional[TreeNode]) -> None:
        if node:
            stack_lt.append(node)
            traverse_lt(node.left)

    def traverse_rt(node: Optional[TreeNode]) -> None:
        if node:
            stack_rt.append(node)
            traverse_rt(node.right)

    # Main: Same paradigm as "2) Optimal (Two-Pointers)" of:
    # https://github.com/samyak1409/DSA/blob/main/01%29%20Arrays/019.1%29%20Two%20Sum%20II%20-%20Input%20Array%20Is%20Sorted.py
    stack_lt, stack_rt = [], []  # to track parent nodes
    traverse_lt(root), traverse_rt(root)  # start
    lt, rt = stack_lt.pop(), stack_rt.pop()  # init with min and max val
    traverse_lt(lt.right), traverse_rt(rt.left)  # check for children on opposite side of both deepest leaves
    while lt.val < rt.val:
        if (two_sum := lt.val+rt.val) == k:
            return True
        elif two_sum < k:
            lt = stack_lt.pop()  # get next node
            traverse_lt(lt.right)  # traverse right child of current node
        else:  # (if two_sum > k)
            rt = stack_rt.pop()  # get next node
            traverse_rt(rt.left)  # traverse left child of current node
    # return False  # optional as bool(None) == False
    """

    # 2.1) Using `yield` which produces this behavior by default!:
    # "Solution 3" in:
    # https://leetcode.com/problems/two-sum-iv-input-is-a-bst/solutions/1420711/c-java-python-3-solutions-hashset-stack-python-yield-solutions-o-h-space

    # Helper Functions:

    def inorder(node: Optional[TreeNode]) -> Generator:
        if node:
            yield from inorder(node.left)
            yield node.val
            yield from inorder(node.right)

    # https://en.wikipedia.org/wiki/Tree_traversal#Reverse_in-order,_RNL
    def reverse_inorder(node: Optional[TreeNode]) -> Generator:
        # For BST, this will yield the values in descending order, like the `inorder` yields the values in ascending
        # order.
        if node:
            yield from reverse_inorder(node.right)
            yield node.val
            yield from reverse_inorder(node.left)

    # Main: Same paradigm as "2) Optimal (Two-Pointers)" of:
    # https://github.com/samyak1409/DSA/blob/main/01%29%20Arrays/019.1%29%20Two%20Sum%20II%20-%20Input%20Array%20Is%20Sorted.py
    generator_lt, generator_rt = inorder(root),  reverse_inorder(root)
    lt, rt = next(generator_lt), next(generator_rt)
    while lt < rt:
        if (two_sum := lt+rt) == k:
            return True
        if two_sum < k:
            lt = next(generator_lt)
        else:  # (if two_sum > k)
            rt = next(generator_rt)
    # return False  # optional as bool(None) == False
