"""
https://leetcode.com/problems/power-of-three
"""


def is_power_of_three(n: int) -> bool:
    """"""

    # "An integer `n` is a power of three, if there exists an integer `x` such that `n == 3^x`."

    # 0) Brute-force (Log): TC = O(log3(n)); SC = O(1)
    # e.g. n = 81
    # x = log3(n) = 4.0
    # So, `n` would be a power of 3, if `x` is an INT.

    # 0.1) [WA] Direct Log:

    """
    from math import log

    if n <= 0:  # for any int `x`, `3^x` (i.e. `n`) can't be non-positive, so:
        return False

    x = log(n, 3)
    print(x)  # debugging
    
    return x == int(x)
    """

    # Gives wrong answer e.g. when n = 243, x comes out to be 4.999999999999999.
    # A consequence of the inherent limitations of floating-point arithmetic in computers.
    # https://leetcode.com/problems/power-of-three/editorial/#:~:text=Common%20pitfalls
    # https://stackoverflow.com/questions/588004/is-floating-point-math-broken

    # 0.2) Using Base Conversion:
    # https://bugs.python.org/msg403065

    """
    from math import log

    if n <= 0:
        return False

    x = log(n, 10) / log(3, 10)
    print(x)  # debugging

    return x == int(x)
    """
    # Weird stuff: Above (using `log`) doesn't work, below (using `log10`) works. :)
    """
    from math import log10

    if n <= 0:
        return False

    x = log10(n) / log10(3)
    print(x)  # debugging

    return x == int(x)
    """

    # 0.3) Using Log and Power: TC = O(log3(n)); SC = O(1)
    # How does it work:
    # case 1) precision error isn't there:
    #         case 1.1) value from `log` is int: reverse check will return True
    #         case 1.2) value from `log` isn't int: `round` will convert it to int, reverse check will return False
    # case 2) precision error is there: `round` will correct it, reverse check will return correct ans.

    """
    from math import log

    if n <= 0:
        return False

    x = round(log(n, 3))  # round the value up
    return 3**x == n  # reverse check
    """

    # 1) Brute-force (Loop): TC = O(log3(n)); SC = O(1)

    """
    while n > 1:
        n /= 3

    return n == 1
    """

    # Follow up: Could you solve it without loops/recursion?

    # 2) Optimal (Maths: Divisor): TC = O(1); SC = O(1)
    # "The positive divisors of 3^19 are exactly the powers of 3 from 3^0 to 3^19."
    # -https://leetcode.com/problems/power-of-three/solutions/77977/math-1-liner-no-log-with-explanation

    """
    from math import log, floor
    max_n = 2**31 - 1  # (`-2^31 <= n <= 2^31 - 1`)
    max_pow_3 = 3 ** floor(log(max_n, 3))  # = 3 ** floor(19.558822360291316) = 3 ** 19 = 1162261467
    print(max_pow_3)  # debugging
    return (n > 0) and (max_pow_3 % n == 0)
    """

    # We can also just hardcode:
    return (n > 0) and (1162261467 % n == 0)

    # Note - We can also solve this using Binary Search.


# Also read: https://stackoverflow.com/questions/600293/how-to-check-if-a-number-is-a-power-of-2
