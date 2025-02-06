"""
https://leetcode.com/problems/powx-n
"""


def my_pow(x: float, n: int) -> float:
    """"""

    # -1) Not Allowed (Operator / built-in function): TC = O(log(n)); SC = O(1)
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

    # 0) [TLE] Brute-force (Loop): TC = O(n); SC = O(1)

    """
    if n < 0:  # n can also be -ve, making +ve in order to proceed with the algo
        x, n = 1/x, -n  # (x ^ -n = (x^-1) ^ n = 1/x ^ n = 1/x * 1/x * 1/x ... n times)

    ans = 1
    for _ in range(n):
        ans *= x  # (x ^ n = x * x * x ... n times)
    return ans
    """

    # 0.1) [TLE] Brute-force (Power Property): TC = O(n); SC = O(1)
    # This approach has the same idea of optimal approach.
    # Problem in this approach: if n = 2^z - 1
    # e.g. n = 127, then till 64 exponentiation would be using squaring, but since 64*2 > 127, hence it'd then do a
    # linear exponentiation. So, since it'd do almost n/2 linear operations, it again falls back down to O(n) TC.
    # [See `1.2)` which fixes this problem effortlessly.]

    """
    if n < 0:  # handling -ve power
        x, n = 1/x, -n  # update values

    # Note that if x == 0, n > 0, as per the constraint, so we do not need to handle x == 0.
    # Handle the edge case n == 0:
    if n == 0:
        return 1

    # Init:
    pow_done = 1
    ans = x
    # While exponentiation isn't done:
    while pow_done != n:
        # If we can square:
        if pow_done * 2 <= n:
            ans *= ans
            pow_done *= 2
        # Else, complete rest linearly:
        else:
            for _ in range(n-pow_done):  # O(n)
                ans *= x
            break
    return ans
    """

    # 1.1) Optimal (Power Property): TC = O(log(n)); SC = O(1)
    # (By me; correct logic but bad implementation.)
    # Property: x^(2y) = (x^y)^2
    # So e.g. if n = 4, we won't calc. x * x * x * x, but
    # 1) product = x * x
    # 2) ans = product * product
    # Great! No. of operations reduced from n to log2(n).
    # e.g. if n = 4294967296 (2^32); log2(n) = 32 only!

    """
    if n == 0:  # edge case
        return 1

    if n < 0:  # n can also be -ve, making +ve in order to proceed with the algo
        x, n = 1/x, -n  # (x ^ -n = x^-1 ^ n = 1/x ^ n)

    if n == 1:  # min power required for this algo = 2
        return x

    ans = 1
    pow_left, prod, curr_terms = n, x, 1  # init
    while pow_left >= 2:  # min power required for this algo = 2
        if pow_left >= 2*curr_terms:
            prod *= prod  # applying the property x^(2y) = (x^y)^2
            curr_terms *= 2  # double
            pow_left = n-curr_terms  # update pow_left
        else:  # e.g. if n = 23, after curr_terms = 8, pow_left = 15, next, 2*curr_terms = 16 which is less than
            # pow_left, but we can observe that pow_left (15) is very close to n (23) which seems like we have not much
            # benefited from this method, so, we'll not jump on to linear multiplication but re-apply the method on 15!
            ans *= prod  # saving product calculated till here
            n, prod, curr_terms = pow_left, x, 1  # reset
    ans *= prod  # product of last iteration
    if pow_left == 1:
        ans *= x  # e.g. if n = 3; above loop will run only 1 time and pow_left = 1
    return ans
    """

    # 1.2) Optimal (Power Property): TC = O(log(n)); SC = O(1)
    # We can also actually convert `0.1)` to optimal by fixing the issue in it using recursion!

    """
    if n < 0:  # handling -ve power
        x, n = 1/x, -n  # update values

    # Note that if x == 0, n > 0, as per the constraint, so we do not need to handle x == 0.
    # If n == 0 (and let's x == 3), then also we do not need to handle it explicitly, dry run to know how.

    # Init:
    pow_done = 1
    ans = x
    # While exponentiation isn't done:
    while pow_done != n:
        # If we can square:
        if pow_done * 2 <= n:
            ans *= ans
            pow_done *= 2
        # Else, recall the func (recursion):
        else:
            return ans * my_pow(x=x, n=n-pow_done)
    return ans
    """

    # 1.3) Optimal (Exponentiation by Squaring) (Same logic as mine, but well implemented):
    # Also known as Square-and-Multiply Algorithm or Binary Exponentiation
    # https://en.wikipedia.org/wiki/Exponentiation_by_squaring

    # 1.3.1) Iterative: TC = O(log(n)); SC = O(1)
    # https://leetcode.com/problems/powx-n/discuss/19560/Shortest-Python-Guaranteed

    """
    if n < 0:  # handling -ve power
        x, n = 1/x, -n  # update values

    ans = 1
    while n != 0:
        if n % 2 == 0:  # power even
            x *= x  # square
            n //= 2
        else:  # power odd
            ans *= x  # multiply
            n -= 1
    return ans
    """
    # Or:
    """
    if n < 0:  # handling -ve power
        x, n = 1/x, -n  # update values

    ans = 1
    while n:
        if n % 2:
            ans *= x  # multiply
            n -= 1
        x *= x  # square
        n //= 1
    return ans
    """

    # 1.3.2) Recursive (Easiest): TC = O(log(n)); SC = O(log(n))
    # https://leetcode.com/problems/powx-n/discuss/19546/Short-and-easy-to-understand-solution
    # https://en.wikipedia.org/wiki/Exponentiation_by_squaring#Recursive_version
    # The method is based on the observation that, for a +ve int n, one has
    #         (x^2) ^ (n/2), if n is even
    # x ^ n =
    #         x * {(x^2) ^ [(n-1)/2]}, if n is odd
    # (https://wikimedia.org/api/rest_v1/media/math/render/svg/46fe9e68c70c04df4c3d22c469a57d4655b50539)

    if n < 0:  # handling -ve power
        x, n = 1/x, -n  # update values

    if n == 0:  # base case
        return 1  # recurse out

    return my_pow(x=x*x, n=n//2) if (n % 2 == 0) else x * my_pow(x=x*x, n=(n-1)//2)  # recurse in
    # note: change `my_pow` above to `self.my_pow` for running inside class


# Similar Questions:
# https://leetcode.com/problems/sqrtx
# https://leetcode.com/problems/super-pow
