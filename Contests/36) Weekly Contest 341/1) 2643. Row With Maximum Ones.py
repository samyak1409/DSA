"""
https://leetcode.com/problems/row-with-maximum-ones
"""


def row_and_maximum_ones(mat: list[list[int]]) -> list[int]:
    """"""

    # 1) Optimal (Iterate & Count): TC = O(m*n); SC = O(1)
    # Iterate through each row and keep the count of ones.

    idx = mx = 0
    for i, row in enumerate(mat):
        if (c := row.count(1)) > mx:
            idx, mx = i, c
    return [idx, mx]
