"""
https://leetcode.com/problems/sqrtx/
"""


def mySqrt(x: int) -> int:
    """Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5."""

    # NOTE: Python doesn't bound integer limit, otherwise will have to use i < x/i instead of i*i < x for comparisons, to avoid exceeding integer upper limit.

    # 1) Brute Force: TC = O(√x); SC = O(1)

    """
    sqrt = 0

    while sqrt*sqrt < x:
        sqrt += 1

    return sqrt if (sqrt*sqrt == x) else sqrt-1
    """

    # 2) Newton's Method (Harder and Slower than Binary Search): TC = O(log x); SC = O(1)
    # https://leetcode.com/problems/sqrtx/discuss/25057/3-4-short-lines-Integer-Newton-Every-Language
    # https://en.wikipedia.org/wiki/Integer_square_root#Algorithm_using_Newton's_method

    # 3) Binary Search (Iterative): TC = O(log x); SC = O(1)

    # https://leetcode.com/problems/sqrtx/discuss/25047/A-Binary-Search-Solution/24042:

    l, h = 0, x

    while l <= h:

        m = (l+h) // 2
        m_x_m = m * m

        if m_x_m == x:
            return m

        elif m_x_m < x:
            l = m+1

        else:  # m_x_m > x
            h = m-1

    return h
