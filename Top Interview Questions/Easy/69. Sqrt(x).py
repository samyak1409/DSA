"""
https://leetcode.com/problems/sqrtx/
"""


def mySqrt(x: int) -> int:

    # Brute Force: TC = O(n^.5); SC = O(1)

    """
    sqrt_int = 0
    num = 0

    while num**2 <= x:
        sqrt_int = num
        num += 1

    return sqrt_int
    """

    # https://en.wikipedia.org/wiki/Integer_square_root#Algorithm_using_Newton's_method: TC = O(?); SC = O(1)

    """
    r = x
    while r**2 > x:
        r = (r + x//r) // 2
    return r
    """

    # Iterative Binary Search: TC = O(log n); SC = O(1)

    l, h = 1, x
    not_found, m = False, 0

    while l <= h:

        not_found = False
        m = (l+h) // 2
        sq = m ** 2
        if sq == x:
            return m
        elif sq < x:
            l = m + 1
        else:  # sq > x
            h = m - 1
            not_found = True  # if loop end with not_found = True; m = m-1

    return m - int(not_found)
