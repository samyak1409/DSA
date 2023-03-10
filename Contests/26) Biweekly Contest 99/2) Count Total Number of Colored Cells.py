"""
https://leetcode.com/problems/count-total-number-of-colored-cells
"""


def colored_cells(n: int) -> int:
    """"""

    # 1) Optimal (Recognize the Pattern 1, 5, 13, 25...): TC = O(1); SC = O(1)
    # https://en.wikipedia.org/wiki/Centered_square_number
    # (n-1)^2 + n^2

    return (n-1)**2 + n**2
