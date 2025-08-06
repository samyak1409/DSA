"""
https://leetcode.com/problems/smallest-number-with-all-set-bits
"""


def smallest_number(n: int) -> int:
    """"""

    # 1) Optimal: TC = O(log2(n)); SC = O(1)

    # Intuition:
    # A num with all set bits is basically `2^p - 1`, where p >= 1. So, we just need to find the smallest `2^p - 1`
    # greater than or equal to `n`.

    # 1.1) Finding iteratively using while loop:

    """
    p = 1
    while (ans := 2**p - 1) < n:
        p += 1
    return ans
    """

    # 1.2) Finding directly using log2:

    """
    from math import log2

    '''
    return 2**ceil(log2(n)) - 1
    '''
    # At first, this might look correct, but for n = powers of 2, e.g. n = 8,
    # 2**ceil(log2(8)) - 1 = 2**ceil(3) - 1 = 2**3 - 1 = 8-1 = 7,
    # which clearly becomes less than actual `n`. But we wanted "greater than or equal to".
    # So, instead we don't want ceil, we want floor+1, so int+1:
    return 2**(int(log2(n))+1) - 1
    """

    # 1.3) Finding directly by getting len of bin repr (num of bits) of `n`:
    # https://leetcode.com/problems/smallest-number-with-all-set-bits/solutions/6102920/find-the-smallest-number-with-only-set-bits:

    """
    return 2**len(bin(n)[2:]) - 1  # (SC = O(log2(n)))
    """

    # Better: Using `bit_length` and `<<` (left shift):

    return (1 << n.bit_length()) - 1
