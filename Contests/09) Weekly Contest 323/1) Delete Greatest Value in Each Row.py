"""
https://leetcode.com/problems/delete-greatest-value-in-each-row
"""


def delete_greatest_value(grid: list[list[int]]) -> int:
    """"""

    # Iterate from the first to the last row and if there exist some unmarked cells, take a maximum from them and mark
    # that cell as visited.
    # Add a maximum of newly marked cells to answer and repeat that operation until the whole matrix becomes marked.

    # 0) Brute-force (Remove max linearly): TC = O(n * m*n); SC = O(1)

    """
    ans = 0
    while grid and grid[0]:  # "Perform the following operation until `grid` becomes empty:"; O(n * m*n)
        max_deleted = 0
        for row in grid:  # O(m*n)
            row.remove(maxi := max(row))  # "Delete the element with the greatest value from each row."; O(n)
            max_deleted = max(max_deleted, maxi)  # tracking max_deleted
        ans += max_deleted  # "Add the maximum of deleted elements to the answer."
    return ans
    """

    # 1) Optimal (Sort the rows in order to get the max in O(1)): TC = O(m * n*log(n)); SC = O(m*n)
    # https://leetcode.com/problems/delete-greatest-value-in-each-row/solutions/2899397/python-c-sort-rows-then-sum-max-of-cols-bonus-one-liner

    """
    # Sort:
    for row in grid:  # O(m * n*log(n))
        row.sort()  # O(n*log(n))
    # Remove & Track Max:
    ans = 0
    for _ in range(len(grid[0])):  # O(n*m)
        max_deleted = 0
        for row in grid:  # O(m)
            max_deleted = max(max_deleted, row.pop())  # "Delete the element with the greatest value from each row.";
            # tracking max_deleted
        ans += max_deleted  # "Add the maximum of deleted elements to the answer."
    return ans
    """

    # We don't really need to remove the elements, we just need to calc. to ans.
    # From future (Contests/41) Biweekly Contest 104/2) 2679. Sum in a Matrix.py):
    # 1) Optimal (Sort, Get Max, Sum): TC = O(m * n*log(n)); SC = O(m*n) {m = rows; n = columns}

    # Sort:
    '''
    for row in grid:
        row.sort()
    '''
    grid = [sorted(row) for row in grid]  # this way, input is not modified

    '''
    ans = 0
    for i in range(len(grid[0])):
        ans += max(row[i] for row in grid)
    return ans
    '''
    # One liner:
    return sum(max(row[i] for row in grid) for i in range(len(grid[0])))
