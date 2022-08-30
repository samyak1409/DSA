"""
https://leetcode.com/problems/pascals-triangle-ii
"""


def get_row(row_index: int) -> list[int]:
    """"""

    # Explanations of all the solutions:
    # https://github.com/samyak1409/DSA/blob/main/01%29%20Arrays/002%29%20Pascal%27s%20Triangle.py

    # Follow up: Could you optimize your algorithm to use only O(rowIndex) extra space?
    # 0) Brute-force (Nested Loop): TC = O(n^2); SC = O(n)

    """
    from itertools import chain

    row = [1]  # init
    for _ in range(row_index):
        row = [i+j for i, j in zip(chain(row, [0]), chain([0], row))]
    return row
    """

    # 1) Better (Combinations): TC = O(n^2); SC = O(1)

    """
    from math import comb

    for i in range(row_index+1):  # +1 coz index
        yield comb(row_index, i)
    """

    # 2) Optimal (Benefiting Combinations' Pattern): TC = O(n); SC = O(1)

    value = 1  # init
    yield value
    for i in range(row_index):
        value = (value*(row_index-i)) // (i+1)
        yield value


# Similar Questions: https://leetcode.com/problems/find-triangular-sum-of-an-array
