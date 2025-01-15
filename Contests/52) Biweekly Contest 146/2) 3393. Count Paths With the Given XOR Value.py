"""
https://leetcode.com/problems/count-paths-with-the-given-xor-value
"""


def count_paths_with_xor_value(grid: list[list[int]], k: int) -> int:
    """"""

    # Modified problem of:
    # https://github.com/samyak1409/DSA/blob/main/SDE%20Sheet/01%29%20Arrays/017%29%20Unique%20Paths.py

    # 0) [TLE] Brute-force (Recursion): TC = O(2^(m+n)); SC = O(m+n)) {recursion stack}
    # TC:
    # In the worst case, the recursion tree will have a depth of m + n - 2.
    # At each level, the number of nodes doubles.
    # This leads to an exponential growth in the number of function calls.
    # SC:
    # The maximum depth of the recursion stack can be m + n - 2.

    """
    # Recursive Func:
    def r(i: int, j: int, x: int) -> int:
        # x: xor till here
        if i >= m or j >= n:  # -ve base case: went out of grid
            return 0
        if i == m-1 and j == n-1:  # +ve base case: reached at bottom left cell
            return int(x^grid[i][j] == k)  # 0 or 1
        # Recurse in:
        return (r(i, j+1, x^grid[i][j]) + r(i+1, j, x^grid[i][j])) % (10**9 + 7)

    m, n = len(grid), len(grid[0])
    return r(i=0, j=0, x=0)
    """

    # 1) Optimal (Recursion + Memoization): TC = O(m*n); SC = O(m*n) {memo}
    # Add memoization to `0)`.
    # TC: Each unique pair of (m, n) is calculated only once and stored in the memoization dictionary.
    # SC: The memoization dictionary can store up to m * n key-value pairs.

    from functools import cache

    # Recursive Func:
    @cache
    def r(i: int, j: int, x: int) -> int:
        # x: xor till here
        if i >= m or j >= n:  # -ve base case: went out of grid
            return 0
        if i == m-1 and j == n-1:  # +ve base case: reached at bottom left cell
            return int(x^grid[i][j] == k)  # 0 or 1
        # Recurse in:
        return (r(i, j+1, x^grid[i][j]) + r(i+1, j, x^grid[i][j])) % (10**9 + 7)

    m, n = len(grid), len(grid[0])
    return r(i=0, j=0, x=0)
