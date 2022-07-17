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

    # 0) (TLE) Brute-force (Using Loop): TC = O(n); SC = O(1)

    """
    if n < 0:  # n can also be negative, making positive in order to proceed with the algo
        # (x ^ -n = x^-1 ^ n = 1/x ^ n = 1/x * 1/x * 1/x ... n times)
        x = 1 / x
        n *= -1

    ans = 1
    for _ in range(n):
        ans *= x  # (x ^ n = x * x * x ... n times)
    return ans
    """

    # 1) Optimal (Using Power Property): TC = O(log(n)); SC = O(1)
    # Property: x^(2y) = (x^y)^2
    # So e.g. if n = 4, we won't calc. x * x * x * x, but
    # 1) product = x * x
    # 2) ans = product * product
    # Great! No. of operations reduced from n to log(n).

    if n == 0:  # edge case
        return 1

    if n < 0:  # n can also be negative, making positive in order to proceed with the algo
        # (x ^ -n = x^-1 ^ n = 1/x ^ n)
        x = 1 / x
        n *= -1

    if n == 1:  # min power required for this algo = 2
        return x

    ans = 1
    power_left, product, current_terms = n, x, 1  # initialization
    while power_left >= 2:  # min power required for this algo = 2
        if power_left >= 2*current_terms:
            product *= product  # applying the property x^(2y) = (x^y)^2
            current_terms *= 2  # double
            power_left = n-current_terms  # update power_left
        else:  # e.g. if n = 23, after current_terms = 8, power_left = 15, next, 2*current_terms = 16 which is less than power_left,
            # but we can observe that power_left (15) is very close to n (23) which seems like we have not much benefited from this method,
            # so, we'll not jump on to linear multiplication but re-apply the method on 15!
            ans *= product  # saving product calculated till here
            n, product, current_terms = power_left, x, 1  # reset
    ans *= product  # product of last iteration
    if power_left == 1:
        ans *= x  # e.g. if n = 3; above loop will run only 1 time and power_left = 1
    return ans
