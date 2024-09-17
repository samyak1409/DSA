"""
https://leetcode.com/problems/sqrtx
"""


def my_sqrt(x: int) -> int:
    """"""

    # Note: You must not use any built-in exponent function or operator.

    # -1) Not Allowed (Built-in Exponent Function or Operator): TC = O(log(x)); SC = O(1)

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
    # comparisons, to avoid exceeding integer upper limit (in case of `sq(ceil(sqrt(2**31 - 1)))`).

    # 0) Brute Force (Linear Search): TC = O(√x); SC = O(1)
    # https://en.wikipedia.org/wiki/Integer_square_root#Algorithm_using_linear_search

    """
    for i in range(x+2):  # +1 ∵ for a non-negative int x, range(sqrt(x)) = [0, x]; 
    # another +1 ∵ we need to go one above the actual answer to know if it's the answer or not
        if i*i > x:
            return i-1
    """
    # Or we can just use:
    """
    from itertools import count

    for i in count():
        if i*i > x:
            return i-1
    """

    # 1.1) Optimal (Binary Search): TC = O(log2(x)); SC = O(1)
    # https://leetcode.com/problems/sqrtx/solutions/25047/a-binary-search-solution/comments/24042
    # https://en.wikipedia.org/wiki/Binary_search_algorithm#Procedure
    # https://en.wikipedia.org/wiki/Integer_square_root#Algorithm_using_binary_search

    lo, hi = 0, x  # ∵ for a non-negative int x, range(sqrt(x)) = [0, x]
    while lo <= hi:  # stop when lo > hi, to be accurate when lo = hi+1
        mid = (lo + hi) // 2
        mid_sq = mid * mid
        if mid_sq == x:  # => mid = sqrt(x)
            return mid
        elif mid_sq < x:  # => mid < sqrt(x)
            lo = mid + 1  # compress range
        else:  # (if mid_sq > x) => mid > sqrt(x)
            hi = mid - 1  # compress range
    # If x is not a perfect square, ans. won't be returned above, and `lo` will become > than `hi`, and the loop will
    # terminate.
    # In these cases answer will be = `lo-1` = `hi`, because the loop terminated because of two possible cases:
    # Either:
    # `mid_sq < x` (=> mid < sqrt(x)), `lo = mid + 1` executed, and `lo` became > than `hi` => int(sqrt(x)) = lo-1 = hi
    # Or:
    # `mid_sq > x` (=> mid > sqrt(x)), `hi = mid - 1` executed, and `hi` became < than `lo` => int(sqrt(x)) = hi = lo-1
    return lo - 1  # or hi

    # 1.2) Optimal (Heron's method, a special case of Newton's method): TC = O(log(x)); SC = O(1)
    # -> Harder and Slower than Binary Search
    # https://leetcode.com/problems/sqrtx/solutions/25057/3-4-short-lines-Integer-Newton-Every-Language
    # https://en.wikipedia.org/wiki/Integer_square_root#Algorithm_using_Newton%27s_method


# Remarks: sqrt(x) = √x = -√x i.e. sqrt(25) = 5 = -5
# But the OJ is not accepting -ve roots, that it should, because it's not mentioned anywhere to return +ve root only,
# it doesn't make any sense to return -ve root though, but still it's correct and so should be accepted.
# Update: https://github.com/LeetCode-Feedback/LeetCode-Feedback/issues/9473
