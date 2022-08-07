"""
https://leetcode.com/problems/pascals-triangle-ii
"""


def get_row(row_index: int) -> list[int]:
    """"""

    # Explanations of all the solutions:
    # https://github.com/samyak1409/DSA/blob/main/01%29%20Arrays/002%29%20Pascal%27s%20Triangle%20.py

    # 0) Brute-force (Nested Loop): TC = O(n^2); SC = O(n)
    # Surprisingly: https://leetcode.com/submissions/detail/767581085

    """
    row = [1]  # init.
    for _ in range(row_index):
        row = [i+j for i, j in zip(row+[0], [0]+row)]
    return row
    """

    # 1) Better (Combinations): TC = O(n^2); SC = O(1)

    from math import comb

    for i in range(row_index+1):  # +1 coz index
        yield comb(row_index, i)

    # 2) Optimal (Pattern): TC = O(n); SC = O(1)
