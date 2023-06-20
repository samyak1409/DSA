"""
https://leetcode.com/problems/unique-paths-ii
"""


def unique_paths_with_obstacles(obstacle_grid: list[list[int]]) -> int:
    """"""

    # All the solutions are (modifications of the solutions) from
    # https://github.com/samyak1409/DSA/blob/main/SDE%20Sheet/01%29%20Arrays/017%29%20Unique%20Paths.py.

    # 2.1) [WA] Optimal (Maths: PnC): TC = O(m*n); SC = O(1)
    # Because the matrix can have ANY NO. OF OBSTACLES, misunderstood the question that only 1 obstacle will be there.
    # If the matrix had only 1 obstacle and that too given explicitly, this approach would have solved the question in
    # O(min(m+n)), which would have been a big jump in performance when compared to the previous approach, exactly like
    # https://leetcode.com/problems/unique-paths. Stupidly, this approach is O(m*n) because of finding obstacle in
    # the Matrix and not because of the actual solution!

    """
    from math import comb

    m, n = len(obstacle_grid)-1, len(obstacle_grid[0])-1  # row last index, col last index

    # Finding obstacles in the grid:
    for i in range(m+1):  # O(m*n)
        for j in range(n+1):
            if obstacle_grid[i][j]:  # i, j -> obstacle indices
                return comb(m+n, min(m, n)) - (comb(i+j, min(i, j)) * comb(m+n-i-j, min(m-i, n-j)))  # O(min(m, n))
                # total unique paths (without obstacle) - paths with obstacle
                # You ask how's this working? Check this: https://youtu.be/m7chPc7zIF4?t=246
    """

    # 1) Time-Optimal (Recursion + Memoization): TC = O(m*n); SC = O(m*n)

    from functools import cache

    # Recursive Function:
    @cache
    def get_unique_paths2(i: int = 0, j: int = 0) -> int:  # default cell (0, 0) -> start point
        # Base Case 1 (IndexOutOfBound (Jumped of the Matrix) OR Obstacle Found):
        if i == m or j == n or obstacle_grid[i][j]:
            return 0
        # Base Case 2 (Reached Finish Point):
        if i == m-1 and j == n-1:
            return 1
        # Recurse In (Move Down | Move Right):
        return get_unique_paths2(i+1, j) + get_unique_paths2(i, j+1)

    m, n = len(obstacle_grid), len(obstacle_grid[0])  # rows, cols
    return get_unique_paths2()

    # 2.2) Optimal (DP): TC = O(m*n); SC = O(1)
    # Use dynamic programming since, from each cell, you can move to the right or down.
    # Assume dp[i][j] is the number of unique paths to reach (i, j).
    # dp[i][j] = dp[i][j -1] + dp[i - 1][j].
    # Be careful when you encounter an obstacle. set its value in dp to 0.
    # https://leetcode.com/problems/unique-paths-ii/solution
