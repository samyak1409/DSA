"""
https://leetcode.com/problems/minimum-path-sum
"""


def min_path_sum(grid: list[list[int]]) -> int:
    """"""

    # All the solutions are (modifications of the solutions) from
    # https://github.com/samyak1409/DSA/blob/main/01%29%20Arrays/017%29%20Unique%20Paths.py.

    # 1) Time-Optimal (Recursion + Memoization): TC = O(m*n); SC = O(m*n)

    from functools import cache

    # Recursive Function:
    @cache
    def get_min_sum(i: int = 0, j: int = 0) -> (int, float):  # default cell (0, 0) -> start point
        # Base Case 1 (IndexOutOfBound (Jumped of the Matrix)):
        if i == m or j == n:
            return float('inf')  # so that this path will never be chosen in min() function
        # Base Case 2 (Reached Finish Point):
        if i == m-1 and j == n-1:
            return grid[i][j]  # because we're returning from here only
        # Recurse In (Move Down | Move Right):
        return grid[i][j] + min(get_min_sum(i+1, j), get_min_sum(i, j+1))

    m, n = len(grid), len(grid[0])  # rows, cols
    return get_min_sum()

    # 2) Optimal (DP): TC = O(m*n); SC = O(1)
    # Easy:
    # https://leetcode.com/problems/minimum-path-sum/discuss/584967/Python-Grid-reduction-(Sounds-fancy-but-a-simple-method)-no-additional-space
