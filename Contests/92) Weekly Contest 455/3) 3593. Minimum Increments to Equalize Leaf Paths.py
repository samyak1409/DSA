"""
https://leetcode.com/problems/minimum-increments-to-equalize-leaf-paths
"""


def min_increase(n: int, edges: list[list[int]], cost: list[int]) -> int:
    """"""

    # 1) Suboptimal (Sort, HashMap: Equalize sibling costs bottom-up): TC = O(n*log2(n)); SC = O(n)
    # [Not hard at all.]
    # Intuition:
    # To make all root-to-leaf path scores equal, the only valid operation is to increase node costs.
    # So, the idea is to equalize the total cost of each root-to-leaf path by:
    # 1. Looking at sibling nodes (i.e., nodes sharing the same parent),
    # 2. Ensuring all siblings contribute equally to their parent’s path score,
    # 3. And propagating this equalized cost upward, from leaf to root.
    # We only count how many nodes required any increase, which gives us the final answer.
    # Approach:
    # 1. Build a level-wise parent-child mapping using `level_wise_nodes`, so we can process the tree from bottom to
    #    top.
    # 2. Start from the deepest level and move upward (bottom-up), processing each group of siblings:
    # - For each parent, find the maximum cost among its children.
    # - Any child with a lower cost must be increased to match this maximum.
    # - These increases are counted in the `increments` dictionary.
    # - The parent’s cost is updated by adding this maximum child cost, representing the equalized contribution from its
    #   children.
    # 3. Finally, return the number of nodes whose cost was increased.
    # Why Bottom-Up?
    # Because only leaf costs are final. Their equalized values affect their parents, and so on. We can’t decide a
    # parent’s required cost until its children are equalized.
    # Hence, by propagating equalized costs up the tree, we ensure all paths from root to any leaf sum to the same
    # total, with the minimum number of node cost increases.

    from collections import defaultdict

    depth = {0: 0}  # k: v = node: level
    # Level-wise parent-child mapping:
    level_wise_nodes = defaultdict(lambda: defaultdict(list))  # k: v = child_level: {parent: children_list}
    # `level_wise_nodes[level][parent]` = list of children at this level, grouped by parent

    # Build level-wise parent-child mapping:
    for parent, child in sorted((min(u, v), max(u, v)) for u, v in edges):
        depth[child] = depth[parent] + 1
        level_wise_nodes[depth[child]][parent].append(child)

    # print(depth); print({k: dict(v) for k, v in level_wise_nodes.items()})  # debug

    increments = {}  # k: v = node: increments

    # Traverse levels from bottom to top:
    for level in range(len(level_wise_nodes), 0, -1):
        for parent, children in level_wise_nodes[level].items():
            # Max cost among sibling nodes (nodes with same parent):
            max_cost = max(cost[child] for child in children)
            # print(max_cost)  # debug
            # All the children that have lesser cost than `max_cost`, needs to be increased individually:
            for child in children:
                if increment := max_cost-cost[child]:
                    increments[child] = increment
            # And then we need to add the equalized cost to the parent for further equalizations:
            cost[parent] += max_cost

    # print(increments)  # debug

    # Every individual increment:
    return len(increments)

    # 2) Optimal (DFS): TC = O(n); SC = O(n)
    # https://leetcode.com/problems/minimum-increments-to-equalize-leaf-paths/solutions
