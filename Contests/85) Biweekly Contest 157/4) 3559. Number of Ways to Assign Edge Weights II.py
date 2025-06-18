"""
https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-ii
"""


def assign_edge_weights(edges: list[list[int]], queries: list[list[int]]) -> list[int]:
    """"""

    # Follow-up version of `3558. Number of Ways to Assign Edge Weights I`. Solution also based on that.

    # 1) [TLE] Suboptimal (Sort, HashMap, Lowest Common Ancestor, Combinatorics):
    # TC = O(n*log2(n) + q*n) {worst case: degenerate tree} O(n*log2(n) + q*log2(n)) {avg. case}; SC = O(n)
    # [Came up with myself.]
    # The only problematic case with this approach is degenerate tree, which leads to LCA (Lowest Common Ancestor) being
    # costed O(n) instead of O(log2(n)).
    # Also, test case for this was not added at the time of the contest!!
    # See comment: https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-ii/description/comments/3005327
    # AC: https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-ii/submissions/1643252874
    # So, I could've got rank ~1k, and AIR ~100, second time in a month! (Weekly Contest 449)

    depth = {1: 1}  # k: v = node: depth
    # For calculating Lowest Common Ancestor:
    parent = {}  # k: v = node: parent node

    # Sort:
    # `(min(u, v), max(u, v))`: so that `u` is always smaller and `v` is always larger
    # Test case: [[2, 1], [3, 2]]
    # `sorted`: so that we process in the correct order
    # Test case: [[2, 3], [1, 2]]
    for u, v in sorted((min(u, v), max(u, v)) for u, v in edges):  # TC = O(n*log2(n))
        depth[v] = depth[u] + 1
        parent[v] = u
    # print(depth); print(parent)  # debug

    ans = []
    for u, v in queries:  # TC = O(q*n) {worst} O(q*log2(n)) {avg.}
        # Calculating the distance b/w the two nodes using LCA:
        path_len = 0  # or `edge_cnt`
        # While u != v != LCA:
        while u != v:  # TC = O(n) {worst} O(log2(n)) {avg.}
            # Whichever node's depth is more, move it up to its parent:
            if depth[u] < depth[v]:
                v = parent[v]
                path_len += 1
            elif depth[u] > depth[v]:
                u = parent[u]
                path_len += 1
            # And when the depth becomes equal, then move them simultaneously until not reached at the same node, i.e.,
            # LCA node:
            else:  # if depth[u] == depth[v]:
                u, v = parent[u], parent[v]
                path_len += 2
        # Calc the ways using combinatorics just like in `#3558`
        if path_len:
            ans.append(pow(2, path_len-1, 10**9+7))  # (using `pow` & its `mod` param for speed)
        else:
            ans.append(0)

    return ans

    # 2) Optimal (Sort, HashMap, Binary Lifting for faster LCA, Combinatorics): TC = O(); SC = O()
