"""
https://leetcode.com/problems/minimum-cost-of-a-path-with-special-roads
"""


def minimum_cost(start: list[int], target: list[int], specialRoads: list[list[int]]) -> int:
    """"""

    # It can be proven that it is optimal to go only to the positions that are either the start or the end of a special
    # road or the target position.
    # Consider all positions given to you as nodes in a graph, and the edges of the graph are the special roads.
    # Now the problem is equivalent to finding the shortest path in a directed graph.

    # 1) Optimal (Dijkstra): TC = O(?); SC = O(?)
    # https://leetcode.com/problems/minimum-cost-of-a-path-with-special-roads/solutions

    pass
