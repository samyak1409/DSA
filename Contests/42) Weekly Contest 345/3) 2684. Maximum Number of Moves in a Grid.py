"""
https://leetcode.com/problems/maximum-number-of-moves-in-a-grid
"""


def max_moves(grid: list[list[int]]) -> int:
    """"""

    # Consider using dynamic programming to find the maximum number of moves that can be made from each cell.
    # The final answer will be the maximum value in cells of the first column.

    # 0) [TLE] Brute-force (Try all using: Recursion (DFS)): TC = O(m * 3**n) {not sure}; SC = O(n) {recursion stack}

    """
    # Recursive Function:
    def recurse(r: int, c: int, prev_r: int = None) -> int:

        if (r == -1 or r == len(grid) or c == len(grid[0])) or (prev_r is not None and grid[r][c] <= grid[prev_r][c-1]):
            return 0

        return 1 + max(recurse(r-1, c+1, r), recurse(r, c+1, r), recurse(r+1, c+1, r))

    ans = 0
    for i in range(len(grid)):
        ans = max(ans, recurse(i, 0))
    return ans - 1
    """

    # 1) Sub-Optimal (Try all using: Recursion (DFS) + Bad Memoization):
    # TC = O(3*m*n) {checked using putting a counter inside func};
    # SC = O(3*m*n + n) {`3*`: extra because of bad memoization; `+ n`: recursion stack}
    # Just applied caching to above solution + a little concise.

    """
    from functools import cache

    # Caching so that if one cell is calc before, it'd be directly returned next time.
    @cache
    # Recursive Function:
    def recurse(r: int, c: int, prev_r: int = None) -> int:

        # Base case (Recurse out):
        if (r == -1 or r == m or c == n) or (prev_r is not None and grid[r][c] <= grid[prev_r][c-1]):
            # `r == -1 or r == m or c == n`: out of grid
            # `prev_r is not None and grid[r][c] <= grid[prev_r][c-1]`:
            # "the value of the cell you move to, should be strictly bigger than the value of the current cell"
            return 0

        # Recurse in:
        return 1 + max(recurse(r+dx, c+1, r) for dx in (-1, 0, +1))
        # Add the count for current, and recurse finding the max from the three cells we're allowed to go.

    # Grid dims:
    m, n = len(grid), len(grid[0])

    # Return the max from the first column ("start at any cell in the first column"):
    return max(recurse(r=row, c=0) for row in range(m)) - 1  # `- 1` coz moving on 1st col is not counted
    """

    # 2) Optimal (Try all using: Recursion (DFS) + Memoization): TC = O(m*n); SC = O(m*n + n)
    # Fix of the memoization problem of above.

    from functools import cache

    # Caching so that if one cell is calc before, it'd be directly returned next time.
    @cache
    # Recursive Function:
    def recurse(r: int, c: int) -> int:

        # Recurse in:
        # Add the count for current, and recurse finding the max from the three cells we're allowed to go.
        return 1 + max((recurse(r+dx, c+1) for dx in (-1, 0, +1)
                        if (0 <= r+dx < m and c+1 < n) and (grid[r+dx][c+1] > grid[r][c])), default=0)
        # `0 <= r+dx <= m and c < n`: if not out of grid
        # `grid[r+dx][c+1] > grid[r][c]`: "the value of the cell you move to, should be strictly bigger than the value
        # of the current cell"

    # Grid dims:
    m, n = len(grid), len(grid[0])

    # Return the max from the first column ("start at any cell in the first column"):
    return max(recurse(r=row, c=0) for row in range(m)) - 1  # `- 1` coz moving on 1st col is not counted
