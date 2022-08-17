"""
https://leetcode.com/problems/search-a-2d-matrix
"""


def search_matrix(matrix: list[list[int]], target: int) -> bool:
    """"""

    # 0) Brute-force (Linear Search): TC = O(m*n); SC = O(1)

    """
    for row in matrix:
        if target in row:
            return True
    return False  # if target is not found above
    """

    # 1) Better (Finding the Target Row + Linear Search): TC = O(m+n); SC = O(1)

    """
    for row in matrix:
        if row[-1] >= target:  # if last element of any row >= target => the target must be in this particular row only!
            return target in row
    return False  # if target is not found above (only when target > matrix[-1][-1])
    """

    # 2) Optimal (Binary Search on whole Matrix): TC = O(log(m*n)); SC = O(1)
    # https://en.wikipedia.org/wiki/Binary_search_algorithm#Procedure

    m, n = len(matrix), len(matrix[0])
    low, high = 0, m*n - 1
    while low <= high:
        mid = (low+high) // 2
        row, col = divmod(mid, n)  # mid // n, mid % n
        integer = matrix[row][col]  # easy
        if integer == target:
            return True
        elif integer < target:
            low = mid + 1
        else:
            high = mid - 1
    return False


# Similar Question: https://leetcode.com/problems/search-a-2d-matrix-ii
