"""
https://leetcode.com/problems/search-a-2d-matrix-ii
"""


def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    """"""

    # 0) Brute-force (Linear Search): TC = O(m*n); SC = O(1)

    for row in matrix:
        if target in row:
            return True
    return False  # if target is not found above
