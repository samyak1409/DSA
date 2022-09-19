"""
https://leetcode.com/problems/set-matrix-zeroes
"""


def set_zeroes(matrix: list[list[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """

    # 0.1) Brute-force (Storing co-ordinates "(i, j)" in an array): TC = O(m*n*(m+n)); SC = O(m*n)

    """
    m, n = len(matrix), len(matrix[0])  # getting no. of rows & columns

    zeroes = []  # for storing co-ordinates of 0s
    for i in range(m):  # TC = O(m*n)
        for j in range(n):
            if matrix[i][j] == 0:
                zeroes.append((i, j))  # if whole matrix is 0, SC = O(m*n)
    # print(zeroes)  #debugging

    for i, j in zeroes:  # if whole matrix is 0, then this loop will run O(m*n) times, so total TC = O(m*n*(m+n))
        # making rows 0:
        for index in range(n):
            matrix[i][index] = 0
        # making columns 0:
        for index in range(m):
            matrix[index][j] = 0
    """

    # 0.2) Space-Optimal Brute-force (Temporarily changing the values to a placeholder value): TC = O(m*n*(m+n));
    #                                                                                        SC = O(1)

    """
    m, n = len(matrix), len(matrix[0])  # getting no. of rows & columns

    for i in range(m):  # O(m)
        for j in range(n):  # O(n)
            if matrix[i][j] == 0:
                # making rows 0:
                for k in range(n):  # O(n)
                    if matrix[i][k] != 0:  # because if we'll change it to None, it (and so it's column) will be
                        # skipped in future iterations
                        matrix[i][k] = None
                # making columns 0:
                for k in range(m):  # O(m)
                    if matrix[k][j] != 0:  # because if we'll change it to None, it (and so it's row) will be
                        # skipped in future iterations
                        matrix[k][j] = None

    # after above iterations, the matrix will be solution ready just with None values in place of 0s,
    # changing the None values back to 0:
    for i in range(m):
        for j in range(n):
            if matrix[i][j] is None:
                matrix[i][j] = 0
    """

    # Follow up: A straightforward solution using O(mn) space is probably a bad idea. A simple improvement uses O(m+n)
    # space, but still not the best solution.
    # 1) Better (Using row & column arrays for/and marking 0s): TC = O(m*n); SC = O(m+n)

    """
    m, n = len(matrix), len(matrix[0])  # getting no. of rows & columns

    row, column = [False]*m, [False]*n  # for marking row & column indices of 0s; SC = O(m+n)
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                row[i] = True
                column[j] = True
    # print(row, column)  #debugging

    for i in range(m):
        for j in range(n):
            if row[i] or column[j]:
                matrix[i][j] = 0
    """

    # Follow up: Could you devise a constant space solution?
    # 2) Optimal (Same logic as above, just using the first row & column of the matrix itself): TC = O(m*n); SC = O(1)
    # the main trick in this algo (which allows solution in O(1) space):
    # saving whether the rows/columns need to be set to 0s in the first row & column of the matrix,
    # to be more accurate, first cell of every row/column which needs to be set to 0
    # AND the same mark of first row & column will be saved in two constant space vars, resulting in O(1) SC!!

    m, n = len(matrix), len(matrix[0])  # getting no. of rows & columns

    # saving whether the first row & column contain any 0s or not:
    first_row_zero, first_column_zero = 0 in matrix[0], 0 in [row[0] for row in matrix]
    # Additional Note: Using `row[0] for row in matrix` instead of `matrix[i][0] for i in range(m)` above,
    # still the SC = O(1) because row has not allocated extra space but is pointing to the matrix only!

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0  # first row cell to 0
                matrix[0][j] = 0  # first column cell to 0

    # setting rows & columns to 0:
    for i in range(1, m):  # IMP: skipping 1st row & column (next line), do you know why? :D
        # (will destroy what we saved in the first row & column)
        for j in range(1, n):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    # now, if first row or column was needed to be set to 0:
    if first_row_zero:
        for k in range(n):
            matrix[0][k] = 0
    if first_column_zero:
        for k in range(m):
            matrix[k][0] = 0


# Similar Questions:
# https://leetcode.com/problems/game-of-life
# https://leetcode.com/problems/number-of-laser-beams-in-a-bank
