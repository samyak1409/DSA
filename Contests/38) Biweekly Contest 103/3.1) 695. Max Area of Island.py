"""
https://leetcode.com/problems/max-area-of-island
"""


def max_area_of_island(grid: list[list[int]]) -> int:
    """"""

    # Same as `2658. Maximum Number of Fish in a Grid`.

    # 1) Optimal (DFS for every cell): TC = O(m*n); SC = O(m*n)
    # "Approach #1: Depth-First Search (Recursive) [Accepted]" in
    # https://leetcode.com/problems/max-area-of-island/editorial

    # Recursive Function:
    def get_area_recursively(r: int, c: int) -> int:

        # Base Case:
        if not (0 <= r < m) or not (0 <= c < n) or grid[r][c] == 0 or (r, c) in visited:
            # `not (0 <= r < m) or not (0 <= c < n)`: out of grid
            # `grid[r][c] == 0`: 0 means water
            # `(r, c) in visited`: avoid revisiting a cell and creating a loop
            return 0  # recurse out

        # Update visited:
        visited.add((r, c))

        # Recurse in (consider the sum from all cells):
        return 1 + get_area_recursively(r, c+1) + get_area_recursively(r, c-1) \
                 + get_area_recursively(r+1, c) + get_area_recursively(r-1, c)

    m, n = len(grid), len(grid[0])
    max_area = 0
    visited = set()  # to track visited cells, else we'll recurse indefinitely from a cell to other; SC = O(m*n)

    # Calc. from every cell:
    for i in range(m):
        for j in range(n):
            max_area = max(max_area, get_area_recursively(i, j))  # update max if required

    return max_area
