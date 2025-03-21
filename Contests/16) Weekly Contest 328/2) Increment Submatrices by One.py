"""
https://leetcode.com/problems/increment-submatrices-by-one
"""


def range_add_queries(n: int, queries: list[list[int]]) -> list[list[int]]:
    """"""

    # 0) [TLE] Brute-force (One by one perform for each query): TC = O(q * n^2) {q == len(queries)}; SC = O(1)

    """
    # Init n x n matrix with all 0s:
    # mat = [[0]*n]*n  # wrong: deep copy is not formed
    mat = [[0]*n for _ in range(n)]

    # For each query:
    for r1, c1, r2, c2 in queries:  # O(q * n*n)
        # Perform ops:
        for r in range(r1, r2+1):  # O(n*n)
            for c in range(c1, c2+1):  # O(n)
                mat[r][c] += 1

    return mat
    """

    # Merge Intervals!?
    # No...
    # Then? 🤔

    # 1) Optimal (For each row: Range Caching!! 💘): TC = O(q*n + n*n) = O(n(q+n)); SC = O(1)
    # Imagine each row as a separate array. Instead of updating the whole sub-matrix together, we can use prefix sum to
    # update each row separately.
    # For each query, iterate over the rows i in the range [row1, row2] and add 1 to prefix sum S[i][col1], and subtract
    # 1 from S[i][col2+1].
    # After doing this operation for all the queries, update each row separately with S[i][j] = S[i][j] + S[i][j-1].
    # https://leetcode.com/problems/increment-submatrices-by-one/solutions/3052675/python3-sweep-line-range-addition-w-visualization-clean-concise
    # This (https://assets.leetcode.com/users/images/2db6189c-c45b-4246-b23b-3b679d40d82a_1673763280.9586592.jpeg)
    # technique is mind-blowing!!!!
    # Range Addition (https://leetcode.com/problems/range-addition) is a must-know!

    # Init n x n matrix with all 0s:
    # mat = [[0]*n]*n  # wrong: deep copy is not formed
    mat = [[0]*n for _ in range(n)]

    # For each query:
    for r1, c1, r2, c2 in queries:  # O(q*n)
        # Range Caching:
        for r in range(r1, r2+1):  # O(n)
            mat[r][c1] += 1  # start
            try:  # EAFP
                mat[r][c2+1] -= 1  # end+1
            except IndexError:
                pass

    # Prefix Sum:
    for r in range(n):  # O(n*n)
        for c in range(1, n):  # O(n)
            mat[r][c] += mat[r][c-1]

    return mat

    # Easy af 😐

    # Is this Sweep Line Algorithm (https://en.wikipedia.org/wiki/Sweep_line_algorithm) ?
