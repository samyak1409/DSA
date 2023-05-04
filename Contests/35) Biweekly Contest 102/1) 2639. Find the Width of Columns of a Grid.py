"""
https://leetcode.com/problems/find-the-width-of-columns-of-a-grid
"""


def find_column_width(grid: list[list[int]]) -> list[int]:
    """"""

    # You can find the length of a number by dividing it by 10 and then rounding it down again and again until this
    # number becomes equal to 0. Add 1 if this number is negative.
    # Traverse the matrix column-wise to find the maximum length in each column.

    # 1) Optimal (Column-wise Traversal): TC = O(m*n); SC = O(1)

    for j in range(len(grid[0])):

        col_max = 0

        for i in range(len(grid)):
            col_max = max(col_max, len(str(grid[i][j])))

        yield col_max

    # If you're feeling lil-adventurous:
    # https://leetcode.com/problems/find-the-width-of-columns-of-a-grid/solutions/3419979/python-1-liner-solution
