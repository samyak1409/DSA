"""
https://leetcode.com/problems/minimum-operations-to-make-columns-strictly-increasing
"""


def minimum_operations(grid: list[list[int]]) -> int:
    """"""

    # 1) Optimal (Greedy: Iterate, Prev+1): TC = O(n*m); SC = O(1)

    ops = 0
    for j in range(len(grid[0])):
        for i in range(1, len(grid)):
            # If curr <= prev:
            if grid[i][j] <= grid[i-1][j]:
                # Ops += num required to make curr = prev + 1:
                ops += grid[i-1][j] - grid[i][j] + 1
                # Make curr = prev + 1:
                grid[i][j] = grid[i-1][j] + 1
    return ops
