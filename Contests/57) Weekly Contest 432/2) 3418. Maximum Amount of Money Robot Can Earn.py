"""
https://leetcode.com/problems/maximum-amount-of-money-robot-can-earn
"""


def maximum_amount(coins: list[list[int]]) -> int:
    """"""

    # Similar to: https://github.com/samyak1409/DSA/blob/main/SDE%20Sheet/01%29%20Arrays/017%29%20Unique%20Paths.py

    # Test TLE/MLE:
    # from random import randint
    # coins = [[randint(-1000, 1000) for _ in range(500)] for _ in range(500)]
    # print(coins)  # debug

    # 1) Optimal (Recursion + Memo): TC = O(m*n*k); SC = O(m*n*k) {k = neutralizes = 2}
    # [Not hard at all.]
    # https://leetcode.com/problems/maximum-amount-of-money-robot-can-earn/solutions/6267298/iterative-dp-reccursive-dp-memoization-clean-code

    from functools import cache

    # Recursive Func:
    @cache
    def r(i: int, j: int, k: int) -> int | float:
        if i >= m or j >= n:  # -ve base case: went out of grid
            return float('-inf')  # so that this path is not considered in any condition
        if i == m - 1 and j == n - 1:  # +ve base case: reached at bottom left cell
            # If we've neutralizes left, and curr val is -ve, skip picking it:
            return max(coins[i][j], 0) if k else coins[i][j]
        # Recurse in:
        # If we've neutralizes left AND CURR VAL IS -VE, try both picking and not picking the curr val,
        # Else,                                          try just picking:
        pick = coins[i][j] + max(r(i, j+1, k), r(i+1, j, k))  # pick, so `k` remains the same
        not_pick = max(r(i, j+1, k-1), r(i+1, j, k-1)) if (k and coins[i][j] < 0) else float('-inf')
        return max(pick, not_pick)

    m, n = len(coins), len(coins[0])
    return r(i=0, j=0, k=2)  # i: row index, j: col index, k: neutralizes left
