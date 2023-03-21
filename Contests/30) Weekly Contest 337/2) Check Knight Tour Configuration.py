"""
https://leetcode.com/problems/check-knight-tour-configuration
"""


def check_valid_grid(grid: list[list[int]]) -> bool:
    """"""

    # It is enough to check if each move of the knight is valid.
    # Try all cases of the knight's movements to check if a move is valid.

    # 2) Time-Optimal (Loops (+HashSet)): TC = O(n*n); SC = O(n*n)
    # Change the data format, so we know where the next visited cell is.
    # Then check if it's valid or not. Repeat this for all the next cells.
    # https://leetcode.com/problems/check-knight-tour-configuration/solutions/3314019/collect-coordinates

    """
    # For edge case when knight doesn't start from the top-left cell:
    if grid[0][0]:
        return False

    # Pre-process: Changing the data format:
    n = len(grid)
    co_ords = [tuple()] * (n*n)  # co-ords[i] stores the co-ords of the i-th visited cell by the knight; SC = O(n*n)
    for i in range(n):
        for j in range(n):
            co_ords[grid[i][j]] = (i, j)

    # Main:
    # diffs = {(+1, -2), (+2, -1), (+2, +1), (+1, +2), (-1, +2), (-2, +1), (-2, -1), (-1, -2)}
    for i in range(n*n - 1):  # O(n*n)
        cur, nxt = co_ords[i], co_ords[i+1]
        # if (nxt[0]-cur[0], nxt[1]-cur[1]) not in diffs:  # O(1); kids
        # if {abs(nxt[0]-cur[0]), abs(nxt[1]-cur[1])} != {2, 1}:  # men
        if abs((nxt[0]-cur[0])*(nxt[1]-cur[1])) != 2:  # legends
            return False
    return True
    """

    # 1) Brute-force = Optimal (Loops): TC = O(n*n * 8) = O(n*n); SC = O(1)
    # Start from 0th cell and try all the 8 possible moves to find next valid cell.
    # Repeat this for all the next cells.

    # This edge case 💀*10: [[8, 3, 6],
    #                        [5, 0, 1],
    #                        [2, 7, 4]]
    if grid[0][0]:
        return False

    n = len(grid)
    moves = ((+1, -2), (+2, -1), (+2, +1), (+1, +2), (-1, +2), (-2, +1), (-2, -1), (-1, -2))
    curr = (0, 0)

    for i in range(1, n*n):  # i: th cell that the knight visited; O(n*n * 8)
        for x, y in moves:  # check all the moves; O(8)
            x, y = x+curr[0], y+curr[1]
            if 0 <= x < n and 0 <= y < n and grid[x][y] == i:  # if indices valid, and we get the correct num
                curr = (x, y)  # update curr
                break
        else:  # none of the moves from the current co-ordinate, lead to the correct num
            return False

    return True

    # https://leetcode.com/problems/check-knight-tour-configuration/solutions/3314019/collect-coordinates/comments/1839901
