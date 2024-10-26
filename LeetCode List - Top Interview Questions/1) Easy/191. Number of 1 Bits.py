"""
https://leetcode.com/problems/number-of-1-bits
"""


def hamming_weight(n: int) -> int:
    """"""

    # 1) Time-optimal (To binary, and Counting 1s):
    # TC = O(log2(n)); SC = O(log2(n)) {log2(n): no. of binary bits in int `n`}

    """
    return bin(n).count('1')
    """

    # 2.1) Optimal (Bit Manipulation): TC = O(log2(n)); SC = O(1)

    """
    count = 0
    while n:  # O(log2(n))
        count += n & 1  # `n & 1`: get the LSB of n
        n >>= 1
    return count
    """

    # 2.2) Optimal (Bit Manipulation): TC = O(s); SC = O(1) {s: no. of set bits (1s) in `n`}
    # (Even faster than `2.1`.)
    # "n & (n-1) drops the lowest set bit. It's a neat little bit trick.
    # Let's use n = 00101100 as an example. This binary representation has three 1s.
    # If n = 00101100, then n-1 = 00101011, so n & (n-1) = 00101100 & 00101011 = 00101000. Count = 1.
    # If n = 00101000, then n-1 = 00100111, so n & (n-1) = 00101000 & 00100111 = 00100000. Count = 2.
    # If n = 00100000, then n-1 = 00011111, so n & (n-1) = 00100000 & 00011111 = 00000000. Count = 3.
    # n is now zero, so the while loop ends, and the final count (the numbers of set bits) is returned."
    # -https://leetcode.com/problems/number-of-1-bits/solutions/55255/c-solution-n-n-1
    # Also, dry run to understand why `n & (n-1)` drops the lowest set bit. [IMP.]

    count = 0
    while n:  # O(s)
        n &= n - 1  # drops lowest set bit; (once all the set bits are dropped, n becomes 0)
        count += 1
    return count
