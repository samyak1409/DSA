"""
https://leetcode.com/problems/sum-of-matrix-after-queries
"""


def matrix_sum_queries(n: int, queries: list[list[int]]) -> int:
    """"""

    # 1) Optimal (Reverse Traverse, HashSet): TC = O(len(queries)); SC = O(2n) = O(n) {n = no. of rows = no. of cols}
    # Good & Easy Q.!
    # Observation 1: New operation overwrites any previous values.
    #   => We need to reverse traverse the queries, and sum up the values.
    # Observation 2: Initially, the matrix is filled with 0s.
    #   => We'd get our answer by traversing on the queries only. (We do not need to worry about matrix indices which
    #   are not covered by traversing the queries only.)
    # Observation 3: While reverse traversing the queries, if a row query is there, all the following column queries
    # would've only `n-1` values instead of `n`.
    #   => We need to track no. of row & col queries along the way in order to calc. correct sum.
    # Observation 4: Edge case: If while reverse traversing, any row query comes with the same row num, then it needs
    # to be ignored completely, because a future query with same op and row/col num has already overwritten it.
    #   => We just need to track that in a hashset.

    ans = 0
    r = c = 0  # count how many row/col ops has been performed till now
    hs = set()  # hash op with row/col index

    # Reverse traverse:
    for i in range(len(queries)-1, -1, -1):
        q = queries[i]
        # (`tuple` because mutable types like `list` are non-hashable)
        # Process the query only if not already took place:
        if (t := tuple(q[:2])) not in hs:
            # Save query to hashset:
            hs.add(t)
            # Update the sum:
            ans += q[2] * (n - (r if q[0] else c))
            # Update query row/col counts:
            if q[0]:
                c += 1
            else:
                r += 1

    return ans
