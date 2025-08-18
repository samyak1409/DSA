"""
https://leetcode.com/problems/minimum-cost-path-with-alternating-directions-ii
"""


from functools import cache


def min_cost(m: int, n: int, w: list[list[int]]) -> int:
    """"""

    # [Easy question.]

    # 1) [MLE, all testcases passed] Time-optimal (Recursion + Memo (i, j, s)): TC = O(m*n); SC = O(m*n*2)
    # [Came up with myself.]

    """
    @cache
    def r(i: int, j: int, s: int) -> int:
        # Out of bound:
        if i == m or j == n:
            return float('inf')
        
        # Reached destination:
        if i == m-1 and j == n-1:
            return (i+1) * (j+1)
        
        # Odd second:
        if s % 2:
            # Curr cell entry cost + Now next we need to wait, so no moving, just increasing the second:
            return (i+1)*(j+1) + r(i, j, s+1)
        
        # Even second:
        # Wait cost + Next we need to move to either right or down:
        return w[i][j] + min(r(i, j+1, s+1), r(i+1, j, s+1))

    # return 1 + min(r(0, 1, 1), r(1, 0, 1))
    # `1` = entry cost for first cell ((0+1)*(0+1))

    # Or, instead of handling first cell separately, if we make the wait time of first cell = 1,
    w[0][0] = 1
    # we can do:
    return r(0, 0, 0)
    # Dry-run to get how it works. It's very easy.
    """

    # 2) Optimal (Recursion + Memo (i, j)): TC = O(m*n); SC = O(m*n)
    # [Came up with myself.]
    # It turns out this was kind of a trick problem. The second counter `s`
    # is actually redundant. For any intermediate cell (i, j) on the path,
    # you always pay its entry cost AND its wait cost before moving on.
    # So, the cost of visiting any intermediate cell is simply (i+1)*(j+1) + w[i][j].
    # This simplifies the problem to a standard grid path-finding problem. The only
    # special cases are the start and the end (no wait cost).

    @cache
    def r(i: int, j: int, s: int) -> int:
        if i == m or j == n:
            return float('inf')
        if i == m-1 and j == n-1:
            return (i+1) * (j+1)
        
        # The cost of any path through an intermediate cell (i, j) is the
        # cell's combined cost (entry + wait) plus the minimum cost to proceed.
        return (i+1)*(j+1) + w[i][j] + min(r(i, j+1, s+1), r(i+1, j, s+1))

    # We handle the start cell's special case (no wait cost) by setting its
    # wait cost to 0. The formula then correctly calculates the cost for (0,0)
    # as (0+1)*(0+1) + 0 = 1, which is just its entry cost.
    w[0][0] = 0
    return r(0, 0, 0)
    # Dry-run to get how it works. It's very easy.
