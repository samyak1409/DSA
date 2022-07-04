"""
https://leetcode.com/problems/set-matrix-zeroes
"""


from typing import List


def setZeroes(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """

    # 0) Brute-force (storing co-ordinates in a list): TC = O(m*n*(m+n)); SC = O(m*n)

    """
    m, n = len(matrix), len(matrix[0])  # getting no. of rows & columns

    zeroes = []  # for storing co-ordinates of 0s
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                zeroes.append((i, j))  # SC = O(m*n)
    # print(zeroes)  #debugging

    for i, j in zeroes:  # problem: if whole matrix is 0, then this loop will run O(m*n) times, and so total TC will ⬆ to O(m*n*(m+n))
        # making rows 0:
        for index in range(n):
            matrix[i][index] = 0
        # making columns 0:
        for index in range(m):
            matrix[index][j] = 0
    """

    # 1) Temporarily changing the values to a placeholder value: TC = O(m*n*(m+n)); SC = O(1)

    """
    m, n = len(matrix), len(matrix[0])  # getting no. of rows & columns

    for i in range(m):  # O(m)
        for j in range(n):  # O(n)
            if matrix[i][j] == 0:
                # making rows 0:
                for k in range(n):  # O(n)
                    if matrix[i][k] != 0:  # because if we'll change it to None then it (and so it's column) will be skipped in future iterations
                        matrix[i][k] = None
                # making columns 0:
                for k in range(m):  # O(m)
                    if matrix[k][j] != 0:  # because if we'll change it to None then it (and so it's row) will be skipped in future iterations
                        matrix[k][j] = None

    # after above iterations, the matrix will be solution ready just with None values in place of 0s, changing the None values back to 0:
    for i in range(m):
        for j in range(n):
            if matrix[i][j] is None:
                matrix[i][j] = 0
    """

    # 2) Using Sets: TC = O(m*n); SC = O(m+n)

    """
    m, n = len(matrix), len(matrix[0])  # getting no. of rows & columns

    rows, columns = set(), set()  # for storing distinct row & column indices containing 0
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                rows.add(i)
                columns.add(j)  # SC = O(m+n)
    # print(rows, columns)  #debugging

    for i in range(m):
        for j in range(n):
            if i in rows or j in columns:  # O(1)
                matrix[i][j] = 0
    """

    # 3) Smart 👌: TC = O(m*n); SC = O(1)

    m, n = len(matrix), len(matrix[0])  # getting no. of rows & columns

    first_row_zero, first_column_zero = 0 in matrix[0], 0 in [row[0] for row in matrix]
    # saving whether the first row and column contain any 0s or not, this is the main trick in this algo (which allows solution in O(1) space):
    # what we're doing here is saving whether the rows/columns need to be set to 0s in the first row and column of the matrix,
    # to be more accurate, first cell of every row/column which needs to be set to 0, AND the same mark of first row and
    # column will be saved in two constant space vars, resulting in O(1) SC!!

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0  # first row cell to 0
                matrix[0][j] = 0  # first column cell to 0

    # setting rows and columns to 0:
    for i in range(1, m):  # imp: skipping 1st row and column (next line), do you know why? :D (will destroy what we saved in the first row and column)
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
