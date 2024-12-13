"""
https://leetcode.com/problems/difference-of-number-of-distinct-values-on-diagonals
"""


def difference_of_distinct_values(grid: list[list[int]]) -> list[list[int]]:
    """"""

    # Hint: Use the set to count the number of distinct elements on diagonals.

    # 1) Brute-force (Simulation: Calc ans. for each grid element one by one):
    # TC = O(m*n * min(m, n))); SC = O(min(m, n))

    """
    m, n = len(grid), len(grid[0])
    ans = []

    # Loop on grid elements, and for each element calc. ans:
    for r in range(m):
        ans.append([])
        for c in range(n):

            # Using for loop (Shorter but trickier (defining range params)): TC = SC = O(min(m, n))
            '''
            s1 = {grid[r-dx][c-dx] for dx in range(1, min(r, c)+1)}   # distinct vals in top-left diagonal
            s2 = {grid[r+dx][c+dx] for dx in range(1, min(m-r, n-c))} #                  bottom-right
            '''

            # Using while loop (Longer but easier): TC = SC = O(min(m, n))
            s1, s2 = set(), set()
            r1, c1 = r, c
            while (r1 := r1-1) >= 0 and (c1 := c1-1) >= 0:
                s1.add(grid[r1][c1])
            r1, c1 = r, c
            while (r1 := r1+1) < m and (c1 := c1+1) < n:
                s2.add(grid[r1][c1])

            ans[-1].append(abs(len(s1)-len(s2)))

    return ans
    """

    # 2) Optimal (Traverse every diagonal two times (Prefix,Suffix)): TC = O(m*n); SC = O(m*n)

    # Traverse diagonal wise two times, one from top to bottom, and another from bottom to top, then calc and save the
    # ans:
    """
    m, n = len(grid), len(grid[0])
    diagonals = []
    for r, c in *((row, 0) for row in range(m-1, -1, -1)), *((0, col) for col in range(1, n)):
        unique = set()
        pre = [0]
        while r < m and c < n:
            unique.add(grid[r][c])
            pre.append(len(unique))
            r, c = r+1, c+1
        r, c = r-1, c-1
        unique.clear()
        suf = [0]
        while r >= 0 and c >= 0:
            unique.add(grid[r][c])
            suf.append(len(unique))
            r, c = r-1, c-1
        suf.reverse()
        diagonals.append([abs(pre[i]-suf[i+1]) for i in range(len(pre)-1)])

    ans = []
    for r in range(m):
        ans.append([])
        for c in range(n):
            ans[-1].append(diagonals[c-r+m-1][min(r, c)])
    return ans
    """

    # Concise: What we can also do is, save top to bottom in `ans` grid only, and then traverse `ans` again while calc.
    # bottom to top, and update the cells with actual answers:

    from itertools import chain

    # Get grid dimensions:
    m, n = len(grid), len(grid[0])
    # Init 2D ans. arr:
    ans = [[0]*n for _ in range(m)]

    # Loop on starting co-ordinates of all the diagonals (bottom-up): TC = O(m*n)
    # (How? Take a 3*3 grid for example. Take 1st column in reverse, and then 1st row (skipping it's 1st element).)
    #     4 5
    # 3 x x x
    # 2 x x x
    # 1 x x x
    # (Numbers show how we move.)
    for r, c in chain(((row, 0) for row in range(m-1, -1, -1)), ((0, col) for col in range(1, n))):

        # Set to track unique elements: SC = O(min(m, n))
        unique = set()
        # Traverse this diagonal (going bottom-right):
        while r < m and c < n:
            # (Intermediate ans) Save num of distinct vals in top-left diagonal:
            ans[r][c] = len(unique)
            # Add curr el in set:
            unique.add(grid[r][c])
            # ++ the indices:
            r, c = r+1, c+1

        # Bring the indices back in bound:
        r, c = r-1, c-1
        # Clear the set to reuse:
        unique.clear()
        # Traverse this diagonal (going top-left):
        while r >= 0 and c >= 0:
            # (Final ans) Update w/ num of distinct vals in bottom-right diagonal:
            ans[r][c] = abs(ans[r][c]-len(unique))
            # Add curr el in set:
            unique.add(grid[r][c])
            # -- the indices:
            r, c = r-1, c-1

    # Return ans.:
    return ans
