"""
https://leetcode.com/problems/sqrtx
"""


def my_sqrt(x: int) -> int:
    """"""

    # Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.
    # -1) Not Allowed (Using Built-in Exponent Function or Operator): TC = O(log(x)); SC = O(1)

    """
    return int(x ** .5)
    """
    """
    return int(pow(x, .5))
    """
    """
    from math import pow
    return int(pow(x, .5))
    """
    """
    from math import sqrt
    return int(sqrt(x))
    """
    """
    from math import isqrt
    return isqrt(x)
    """

    # NOTE: Python doesn't bound integer limit, otherwise we would have to use i == x/i instead of i*i == x for
    # comparisons, to avoid exceeding integer upper limit.

    # 0) Brute Force (Linear Search): TC = O(√x); SC = O(1)
    # https://en.wikipedia.org/wiki/Integer_square_root#Algorithm_using_linear_search

    # 0.1) Intuitive:
    """
    for sqrt in range(0, x+1):  # ∵ for a non-negative integer x, range(sqrt(x)) = [0, x]
        sq = sqrt * sqrt
        if sq == x:
            return sqrt
        elif sq > x:  # for non-perfect square x
            return sqrt-1
    """
    # 0.2) Bit Faster (due to fewer comparisons):
    """
    sqrt = 0
    while sqrt*sqrt < x:
        sqrt += 1
    return sqrt if (sqrt*sqrt == x) else sqrt-1
    """

    # 1.1) Optimal (Binary Search): TC = O(log(x)); SC = O(1)
    # https://leetcode.com/problems/sqrtx/discuss/25047/A-Binary-Search-Solution/24042
    # https://en.wikipedia.org/wiki/Integer_square_root#Algorithm_using_binary_search

    lo, hi = 0, x  # ∵ for a non-negative integer x, range(sqrt(x)) = [0, x]
    while lo <= hi:
        mid = (lo+hi) // 2
        mid_sq = mid * mid
        if mid_sq == x:  # => mid = sqrt(x)
            return mid
        elif mid_sq < x:  # => mid < sqrt(x)
            lo = mid + 1  # update range
        else:  # (if mid_sq > x) => mid > sqrt(x)
            hi = mid - 1  # update range
    # If x is not a perfect square, ans. won't be returned above, and `lo` will become > than `hi`, and the loop will
    # terminate.
    # In these cases answer will be = `lo-1` = `hi`, because the loop terminated because of two possible cases:
    # Either:
    # `mid_sq < x` (=> mid < sqrt(x)), `lo = mid + 1` executed, and `lo` became > than `hi` => int(sqrt(x)) = lo-1 = hi
    # Or:
    # `mid_sq > x` (=> mid > sqrt(x)), `hi = mid - 1` executed, and `hi` became < than `lo` => int(sqrt(x)) = hi = lo-1
    return lo-1  # or hi

    # 1.2) Optimal (Heron's method, a special case of Newton's method): TC = O(log(x)); SC = O(1)
    # -> Harder and Slower than Binary Search
    # https://leetcode.com/problems/sqrtx/discuss/25057/3-4-short-lines-Integer-Newton-Every-Language
    # https://en.wikipedia.org/wiki/Integer_square_root#Algorithm_using_Newton%27s_method


# Remarks: sqrt(x) = √x = -√x i.e. sqrt(25) = 5 = -5
# But the OJ is not accepting -ve roots, that it should, because it's not mentioned anywhere to return +ve root only,
# it doesn't make any sense to return -ve root though, but still it's correct and so should be accepted.
# Update: https://github.com/LeetCode-Feedback/LeetCode-Feedback/issues/9473
