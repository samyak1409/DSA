"""
https://leetcode.com/problems/number-of-even-and-odd-bits
"""


def even_odd_bit(n: int) -> list[int]:
    """"""

    # Maintain two integer variables, even and odd, to count the number of even and odd indices in the binary
    # representation of integer n.

    # 1) Time-Optimal (To binary str, & Iterate): TC = O(log2(n)); SC = O(log2(n))

    """
    even_odd = [0, 0]
    for index, value in enumerate(bin(n)[2:][::-1]):
        if int(value):  # value will be either '0' or '1'
            even_odd[index & 1] += 1  # (`index & 1` == index % 2)
    return even_odd
    """

    # 2) Optimal: TC = O(log2(n)); SC = O(1)

    # Divide n by 2 while n is positive, and if n modulo 2 is 1, add 1 to its corresponding variable.

    # 2.1) Iterate & Keep removing the LSB:

    """
    even_odd = [0, 0]
    index = 0
    while n:  # while n is not 0
        if n & 1:  # (if n % 2); if LSB of n is 1
            even_odd[index] += 1
        n >>= 1  # (n //= 2); remove LSB
        index = 1-index  # 0 -> 1, 1 -> 0; update index
    return even_odd
    """

    # 2.2) Bitmask (https://en.wikipedia.org/wiki/Mask_(computing)) & Count:
    # https://leetcode.com/problems/number-of-even-and-odd-bits/solutions/3314042/one-liner

    return [(n & 0b0101010101).bit_count(), (n & 0b1010101010).bit_count()]
    # "1 <= n <= 1000", round(log2(max(n))) == 10
