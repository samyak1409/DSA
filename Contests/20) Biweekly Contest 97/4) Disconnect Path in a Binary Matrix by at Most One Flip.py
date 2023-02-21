"""
https://leetcode.com/problems/disconnect-path-in-a-binary-matrix-by-at-most-one-flip
"""


def is_possible_to_cut_path(grid: list[list[int]]) -> bool:
    """"""

    # We can consider the grid a graph with edges between adjacent cells.
    # If you can find two non-intersecting paths from (0, 0) to (m - 1, n - 1) then the answer is false. Otherwise, it
    # is always true.

    # 1) Optimal (DFS 2 Times): TC = O(m*n); SC = O(m*n)
    # Run DFS and mark a path with 0s, run DFS again and check if a path is left.
    # https://leetcode.com/problems/disconnect-path-in-a-binary-matrix-by-at-most-one-flip/solutions/3141656/explained-run-dfs-2-times-very-simple-and-easy-to-understand-solution

    from copy import deepcopy
    grid = deepcopy(grid)  # avoiding modifying the input grid by making a local deep-copied grid (just a good practice)
    # TC = O(m*n); SC = O(m*n)

    m, n = len(grid), len(grid[0])

    # Recursive Function: TC = O(m*n); SC = O(m+n) {recursion stack}
    def has_path(i: int = 0, j: int = 0) -> bool:

        # Base Cases:
        if i == m or j == n:  # went out of grid
            return False
        if grid[i][j] == 0:  # can't move through a cell with value 0
            return False
        if i == m-1 and j == n-1:  # reached to the destination
            return True

        grid[i][j] = 0  # mark the path with 0

        # Recurse:
        return has_path(i+1, j) or has_path(i, j+1)
        # IMP: By using `or`, it's made sure that we only make a single path 0 and not all the paths 0.

    if not has_path():  # no path found => matrix is already disconnected
        return True

    # So, if we reached here, that means the grid has >= 1 path(s). And, `grid[i][j] = 0` has marked one of the paths
    # with 0s. So, now we'll run the DFS once again and if we still find a path, that would mean that it's impossible
    # to disconnect the grid using at most 1 flip!

    grid[0][0] = 1  # (flip the start back to 1 that was flipped to 0 while first DFS)
    # [print(row) for row in grid]  #debugging
    return not has_path()  # `return False if has_path() else True`
