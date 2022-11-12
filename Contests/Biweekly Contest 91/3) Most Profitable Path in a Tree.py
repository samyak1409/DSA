"""
https://leetcode.com/problems/most-profitable-path-in-a-tree
"""


def most_profitable_path(edges: list[list[int]], bob: int, amount: list[int]) -> int:
    """"""

    # 1) Optimal (DFS): TC = O(?); SC = O(?)
    # Bob travels along a fixed path (from node “bob” to node 0).
    # Calculate Alice’s distance to each node via DFS.
    # We can calculate Alice’s score along a path ending at some node easily using Hints 1 and 2.
    # https://leetcode.com/problems/most-profitable-path-in-a-tree/discuss
