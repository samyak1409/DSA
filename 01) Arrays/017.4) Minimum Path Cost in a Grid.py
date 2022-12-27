"""
https://leetcode.com/problems/minimum-path-cost-in-a-grid
"""


def min_path_cost(grid: list[list[int]], move_cost: list[list[int]]) -> int:
    """"""

    # One thing is clear, that greedy approach won't work here, i.e. choosing the minimum (cost cell + path) because
    # it may be possible that after choosing a minimum cell on current row, we left out on a more optimal overall path
    # which could be starting from the other cell of the current row.
    # Hence, this must be solved by DP.

    # 1) Sub-Optimal (Recursion + Memoization): TC = O(?); SC = O(?)
    # https://leetcode.com/problems/minimum-path-cost-in-a-grid/solutions

    # 2) Optimal (DP): TC = O(?); SC = O(?)
    # What is the optimal cost to get to each of the cells in the second row? What about the third row?
    # Use dynamic programming to compute the optimal cost to get to each cell.
    # https://leetcode.com/problems/minimum-path-cost-in-a-grid/solutions
