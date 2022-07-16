"""
https://leetcode.com/problems/powx-n
"""


def myPow(x: float, n: int) -> float:
    """"""

    # -1) Not Allowed (Using operator or built-in function): TC = O(log(n)); SC = O(1)
    # Though give following a read:
    # https://stackoverflow.com/questions/48839772/why-is-time-complexity-o1-for-powx-y-while-it-is-on-for-xy
    # https://stackoverflow.com/questions/1019740/speed-of-calculating-powers-in-python

    # https://docs.python.org/3/library/functions.html#pow:
    """
    return x ** n
    """
    # https://docs.python.org/3/library/math.html#math.pow:
    """
    import math
    return math.pow(x, n)
    """

    # 0) Brute-force (Using Loop) (TLE): TC = O(n); SC = O(1)

    """
    ans = 1
    if n > 0:
        for _ in range(n):
            ans *= x
    elif n < 0:
        for _ in range(-n):
            ans /= x
    return ans
    """

    # 1) 
