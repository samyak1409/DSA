"""
https://leetcode.com/problems/sort-matrix-by-diagonals
"""


def sort_matrix(grid: list[list[int]]) -> list[list[int]]:
    """"""

    # 1) Optimal (Loop on diagonals one by one): TC = O(n^2 + n*(n*log(n))) = O(n^2 * log(n)); SC = O(n)
    # Looping over the diagonals one by one from up to down, meaning first loop on top-right diagonal, and so on till
    # the bottom-left diagonal, and replacing each diagonal one by one with their sorted values.
    # The main part in this approach is correctly looping by playing with the indices.

    """
    # No. of diagonals = 2*n - 1:
    for i in range(1, 2*(n:=len(grid))):
        if i < n:  # upper diagonals
            nums = []
            # Store the nums in the curr diagonal:
            for j in range(i):
                nums.append(grid[j][n-i+j])
            # Sort the nums:
            nums.sort()
            # Replace in the diagonal:
            for j in range(i):
                grid[j][n-i+j] = nums[j]
        else:  # lower diagonals
            nums = []
            # Store the nums in the curr diagonal:
            for j in range(2*n-i):
                nums.append(grid[i-n+j][j])
            # Sort the nums:
            nums.sort(reverse=True)
            # Replace in the diagonal:
            for j in range(2*n-i):
                grid[i-n+j][j] = nums[j]

    # Debug:
    for row in grid:
        print(row)

    return grid
    """

    # Hint:
    # "Try establishing a relation using i and j indexes for diagonal elements."
    # -https://leetcode.com/problems/sort-matrix-by-diagonals/description/comments/2847044

    # Next two solutions are wrong because:
    # "These exact elements need to be sorted and placed back on the diagonals where they were originally given."
    # -https://leetcode.com/problems/sort-matrix-by-diagonals/description/comments/2845854

    # 0.1) [WA] Time-optimal (Two Pointers): TC = O(n^2 + (n^2)*log(n^2)) = O(n^2 * log(n)); SC = O(n^2)
    # Assumed that all the nums in the grid can go anywhere as long as the two conditions mentioned in the problem are
    # matched.

    """
    # Store all the nums in an arr:
    nums = []
    for r in range(n:=len(grid)):
        for c in range(n):
            nums.append(grid[r][c])
    # Sort the arr:
    nums.sort()

    # Use two pointers left & right to get the lowest and the biggest nums, and overwrite to the grid:
    lt, rt = -1, n * n  # (https://chrissardegna.com/blog/python-expontentiation-performance)
    for r in range(n):
        for c in range(n):
            grid[r][c] = nums[lt:=lt+1] if r < c else nums[rt:=rt-1]
            # If `r < c` means we're in the upper triangle of the grid:
            # e.g. see the row and column indices on a 3x3 grid:
            # (0,0) (0,1) (0,2)
            # (1,0) (1,1) (1,2)
            # (2,0) (2,1) (2,2)

    # Debug:
    for row in grid:
        print(row)

    return grid
    """

    # 0.2) [WA] Time-optimal (Store nums in two separate arr): TC = O(n^2 * log(n)); SC = O(n^2)
    # Assumed that all the nums in the upper triangle can go anywhere in the upper triangle, and same for lower
    # triangle, as long as the two conditions mentioned in the problem are matched.

    """
    # Store the nums in upper and lower triangle in two separate arrays:
    nums1, nums2 = [], []
    for r in range(n:=len(grid)):
        for c in range(n):
            (nums1 if r < c else nums2).append(grid[r][c])
    # Sort:
    nums1.sort(), nums2.sort(reverse=True)

    # Overwrite:
    i = j = -1
    for r in range(n):
        for c in range(n):
            grid[r][c] = nums1[i:=i+1] if r < c else nums2[j:=j+1]
            # If `r < c` means we're in the upper triangle of the grid:
            # e.g. see the row and column indices on a 3x3 grid:
            # (0,0) (0,1) (0,2)
            # (1,0) (1,1) (1,2)
            # (2,0) (2,1) (2,2)

    # Debug:
    for row in grid:
        print(row)

    return grid
    """

    # 0.3) Time-optimal (`r-c` as hashmap key): TC = O(n^2 * log(n)); SC = O(n^2)
    # Even though this solution is not space-optimal, but still is the best one practically due to its simplicity.
    # `1)` is little complicated to code out because of indices for looping diagonal by diagonal.
    # `r-c`: Cool math!
    # `r-c` values for each index in the grid:
    # +0 -1 -2
    # +1 +0 -1
    # +2 +1 +0

    from collections import defaultdict

    hm = defaultdict(list)  # (key: value) = (r-c: [grid[r][c], ...])
    # Using `r-c` to store each diagonal nums to separate arrays:
    for r in range(n:=len(grid)):
        for c in range(n):
            hm[r-c].append(grid[r][c])

    '''
    # Sort each array one by one:
    for k in hm:
        hm[k].sort(reverse=k>=0)  # `k>=0`: True if "bottom-left triangle (including the middle diagonal)" else False
        hm[k].append(0)  # index to know on which element we're currently in this array
    
    # Loop on the grid, and overwrite:
    for r in range(n):
        for c in range(n):
            grid[r][c] = hm[r-c][hm[r-c][-1]]  # `hm[r-c][-1]`: index
            hm[r-c][-1] += 1  # ++ the index
    '''

    # Sort each array one by one:
    for k in hm:
        hm[k].sort(reverse=k<0)  # `k<0` instead of `k>=0` (see above commented snippet) so that we do not need to keep
        # an index, and we can just pop from the last (like a stack) as it's O(1).

    # Loop on the grid, and overwrite:
    for r in range(n):
        for c in range(n):
            grid[r][c] = hm[r-c].pop()  # `pop()` so that next time we've next num on the top of the arr

    # Debug:
    for row in grid:
        print(row)

    return grid

    # One more insight, if we do `r+c` as hm key for diagonals, we'd get diagonals like:
    # 0 1 2
    # 1 2 3
    # 2 3 4
    # i.e. from right to left.
    # Using `r-c` (or `c-r`), we got left to right.
