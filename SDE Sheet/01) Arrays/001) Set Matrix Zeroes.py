"""
https://leetcode.com/problems/set-matrix-zeroes
"""


def set_zeroes(matrix: list[list[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """

    # 0) Brute-force (Copying matrix): TC = O(m*n); SC = O(m*n)

    """
    from copy import deepcopy

    # Create a copy:
    mat_copy = deepcopy(matrix)
    m, n = len(mat_copy), len(mat_copy[0])

    # For rows:
    for i in range(m):
        # Check if i-th row has a 0:
        if 0 in mat_copy[i]:
            # Set the row to 0:
            for j in range(n):
                matrix[i][j] = 0

    # For columns:
    for j in range(n):
        # Check if j-th col has a 0:
        if 0 in (mat_copy[i][j] for i in range(m)):
            # Set the col to 0:
            for i in range(m):
                matrix[i][j] = 0
    """

    # Follow up: A straightforward solution using O(mn) space is probably a bad idea. A simple improvement uses O(m+n)
    # space, but still not the best solution.

    # 1) Time-optimal (Using row & column arrays for/and marking 0s): TC = O(m*n); SC = O(m+n)

    """
    m, n = len(matrix), len(matrix[0])

    row, column = [False] * m, [False] * n  # for marking row & column indices of 0s; SC = O(m+n)
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                row[i] = True
                column[j] = True

    for i in range(m):
        for j in range(n):
            if row[i] or column[j]:
                matrix[i][j] = 0
    """

    # Follow up: Could you devise a constant space solution?

    # 2.1) Optimal (Setting to a placeholder value first, instead of 0): TC = O(m*n); SC = O(1)

    """
    m, n = len(matrix), len(matrix[0])

    # For rows:
    for i in range(m):
        # Check if i-th row has a 0:
        if 0 in matrix[i]:
            # Set the row to None:
            for j in range(n):
                # Avoid tempering the 0s, for future:
                if matrix[i][j] != 0:
                    matrix[i][j] = None

    # For columns:
    for j in range(n):
        # Check if j-th col has a 0:
        if 0 in (matrix[i][j] for i in range(m)):  # (note: using tuple comprehension so it's generator, so SC = O(1))
            # Set the col to None:
            for i in range(m):
                # Avoid tempering the 0s, for future:
                if matrix[i][j] != 0:
                    matrix[i][j] = None

    # At the end, convert all `None` to 0s:
    for i in range(m):
        for j in range(n):
            if matrix[i][j] is None:
                matrix[i][j] = 0
    """

    # 2.2) Optimal (Same logic as `1)`, just using the first row & column of the matrix itself): TC = O(m*n); SC = O(1)
    # The main trick in this algo (which allows solution in O(1) space):
    # Saving whether the rows/columns need to be set to 0s in the first row & column of the matrix,
    # to be more accurate, first cell of every row/column which needs to be set to 0,
    # AND the same mark of first row & column will be saved in two constant space vars, resulting in O(1) SC.

    m, n = len(matrix), len(matrix[0])

    # Saving whether the first row & column contain any 0s or not:
    first_row_zero, first_column_zero = 0 in matrix[0], 0 in (matrix[i][0] for i in range(m))
    # (note: using tuple comprehension so it's generator, so SC = O(1))

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0  # first row cell to 0
                matrix[0][j] = 0  # first column cell to 0

    # Setting rows & columns to 0:
    for i in range(1, m):  # IMP: skipping 1st row & column (next line), do you know why? :D
        # (will destroy what we saved in the first row & column)
        for j in range(1, n):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    # Now, if first row or column was needed to be set to 0:
    if first_row_zero:
        for k in range(n):
            matrix[0][k] = 0
    if first_column_zero:
        for k in range(m):
            matrix[k][0] = 0


# Similar Questions:
# https://leetcode.com/problems/game-of-life
# https://leetcode.com/problems/number-of-laser-beams-in-a-bank
