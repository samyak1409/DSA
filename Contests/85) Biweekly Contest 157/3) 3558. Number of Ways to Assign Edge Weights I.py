"""
https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-i
"""


def assign_edge_weights(edges: list[list[int]]) -> int:
    """"""

    # 1) Suboptimal (Sort, HashMap, Combinatorics): TC = O(n*log2(n)); SC = O(n)
    # [Came up with myself.]
    # This Q. has 2 parts:
    # 1. Find the max depth of the tree using sorting and simple hashmap:
    # `depth[v] = depth[u]+1`; `max_depth = max(max_depth, depth[v])`
    # 2. Calc. the ans using combinatorics:
    # All combinations = `2 ^ max_edges`
    # With odd sum = `(2^max_edges) / 2`

    depth = {1: 1}  # k: v = node: depth
    max_depth = 0

    # Sort:
    # `(min(u, v), max(u, v))`: so that `u` is always smaller and `v` is always larger
    # Test case: [[2, 1], [3, 2]]
    # `sorted`: so that we process in the correct order
    # Test case: [[2, 3], [1, 2]]
    for u, v in sorted((min(u, v), max(u, v)) for u, v in edges):

        depth[v] = depth[u] + 1
        max_depth = max(max_depth, depth[v])

    # print(depth, max_depth)  # debug

    max_edges = max_depth - 1
    # `2` since we've two choices of edge weights (either 1 or 2):
    total_ways = 2 ** max_edges
    # Half of the ways would give even sum and half odd, so:
    ways_with_odd_sum = total_ways // 2

    return ways_with_odd_sum % (10**9 + 7)

    # 2) Optimal (DFS, Combinatorics): TC = O(n); SC = O(n)
    # https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-i/solutions
