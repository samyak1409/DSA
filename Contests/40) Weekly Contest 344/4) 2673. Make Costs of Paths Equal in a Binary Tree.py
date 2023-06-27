"""
https://leetcode.com/problems/make-costs-of-paths-equal-in-a-binary-tree
"""


def min_increments(n: int, cost: list[int]) -> int:
    """"""

    # The path from the root to a leaf that has the maximum cost should not be modified.
    # The optimal way is to increase all other paths to make their costs equal to the path with maximum cost.

    # 1) Optimal (No DFS, Iterative): TC = O(n); SC = O(n)
    # {Though SC=O(log(n)) is possible by using a carry_list which contains the carries to be added on above level.}
    # -> It's Easy!!
    # At first, this question may look hard.
    # One thing is easily realized that the highest cost path should remain the same, and other lesser cost paths should
    # come up (increase) to that highest cost path, for getting the optimal ans.
    # Now, it just takes the realization that for any two sibling leaf nodes (left and right), if the path cost is
    # different, then, only one of these two nodes would have to be changed. Changing upper nodes won't change the
    # difference in their cost path as their parents are the same, so both would be changed! That's it!
    # Now, just building this up.

    # [WA]:
    # It'll be a WA if you just consider their difference and do nothing else.
    # Think, that if there are 2 parent nodes (which are siblings), their respective children nodes are normalized.
    # After this, parent nodes are normalized. But wait, do you see that if the cost of the nodes after normalizing too
    # is different for both the parents' children, then the cost path won't be the same, even if the parents are
    # normalized.
    """
    ans = 0
    for i in range(1, n, 2):
        ans += abs(cost[i]-cost[i+1])
    return ans
    """
    # Just a small fix that the normalized cost of the children should be added up in the parent before normalizing the
    # parents, and done!

    ans = 0
    # Traverse the tree from bottom level to top level, right to left (basically reverse level order traversal):
    for i in range(n-1, 1, -2):
        # (stop=1 so that root node is not considered, we only want to consider left & right nodes)
        # Add the diff to the ans:
        ans += abs(cost[i-1]-cost[i])
        # Sum up the normalized cost (max one) to the parent node for future normalization:
        cost[(i//2)-1] += max(cost[i-1], cost[i])  # `(i//2)-1` get the index of parent from the current index
    return ans
