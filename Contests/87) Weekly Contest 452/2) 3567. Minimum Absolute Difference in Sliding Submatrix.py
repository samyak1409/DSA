"""
https://leetcode.com/problems/minimum-absolute-difference-in-sliding-submatrix
"""


def min_abs_diff(grid: list[list[int]], k: int) -> list[list[int]]:
    """"""

    # 1) Brute-force (Loop, HashSet, Sort): TC = O(m-k * n-k * k^2 * log2(k)); SC = O(k^2)

    m, n = len(grid), len(grid[0])
    # Dimensions of `ans`:
    m_, n_ = m-k+1, n-k+1

    # Init ans:
    ans = [[0]*n_ for _ in range(m_)]

    # `i` & `j` are the starting points of submatrix:
    for i in range(m_):  # O(m-k)
        for j in range(n_):  # O(n-k)

            # HashSet to only save distinct vals:
            hs = set()

            # Loop on the k*k submatrix to add the vals:
            for i_ in range(i, i+k):  # O(k)
                for j_ in range(j, j+k):  # O(k)
                    hs.add(grid[i_][j_])

            # If we don't have at least 2 distinct vals, then the ans would be 0 only, so skip:
            if len(hs) >= 2:

                # Now, just find the min abs diff:
                vals = sorted(hs)  # O(k^2 * log2(k^2)) = O(k^2 * 2 * log2(k)) = O(k^2 * log2(k))
                mn = float('inf')
                for i_ in range(len(vals)-1):  # O(k)
                    mn = min(mn, vals[i_+1]-vals[i_])
                ans[i][j] = mn

    return ans
