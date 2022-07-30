"""
https://leetcode.com/problems/rotate-image
"""


def rotate(matrix: list[list[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """

    # 0) Brute-force (Using matrix copy): TC = O(n^2); SC = O(n^2)

    """
    from copy import deepcopy

    n = len(matrix)
    matrix_copy = deepcopy(matrix)  # you should know what deepcopy is for 😁
    for i in range(n):
        for j in range(n):
            matrix[j][-i-1] = matrix_copy[i][j]
    """

    # 1) Optimal (Transpose & Mirror (Y-axis)): TC = O(n^2); SC = O(1)
    # Intuition: We can observe that, the first row of the output matrix is just the reverse of the first column of
    # input matrix, and so on.

    n = len(matrix)
    # Transposing:
    for i in range(n):  # O(n^2)
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # Mirroring on Y-axis:
    for i in range(n):  # O(n^2)
        matrix[i].reverse()
