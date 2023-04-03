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

    # 1.1) Better (Finding the Target Row + Linear Search): TC = O(m+n); SC = O(1)

    """
    for row in matrix:
        if row[-1] >= target:  # if last element of any row >= target => the target must be in this particular row only!
            return target in row
    return False  # if target is not found above (only when target > matrix[-1][-1])
    """

    # 1.2)
    # https://leetcode.com/problems/search-a-2d-matrix/discuss/1895837/C++-BINARY-SEARCH-TREE-(**)-Explained-with-IMG
    # Looks cool but, TC = O(m+n); SC = O(1), so doesn't make sense to use over simple `1.1)`.

    # 2) Optimal (Binary Search on whole Matrix): TC = O(log(m*n)); SC = O(1)
    # https://en.wikipedia.org/wiki/Binary_search_algorithm#Procedure

    m, n = len(matrix), len(matrix[0])
    lo, hi = 0, m*n - 1
    while lo <= hi:
        mid = (lo+hi) // 2
        row, col = divmod(mid, n)  # mid // n, mid % n
        integer = matrix[row][col]  # easy
        if integer == target:
            return True
        elif integer < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return False

    # 2.1) Alternatively we can also do Binary Search to find the Target Row, then Binary Search to find the Target,
    # which is basically the same thing as above and so the complexity of the algo is the same too.
    # TC = O(log(m)+log(n)) = O(log(m*n)); SC = O(1)
    # Benefit?:
    # "m * n may overflow for large m and n. I think it is better to binary search by row first, then binary search by
    # column. The time complexity is the same but this avoids multiplication overflow."
    # -https://leetcode.com/problems/search-a-2d-matrix/discuss/26220/Don't-treat-it-as-a-2D-matrix-just-treat-it-as-a-sorted-list/comments/25272


# Similar Questions:
# https://leetcode.com/problems/search-a-2d-matrix-ii
