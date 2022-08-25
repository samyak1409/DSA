"""
https://leetcode.com/problems/powx-n
"""


def my_pow(x: float, n: int) -> float:
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

    # 0) [TLE] Brute-force (Using Loop): TC = O(n); SC = O(1)

    """
    if n < 0:  # n can also be negative, making positive in order to proceed with the algo
        x, n = 1/x, -n  # (x ^ -n = (x^-1) ^ n = 1/x ^ n = 1/x * 1/x * 1/x ... n times)

    ans = 1
    for _ in range(n):
        ans *= x  # (x ^ n = x * x * x ... n times)
    return ans
    """

    # 1.1) Optimal (By me; correct logic but bad implementation) (Using Power Property): TC = O(log(n)); SC = O(1)
    # Property: x^(2y) = (x^y)^2
    # So e.g. if n = 4, we won't calc. x * x * x * x, but
    # 1) product = x * x
    # 2) ans = product * product
    # Great! No. of operations reduced from n to log(n).
    # e.g. if n = 4294967296 (2^32); log(n) = 32 only!

    """
    if n == 0:  # edge case
        return 1

    if n < 0:  # n can also be negative, making positive in order to proceed with the algo
        x, n = 1/x, -n  # (x ^ -n = x^-1 ^ n = 1/x ^ n)

    if n == 1:  # min power required for this algo = 2
        return x

    ans = 1
    power_left, product, current_terms = n, x, 1  # init
    while power_left >= 2:  # min power required for this algo = 2
        if power_left >= 2*current_terms:
            product *= product  # applying the property x^(2y) = (x^y)^2
            current_terms *= 2  # double
            power_left = n-current_terms  # update power_left
        else:  # e.g. if n = 23, after current_terms = 8, power_left = 15, next, 2*current_terms = 16 which is less than
            # power_left, but we can observe that power_left (15) is very close to n (23) which seems like we have not
            # much benefited from this method, so, we'll not jump on to linear multiplication but re-apply the method on
            # 15!
            ans *= product  # saving product calculated till here
            n, product, current_terms = power_left, x, 1  # reset
    ans *= product  # product of last iteration
    if power_left == 1:
        ans *= x  # e.g. if n = 3; above loop will run only 1 time and power_left = 1
    return ans
    """

    # 1.2) Optimal (Exponentiation by Squaring) (Same logic as mine, but well implemented):
    # Also known as Square-and-Multiply Algorithm or Binary Exponentiation
    # https://en.wikipedia.org/wiki/Exponentiation_by_squaring

    # 1.2.1) Iterative:  TC = O(log(n)); SC = O(1)
    # https://leetcode.com/problems/powx-n/discuss/19560/Shortest-Python-Guaranteed

    """
    if n < 0:  # handling negative power
        x, n = 1/x, -n  # update values

    ans = 1
    while n != 0:
        if n % 2 == 0:  # power even
            x *= x  # square
            n //= 2
        else:  # power odd
            ans *= x  # multiply
            n -= 1
            x *= x  # square
            n //= 2
    return ans
    """
    # In short:
    """
    if n < 0:  # handling negative power
        x, n = 1/x, -n  # update values

    ans = 1
    while n:
        if n & 1:  # if n % 2 == 1
            ans *= x  # multiply
            n -= 1
        x *= x  # square
        n >>= 1  # n //= 2
    return ans
    """

    # 1.2.2) Recursive (Easiest):  TC = O(log(n)); SC = O(log(n))
    # https://leetcode.com/problems/powx-n/discuss/19546/Short-and-easy-to-understand-solution
    # https://en.wikipedia.org/wiki/Exponentiation_by_squaring#Recursive_version
    # The method is based on the observation that, for a positive integer n, one has
    #         (x^2) ^ (n/2), if n is even
    # x ^ n =
    #         x * {(x^2) ^ [(n-1)/2]}, if n is odd
    # (https://wikimedia.org/api/rest_v1/media/math/render/svg/46fe9e68c70c04df4c3d22c469a57d4655b50539)

    if n < 0:  # handling negative power
        x, n = 1/x, -n  # update values

    if n == 0:  # base case
        return 1  # recurse out

    return my_pow(x*x, n//2) if (n % 2 == 0) else x*my_pow(x*x, (n-1)//2)  # recurse in
    # note: change `my_pow` above to `self.my_pow` for running inside class


# Similar Question: https://leetcode.com/problems/super-pow
