"""
https://leetcode.com/problems/maximum-number-of-fish-in-a-grid
"""


def find_max_fish(grid: list[list[int]]) -> int:
    """"""

    # Run DFS from each non-zero cell.
    # Each time you pick a cell to start from, add up the number of fish contained in the cells you visit.

    # -1) [WA] Sub-Optimal (DFS for every cell): TC = O(m*n * ?); SC = O(m*n)
    # This implementation is wrong because it just travels through the cell once, and then never visits it again (for
    # every starting cell). So, this implementation would be correct for the problems where there is given that we can
    # visit a cell only once while traversing.
    # Input:    grid = [[4, 5, 5], [0, 10, 0]]
    # Output:   20
    # Expected: 24

    """
    # Recursive Function: TC = O(?); SC = O(m*n)
    def get_fishes_recursively(r: int, c: int) -> int:

        # Base Case:
        if not (0 <= r < m) or not (0 <= c < n) or grid[r][c] == 0 or (r, c) in visited:
            # `not (0 <= r < m) or not (0 <= c < n)`: out of grid
            # `grid[r][c] == 0`: "Move to any adjacent water cell."
            # `(r, c) in visited`: avoid revisiting a cell and creating a loop
            return 0  # recurse out

        # Update visited:
        visited.add((r, c))

        # "Catch all the fish at cell (r, c)" and recurse in (consider the cell which gives the highest count):
        return grid[r][c] + max(get_fishes_recursively(r, c+1), get_fishes_recursively(r, c-1),
                                get_fishes_recursively(r+1, c), get_fishes_recursively(r-1, c))

    m, n = len(grid), len(grid[0])
    max_fishes = 0

    # Calc. from every cell:
    for i in range(m):  # O(m*n * ?)
        for j in range(n):  # O(n * ?)
            visited = set()  # to track visited cells, else we'll recurse indefinitely from a cell to other; SC = O(m*n)
            max_fishes = max(max_fishes, get_fishes_recursively(i, j))  # update max if required

    return max_fishes
    """

    # 1) Sub-Optimal (DFS for every cell): TC = O(m*n * ?); SC = O(m*n)

    """
    # Recursive Function: TC = O(?); SC = O(m*n)
    def dfs(r: int, c: int) -> None:

        # Base Case:
        if not (0 <= r < m) or not (0 <= c < n) or grid[r][c] == 0 or (r, c) in visited:
            # `not (0 <= r < m) or not (0 <= c < n)`: out of grid
            # `grid[r][c] == 0`: "Move to any adjacent water cell."
            # `(r, c) in visited`: avoid revisiting a cell and creating a loop
            return  # recurse out

        # Update visited:
        visited.add((r, c))

        # Recurse in (Traverse in all the 4 directions):
        for r, c in ((r, c+1), (r, c-1), (r+1, c), (r-1, c)):
            dfs(r, c)

    m, n = len(grid), len(grid[0])
    max_fishes = 0

    # Calc. from every cell:
    for i in range(m):  # O(m*n * ?)
        for j in range(n):  # O(n * ?)
            visited = set()  # to track visited cells, else we'll recurse indefinitely from a cell to other; SC = O(m*n)
            dfs(i, j)  # fills `visited`
            max_fishes = max(max_fishes, sum(grid[r][c] for r, c in visited))
            # get total fish count from this traversal & update max if required

    return max_fishes
    """

    # 2) Optimal (DFS for every cell but global `visited`): TC = O(m*n) {as visiting every cell only once}; SC = O(m*n)
    # Just got to know from "Approach #1: Depth-First Search (Recursive) [Accepted]" in
    # https://leetcode.com/problems/max-area-of-island/editorial that changing `max` to `sum` in `-1)` would solve the
    # problem!
    # And taking `visited` reduce the time and make it optimal. Think why we can take `visited` as global!

    # Recursive Function:
    def get_fishes_recursively(r: int, c: int) -> int:

        # Base Case:
        if not (0 <= r < m) or not (0 <= c < n) or grid[r][c] == 0 or (r, c) in visited:
            # `not (0 <= r < m) or not (0 <= c < n)`: out of grid
            # `grid[r][c] == 0`: "Move to any adjacent water cell."
            # `(r, c) in visited`: avoid revisiting a cell and creating a loop
            return 0  # recurse out

        # Update visited:
        visited.add((r, c))

        # "Catch all the fish at cell (r, c)" and recurse in (consider the sum from all cells):
        return grid[r][c] + sum((get_fishes_recursively(r, c+1), get_fishes_recursively(r, c-1),
                                 get_fishes_recursively(r+1, c), get_fishes_recursively(r-1, c)))

    m, n = len(grid), len(grid[0])
    max_fishes = 0
    visited = set()  # to track visited cells, else we'll recurse indefinitely from a cell to other; SC = O(m*n)

    # Calc. from every cell:
    for i in range(m):
        for j in range(n):
            max_fishes = max(max_fishes, get_fishes_recursively(i, j))  # update max if required

    return max_fishes


# Similar Questions:
# https://leetcode.com/problems/max-area-of-island
