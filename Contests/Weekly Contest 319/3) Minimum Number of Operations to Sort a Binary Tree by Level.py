"""
https://leetcode.com/problems/minimum-number-of-operations-to-sort-a-binary-tree-by-level
"""


from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def minimum_operations(root: Optional[TreeNode]) -> int:
    """"""

    # 1) Optimal (Level Order Traversal + Min Swaps to Sort an Array): TC = O(log(n) * (k + k*log(k))); SC = O(k)
    #                                                                  where k = log(2^n, base=n)
    # We can group the values level by level and solve each group independently.
    # Do BFS to group the value level by level.
    # Find the minimum number of swaps to sort the array of each level.
    # While iterating over the array, check the current element, and if not in the correct index, replace that element
    # with the index of the element which should have come.

    # Helper Function:
    def get_min_swaps(arr: list[int], n: int) -> int:
        """
        Minimum Swaps to Sort an Array (Greedy) (TC = O(n*log(n)); SC = O(n))
        While iterating over the array, check the current element, and if not in the correct place, swap it with the
        correct element which should be at this place (greedily) which will give the optimal answer.
        See https://www.geeksforgeeks.org/minimum-number-swaps-required-sort-array for complete explanation.
        NOTE: It's easy, just dry run it with arr = [7, 6, 8, 5] & arr = [7, 6, 5, 4].
        """
        sorted_arr = sorted(arr)
        ans = 0
        original_index = {val: i for i, val in enumerate(arr)}  # `val: index` mapping of input array
        for i in range(n):
            # Checking whether the current num is at the right place or not:
            if (num_at_i := arr[i]) != (req_num_at_i := sorted_arr[i]):
                # If not, bring the correct num here, and move the current num at the index where the correct num was
                # (i.e. swap):
                arr[i], arr[original_index[req_num_at_i]] = req_num_at_i, num_at_i
                # `num_at_i` is moved to some higher index, and we will eventually come to it again, so we need its
                # index to be updated in our hashmap:
                original_index[num_at_i] = original_index[req_num_at_i]
                ans += 1  # update ans
        return ans

    # Level Order Traversal (BFS) (TC = O(n) {= O(log(n, base=2) * log(2^n, base=n))}; SC = O(log(2^n, base=n))):
    # Derivation of TC and SC:
    # Total nodes in the Tree = n => TC = n
    # `while` loop will run levels time, and no. of levels in a binary tree = log(n, base=2)
    # => TC of `for` loop will be = n / log(n, base=2)
    # n can be written as log(2^n, base=2)
    # => TC(`for` loop) = log(2^n, base=2) / log(n, base=2)
    #                   = log(2^n, base=n) {using https://en.wikipedia.org/wiki/Logarithm#Change_of_base}
    # And that's also the SC of our algo.
    # (Because that only is the max space that will be taken by `queue` & so `vals`.)
    queue = [root]  # init
    min_ops = 0
    while queue:
        queue_copy = queue[:]  # for traversing current level
        queue = []  # will contain nodes from next level
        for node in queue_copy:
            '''
            if node_ := node.left:
                queue.append(node_)
            if node_ := node.right:
                queue.append(node_)
            '''
            queue.extend(filter(None, (node.left, node.right)))  # one liner

        vals = [node.val for node in queue]
        # print(vals)  #debugging
        min_ops += get_min_swaps(arr=vals, n=len(vals))

    return min_ops
