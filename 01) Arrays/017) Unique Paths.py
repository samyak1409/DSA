"""
https://leetcode.com/problems/unique-paths
"""


def unique_paths(m: int, n: int) -> int:
    """"""

    # 0) [TLE] Brute-force (Recursion): TC = O(2^(m+n)); SC = O(m+n)
    # The formula to determine the time complexity for recursion = branches ^ depth = the number of nodes in the
    # recursion tree.
    # In our case, we have 2 possible branches (going down or going right), while for the depth, is the maximum possible
    # distance taken to get (m, n) which is m + n.
    # Given this, we can also mention the space complexity taken on the stack: O(m+n)

    """
    def get_unique_paths(i: int = 0, j: int = 0) -> int:  # default cell (0, 0) -> start point
        # Base Case 1 (IndexOutOfBound (Jumped out of the Matrix)):
        if i == m or j == n:
            return 0
        # Base Case 2 (Reached Finish Point):
        if i == m-1 and j == n-1:
            return 1
        # Recurse (Move Bottom | Move Right):
        return get_unique_paths(i+1, j) + get_unique_paths(i, j+1)

    return get_unique_paths()
    """

    # 1) Better (Recursion + Memoization): TC = O(m*n); SC = O(m*n)
    # In the brute-force approach, time complexity is increasing because of duplicate recursive calls
    # (check in recursion tree here: https://youtu.be/t_f0nwwdg5o?t=612)
    # So, we can simply store (MEMOIZE) the results of every recursive call in HashMap so that the same recursive call
    # will never be made again, rather it's result will be returned immediately.
    # Note: Turns out that since this is a recursive solution, and now we are using memoization in it,
    # it can apparently be called "DP (Memoization)"
    # DP: https://en.wikipedia.org/wiki/Dynamic_programming;
    #     https://en.wikipedia.org/wiki/Dynamic_programming#Computer_programming
    # Memoization: https://en.wikipedia.org/wiki/Memoization

    """
    def get_unique_paths(i: int = 0, j: int = 0, memoized: dict = None) -> int:  # default cell (0, 0) -> start point
        # Initialization (@ first call):
        if memoized is None:
            memoized = {}  # local to this function
        # Base Case 1 (IndexOutOfBound (Jumped out of the Matrix)):
        if i == m or j == n:
            return 0
        # Base Case 2 (Reached Finish Point):
        if i == m-1 and j == n-1:
            return 1
        # If this is not a duplicate recursive call:
        if memoized.get((i, j)) is None:
            # Recurse (Move Bottom | Move Right) and Memoize the Result:
            memoized[(i, j)] = get_unique_paths(i+1, j, memoized) + get_unique_paths(i, j+1, memoized)
        # Return Result:
        return memoized[(i, j)]

    # memo = {}  # use global variables as less as possible
    # https://youtu.be/t_f0nwwdg5o?t=700
    # https://stackoverflow.com/questions/484635/are-global-variables-bad

    return get_unique_paths()
    """
    # Pythonic way of doing this 🤩:
    """
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
    """

    # 2) Better (DP): TC = O(m*n); SC = O(m*n)
    # https://leetcode.com/problems/unique-paths/discuss/22954/C%2B%2B-DP
    # https://leetcode.com/problems/unique-paths/discuss/1581998#:~:text=Solution%20%2D%20III%20(Dynamic%20Programming%20%2D%20Tabulation)

    # 3) Optimal (Maths): TC = O(min(m, n)); SC = O(1)
    # https://youtu.be/t_f0nwwdg5o?t=817
    # Intuition: If we observe examples there is a similarity in paths from start to end.
    # From start to end we need a certain no. of down & right steps i.e. (m-1) & (n-1) respectively.
    # So each time we are taking exactly (m+n-2) steps to reach the end.
    #
    #     Out of total (m+n-2) steps, if we choose total (m-1) down steps or total (n-1) right steps, and calculate the
    #     Combinations (i.e.: C(m+n-2, m-1) or C(m+n-2, n-1)), we’ll get the total number of unique paths.
    #     Why? Not able to understand even after hours of trying :(
    #
    #     Instead understood it like: (Source: https://youtu.be/m7chPc7zIF4)
    #     We have to find all the unique WAYS, so it looks like we have to use Permutations:
    #     We know we have to take exactly (m+n-2) steps, and we got (m-1) down & (n-1) right steps,
    #     so Total Ways = P(m+n-2, (m-1)+(n-1)) = P(m+n-2, m+n-2) = (m+n-2)!
    #     but wait, changing the internal order of down & right steps doesn't matter
    #     i.e. DRR and RRD are different, but DRR and DRR {order of R is opposite} are same.
    #     So removing this: Total Unique Ways = (m+n-2)! / (m-1)!(n-1)!
    #     Which turns out to be the formula of Combinations, N = m+n-2; R = m-1 (or n-1) => (N-R) = n-1 (or m-1)
    #
    # => Total Unique Ways = C(m+n-2, m-1) or C(m+n-2, n-1)
    # https://leetcode.com/problems/unique-paths/discuss/22958/Math-solution-O(1)-space
    # https://leetcode.com/problems/unique-paths/discuss/1581998#:~:text=Solution%20%2D%20V%20(Math)

    """
    N = m + n - 2  # m-1 + n-1
    r = min(m, n) - 1  # m-1 or n-1
    # Calculating comb(n, r) (Using the trick: comb(10, 3) = 10*9*8 / 3*2*1):
    denominator = numerator = 1
    for i in range(r, 0, -1):
        denominator *= i
        numerator *= N-r+i
    return numerator // denominator
    """
    # Or:
    from math import comb
    return comb(m+n-2, min(m, n)-1)


# Similar Question: https://leetcode.com/problems/unique-paths-ii
