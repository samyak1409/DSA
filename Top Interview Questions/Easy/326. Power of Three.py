"""
https://leetcode.com/problems/power-of-three/
"""


def isPowerOfThree(n: int) -> bool:

    from math import log

    # 1) Using Log (Problematic):

    """
    if n < 1:  # non-positive integers
        return False

    x = log(n, 3)

    diff = abs(x-round(x))
    print(x, round(x), diff)  # debug

    # return diff == 0  # https://leetcode.com/problems/power-of-three/solution/#:~:text=Common%20pitfalls

    from sys import float_info
    print(float_info.epsilon, diff-float_info.epsilon)  # debug

    return diff-float_info.epsilon <= 0
    """

    # 3) Log and Power 👌 (Solves the problem of Method 1): TC = O(?); SC = O(?)

    """
    if n < 1:
        return False

    x = round(log(n, 3))
    print(x)  # debug

    return 3**x == n
    """

    # 2) Divide Loop: TC = O(log3 (n)); SC = O(1)

    while n > 1:
        n /= 3

    return n == 1
