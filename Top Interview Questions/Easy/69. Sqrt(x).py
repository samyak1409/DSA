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

    low = 0  # Because 0 is sqrt of the smallest possible non-negative integer, i.e. 0. {sqrt(min(x)) = sqrt(0) = 0}
    high = x  # Because sqrt(x) will always be lesser than or equal to x. {sqrt(x) <= x for any non-negative integer x}

    # Now Standard Binary Search:

    while low <= high:

        mid = (low+high) // 2
        mid_sq = mid * mid

        if mid_sq == x:  # sqrt found; if mid_sq = x => mid = sqrt(x)
            return mid

        elif mid_sq < x:  # => mid is < sqrt(x)
            low = mid+1

        else:  # (mid_sq > x) => mid is > sqrt(x)
            high = mid-1

    return high  # if mid is not returned above, => x is not a perfect square => sqrt(x) = floating point number, so returning the floor integer value
