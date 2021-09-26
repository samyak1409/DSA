"""
https://leetcode.com/problems/reverse-integer/
"""


def reverse(x: int) -> int:

    # Method 1 (Generic):

    """
    sign = -1 if x < 0 else 1

    x = abs(x)
    rev = 0
    while x:
        rev = (rev * 10) + (x % 10)
        x //= 10

    return sign * rev if (-(2**31) <= rev <= (2**31)-1) else 0
    """

    # Method 2 (Pythonic):

    sign = [1, -1][x < 0]

    rev = int(str(abs(x))[::-1])

    return sign * rev if (-(2**31) <= rev <= (2**31)-1) else 0
