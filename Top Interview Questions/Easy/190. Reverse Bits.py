"""
https://leetcode.com/problems/reverse-bits/
"""


def reverseBits(n: int) -> int:

    # 0) Using functions (not something to do in an interview): TC = O(1); SC = O(1)

    """
    print(n)  # passed arg is of type int

    b_ = bin(n)[2:]  # deci -> bin and trimming that '0b' (denote binary nums in python)
    print(b_)

    b = b_.zfill(32)  # "32 bits" unsigned integer
    print(b)

    rb = b[::-1]  # reversing
    print(rb)

    return int(rb, base=2)  # bin -> deci
    """

    """
    return int(bin(n)[2:].zfill(32)[::-1], base=2)
    """

    # 1) Bit Manipulation: TC = O(1); SC = O(1)

    """
    https://leetcode.com/problems/reverse-bits/discuss/732138/Python-O(32)-simple-solution-explained

    We are asked to reverse bits in our number. What is the most logical way to do it? Create number out, process 
    original number bit by bit from end and add this bit to the end of our out number, and that is all! Why it is works?

    out = (out << 1) | (n & 1) adds last bit of n to out
    n >>= 1 removes last bit from n.

    Imagine number n = 11011010, and out = 0
    out = 0, n = 1101101
    out = 01, n = 110110
    out = 010, n = 11011
    out = 0101, n = 1101
    out = 01011, n = 110
    out = 010110, n = 11
    out = 0101101, n = 1
    out = 01011011, n = 0

    Complexity: time complexity is O(32), space complexity is O(1).
    """

    ans = 0  # note that type(n) = type(ans) = int; python will apply the bit ops on underlying binary only!

    for _ in range(32):  # "32 bits" unsigned integer

        ans <<= 1  # left shift ans. by 1 bit, so that next digit can be appended to ans

        if n:  # once n is 0; "ans <<= 1" will keep shifting till correct ans is not formulated!

            n_lsb = n & 1  # (bitwise AND) getting the LSB of n (0 & 1 = 0; 1 & 1 = 1) try yourself

            ans |= n_lsb  # (bitwise OR) adding the LSB of n to the ans (0 | 0 = 0; 0 | 1 = 1) try yourself

            n >>= 1  # right shift n by 1 bit as the current LSB is processed, and now we need the next LSB!

    return ans
