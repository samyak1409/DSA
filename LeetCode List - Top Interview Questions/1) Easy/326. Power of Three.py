"""
https://leetcode.com/problems/power-of-three
"""


def is_power_of_three(n: int) -> bool:

    # 1) Simple Maths (Correct but Problematic in programming): TC = O(log3 (n)); SC = O(1)

    """
    if n <= 0:  # non-positive integers
        return False

    from math import log
    x = log(n, 3)
    return x == int(x)

    # Can give wrong answer because: https://leetcode.com/problems/power-of-three/solution/#:~:text=Common%20pitfalls
    """

    # 1.1) Log and Exponent (Power) 👌 (Solves the problem of method 1): TC = O(log3 (n)); SC = O(1)

    """
    if n <= 0:  # non-positive integers
        return False

    from math import log
    x = round(log(n, 3))  # round the value up
    return 3**x == n  # reverse check

    # How does it give correct answer:
    # case 1) precision error is there: rounding up will correct it, reverse check will return True
    # case 2) precision errors isn't there:
    #                                       case 2.1) value from 'log' is a decimal num: 'round' will convert it to int,
    #                                                                                    reverse check will return False
    #                                       case 2.2) value from 'log' is an int: reverse check will return True
    """

    # 2) Divide Loop: TC = O(log3 (n)); SC = O(1)

    """
    while n > 1:
        n /= 3

    return n == 1
    """

    # 3) Thug Life: TC = O(1); SC = O(1)

    # https://leetcode.com/problems/power-of-three/solution/#approach-4-integer-limitations
    # https://leetcode.com/problems/power-of-three/discuss/77977/Math-1-liner-no-log-with-explanation

    """
    from math import log, floor
    max_n = 2**31 - 1  # Q. constraint: (-2^31 <= n <= 2^31 - 1)
    max_pow_3 = 3 ** floor(log(max_n, 3))  # = 3 ** floor(19.558822360291316) = 3 ** 19 = 1162261467
    print(max_pow_3)  #debugging
    return (n > 0) and (max_pow_3 % n == 0)
    """

    return (n > 0) and (1162261467 % n == 0)

    # Also read: https://stackoverflow.com/questions/600293/how-to-check-if-a-number-is-a-power-of-2
