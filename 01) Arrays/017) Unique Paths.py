"""
https://leetcode.com/problems/unique-paths
"""


def uniquePaths(m: int, n: int) -> int:
    """"""

    # 0) (TLE) Brute-force (Recursion): TC = O(2^(m+n)); SC = O(m+n)
    # The formula to determine the time complexity for recursion = branches ^ depth = the number of nodes in the recursion tree
    # In our case, we have 2 possible branches (going down or going right), while for the depth, is the maximum possible distance taken to get (m, n) which is m + n.
    # Given this, we can also mention the space complexity taken on the stack: O(m+n)

    def get_unique_paths(i: int = 0, j: int = 0) -> int:  # default cell (0, 0) -> start point
        # Base Case 1 (Reached Finish Point):
        if i == m-1 and j == n-1:
            return 1
        # Base Case 2 (IndexOutOfBound (Jumped of the Matrix)):
        if i == m or j == n:
            return 0
        # Recursion (Move Bottom | Move Right):
        return get_unique_paths(i+1, j) + get_unique_paths(i, j+1)

    return get_unique_paths()
