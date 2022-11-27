"""
https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column
"""


def ones_minus_zeros(grid: list[list[int]]) -> list[list[int]]:
    """"""

    # 1) Optimal (Save counts to an array and reuse in calculations): TC = O(m*n); SC = O(m+n)
    # You need to reuse information about a row or a column many times. Try storing it to avoid computing it multiple
    # times.
    # Use an array to store the number of 1’s in each row and another array to store the number of 1’s in each column.
    # Once you know the number of 1’s in each row or column, you can also easily calculate the number of 0’s.

    m, n = len(grid), len(grid[0])

    # Count Ones: TC = O(m*n)
    ones_cnt_in_row, ones_cnt_in_col = [0]*m, [0]*n  # init; SC = O(m+n)
    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            ones_cnt_in_row[i] += val
            ones_cnt_in_col[j] += val
    # print(ones_cnt_in_row, ones_cnt_in_col)  #debugging

    # Calc. diff: TC = O(m*n)
    # diff = [[0 for _ in range(n)] for _ in range(m)]  # correct but can be shorter
    # diff = [[0]*n]*m  # shortest but when the list is multiplied, it's not deep-copied, resulting in WA
    diff = [[0]*n for _ in range(m)]  # combination of both, correct and shortest
    # Conclusion: Prefer using List Comprehension over `*` Operator to be safe.
    for i in range(m):
        for j in range(n):
            # diff[i][j] = ones_cnt_in_row[i] + ones_cnt_in_col[j] - (n-ones_cnt_in_row[i]) - (m-ones_cnt_in_col[j])
            diff[i][j] = 2*(ones_cnt_in_row[i]+ones_cnt_in_col[j]) - (n+m)
    return diff
