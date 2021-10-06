"""
https://leetcode.com/problems/reverse-bits/
"""


def reverseBits(n: int) -> int:

    # Explanation:
    """
    print(n)  # passed arg is of type binary but casted to decimal maybe because param type is int

    b_ = bin(n)[2:]  # deci -> bin and trimming that '0b' (that's used to identify binary nums in python)
    print(b_)

    b = b_.zfill(32)  # "32 bits unsigned integer"
    print(b)

    rb = b[::-1]  # reversing
    print(rb)

    return int(rb, base=2)  # bin -> deci
    """

    return int(bin(n)[2:].zfill(32)[::-1], base=2)
