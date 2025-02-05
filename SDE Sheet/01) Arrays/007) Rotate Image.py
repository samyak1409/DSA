"""
https://leetcode.com/problems/rotate-image
"""


def rotate(matrix: list[list[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """

    # "You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
    # DO NOT allocate another 2D matrix and do the rotation."

    # -1) Not Allowed (Using Matrix Copy): TC = O(n^2); SC = O(n^2)

    """
    from copy import deepcopy

    n = len(matrix)
    matrix_copy = deepcopy(matrix)  # you should know what deepcopy is for
    for i in range(n):
        for j in range(n):
            matrix[j][~i] = matrix_copy[i][j]  # (~i = -i-1)
    """

    # 1) Optimal: TC = O(n^2); SC = O(1)

    # 1.1) Rotate Groups of Four Cells:
    # Intuition: Observe how the cells move in groups when we rotate the image.
    # https://leetcode.com/problems/rotate-image/solution/#approach-1-rotate-groups-of-four-cells

    # 1.2) Transpose & Mirror (Y-axis):
    # The most elegant solution for rotating the matrix is to firstly reverse the matrix around the main
    # diagonal, and then reverse it from left to right. These operations are called transpose and reflect in linear
    # algebra.
    # Intuition: We can observe that, the first row of the output matrix is just the reverse of the first column of
    # input matrix, and so on.
    # https://leetcode.com/problems/rotate-image/solution/#approach-2-reverse-on-diagonal-and-then-reverse-left-to-right
    # https://leetcode.com/problems/rotate-image/discuss/18872/A-common-method-to-rotate-the-image

    """
    n = len(matrix)
    # Transposing:
    for i in range(n):  # O(n^2)
        for j in range(i+1, n):  # imp: `i+1`
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # Mirroring on Y-axis:
    for i in range(n):  # O(n^2)
        matrix[i].reverse()
    """

    # OR Mirror (X-axis) & Transpose:

    n = len(matrix)
    # Mirroring on X-axis: O(n^2)
    matrix.reverse()
    # Transposing:
    for i in range(n):  # O(n^2)
        for j in range(i+1, n):  # imp: `i+1`
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Even though this approach does twice as many reads and writes as approach 1, most people would consider it a
    # better approach because the code is simpler, and it is built with standard matrix operations that can be found in
    # any matrix library.

    # Interesting Implementations of this Approach:
    # https://leetcode.com/problems/rotate-image/discuss/18884/Seven-Short-Solutions-(1-to-7-lines)

    # Bonus Question: What would happen if you reflect and then transpose? Would you still get the correct answer?
    # Nope, it'll rotate -90° Clockwise = 90° Anti-Clockwise.

    # Rotations:
    # Transpose & Mirror (Y-axis) OR Mirror (X-axis) & Transpose: 90° Clockwise
    # Transpose & Mirror (X-axis) OR Mirror (Y-axis) & Transpose: 90° Anti-Clockwise
    # Mirror (X-axis) & Mirror (Y-axis) OR Mirror (Y-axis) & Mirror (X-axis): 180° Clockwise == 180° Anti-Clockwise


# Similar Questions:
# https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation
