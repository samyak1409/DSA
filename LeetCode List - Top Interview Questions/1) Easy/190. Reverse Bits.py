"""
https://leetcode.com/problems/reverse-bits
"""


def reverse_bits(n: int) -> int:
    """"""

    # 1) Time-optimal (Reversing the Binary String: Not supposed to be solved like this.): TC = O(32); SC = O(32)

    """
    print(n, type(n))  # 43261596 <class 'int'>
    # arg passed is actually int

    n = bin(n)  # deci -> bin
    print(n, type(n))  # 0b10100101000001111010011100 <class 'str'>

    n = n[2:]  # trim '0b' (denotes binary num in python)
    print(n)  # 10100101000001111010011100

    n = n.zfill(32)  # fill 0s to the left to make the str "32 bits"
    print(n)  # 00000010100101000001111010011100

    n = n[::-1]  # reverse
    print(n)  # 00111001011110000010100101000000

    n = int(n, base=2)  # bin -> deci
    print(n)  # 964176192

    return n
    """
    
    # One liner:
    """
    return int(bin(n)[2:].zfill(32)[::-1], base=2)  # deci -> bin, trim '0b', fill 0s, reverse, bin -> deci
    """

    # 2) Optimal (Bit Manipulation): TC = O(32); SC = O(1)
    # [EASY]
    # "We are asked to reverse bits in our number. What is the most logical way to do it?
    # Create number `out`, process original number bit by bit from end and add this bit to the end of our `out` number,
    # and that is all! Why it is works?
    #
    # out = (out << 1) | (n & 1) adds last bit of n to out
    # n >>= 1 removes last bit from n.
    #
    # Imagine number n = 11011010, and out = 0
    # out = 0, n = 1101101
    # out = 01, n = 110110
    # out = 010, n = 11011
    # out = 0101, n = 1101
    # out = 01011, n = 110
    # out = 010110, n = 11
    # out = 0101101, n = 1
    # out = 01011011, n = 0
    #
    # Complexity: time complexity is O(32), space complexity is O(1)."
    # -https://leetcode.com/problems/reverse-bits/solutions/732138/python-o-32-simple-solution-explained

    ans = 0
    for _ in range(32):  # because we want exactly 32 bits only
        ans = ans << 1 | n & 1  # bitwise (op is applied bit by bit)
        n >>= 1
        # `ans << 1`: getting the one left shifted `ans`, so that next digit can be added
        # `n & 1`: bitwise AND, getting the LSB of `n` (0 & 1 = 0; 1 & 1 = 1)
        # `ans = ans << 1 | n & 1`: bitwise OR, adding the LSB of `n` to `ans` (0 | 0 = 0; 0 | 1 = 1)
        # `n >>= 1`: right shift `n` by one bit as the current LSB is processed, and we need the next LSB
    return ans

    # Follow up: If this function is called many times, how would you optimize it?
