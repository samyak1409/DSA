"""
https://leetcode.com/problems/first-completely-painted-row-or-column
"""


def first_complete_index(arr: list[int], mat: list[list[int]]) -> int:
    """"""

    # Can we use a frequency array?
    # Pre-process the positions of the values in the matrix.
    # Traverse the array and increment the corresponding row and column frequency using the pre-processed positions.
    # If the row frequency becomes equal to the number of columns, or vice-versa return the current index.

    # 1) Optimal (HashMap): TC = O(m*n); SC = O(m*n)

    # Preprocessing:
    m, n = len(mat), len(mat[0])
    hm = {}  # to get the position of the numbers in the matrix
    for i in range(m):
        for j in range(n):
            hm[mat[i][j]] = (i, j)  # key: num; value: co-ordinates

    # Main:
    row_freq, col_freq = [0] * m, [0] * n  # `row_freq[i]` = number of elements painted in i-th row
    for ind, num in enumerate(arr):
        i, j = hm[num]
        row_freq[i], col_freq[j] = row_freq[i]+1, col_freq[j]+1
        if row_freq[i] == n or col_freq[j] == m:  # imp: no. of elements in a row = column_count, and vice versa
            # (had penalty in the contest here)
            return ind

    # If asked any other way to solve this:
    # 2) Optimal (HashMap): TC = O(m*n); SC = O(m*n)
    # https://leetcode.com/problems/first-completely-painted-row-or-column/solutions/3469270/c-dry-run-single-map
    # https://leetcode.com/problems/first-completely-painted-row-or-column/solutions/3468668/c-using-only-single-map-explained-easy-to-understand
