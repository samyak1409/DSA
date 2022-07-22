"""
https://leetcode.com/problems/unique-paths
"""


def uniquePaths(m: int, n: int) -> int:
    """"""

    # 0) (TLE) Brute-force (Recursion): TC = O(2^(m+n)); SC = O(m+n)
    # The formula to determine the time complexity for recursion = branches ^ depth = the number of nodes in the recursion tree
    # In our case, we have 2 possible branches (going down or going right), while for the depth, is the maximum possible distance taken to get (m, n) which is m + n.
    # Given this, we can also mention the space complexity taken on the stack: O(m+n)

    """
    def get_unique_paths(i: int = 0, j: int = 0) -> int:  # default cell (0, 0) -> start point
        # Base Case 1 (Reached Finish Point):
        if i == m-1 and j == n-1:
            return 1
        # Base Case 2 (IndexOutOfBound (Jumped of the Matrix)):
        if i == m or j == n:
            return 0
        # Recurse (Move Bottom | Move Right):
        return get_unique_paths(i+1, j) + get_unique_paths(i, j+1)

    return get_unique_paths()
    """

    # 1) Better (Recursion + Memoization): TC = O(m*n); SC = O(m*n)
    # In the brute-force approach, time complexity is increasing because of duplicate recursive calls
    # (check in recursion tree here: https://youtu.be/t_f0nwwdg5o?t=612)
    # So, we can simply store (MEMOIZE) the results of every recursive call in HashMap so that the same recursive call will never be made again,
    # rather it's result will be returned immediately.
    # Note: Turns out that since this is a recursive solution, and now we are using memoization in it,
    # it can apparently be called "DP (Memoization)"
    # DP: https://en.wikipedia.org/wiki/Dynamic_programming; https://en.wikipedia.org/wiki/Dynamic_programming#Computer_programming
    # Memoization: https://en.wikipedia.org/wiki/Memoization

    """
    def get_unique_paths(i: int = 0, j: int = 0, memoized: dict = None) -> int:  # default cell (0, 0) -> start point
        # Initialization (@ first call):
        if memoized is None:
            memoized = {}  # local to this function
        # Base Case 1 (Reached Finish Point):
        if i == m-1 and j == n-1:
            return 1
        # Base Case 2 (IndexOutOfBound (Jumped of the Matrix)):
        if i == m or j == n:
            return 0
        # If this is not a duplicate recursive call:
        if memoized.get((i, j)) is None:
            # Recurse (Move Bottom | Move Right) and memoize the result:
            memoized[(i, j)] = get_unique_paths(i+1, j, memoized) + get_unique_paths(i, j+1, memoized)
        # Return Result:
        return memoized[(i, j)]

    # memo = {}  # use global variables as less as possible
    # https://youtu.be/t_f0nwwdg5o?t=700
    # https://stackoverflow.com/questions/484635/are-global-variables-bad

    return get_unique_paths()
    """
    # Pythonic way of doing this 🤩:
    from functools import cache

    @cache
    def get_unique_paths(i: int = 0, j: int = 0) -> int:  # default cell (0, 0) -> start point
        # Base Case 1 (Reached Finish Point):
        if i == m-1 and j == n-1:
            return 1
        # Base Case 2 (IndexOutOfBound (Jumped of the Matrix)):
        if i == m or j == n:
            return 0
        # Recurse (Move Bottom | Move Right):
        return get_unique_paths(i+1, j) + get_unique_paths(i, j+1)

    return get_unique_paths()

    # 2) Better (DP): TC = O(m*n); SC = O(m*n)
    # https://leetcode.com/problems/unique-paths/discuss/22954/C%2B%2B-DP
    # https://leetcode.com/problems/unique-paths/discuss/1581998/C%2B%2BPython-5-Simple-Solutions-w-Explanation-or-Optimization-from-Brute-Force-to-DP-to-Math#:~:text=%E2%9C%94%EF%B8%8F%20Solution%20%2D%20III%20(Dynamic%20Programming%20%2D%20Tabulation)
