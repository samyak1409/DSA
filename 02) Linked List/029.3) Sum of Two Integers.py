"""
https://leetcode.com/problems/sum-of-two-integers
"""


def get_sum(a: int, b: int) -> int:
    """"""

    # -1) Prohibited (+ / __add__): TC = O(1); SC = O(1)

    """
    return a + b
    """
    """
    return a.__add__(b)
    """

    # 1) Optimal (Bit Manipulation): TC = O(1) {"-1000 <= a, b <= 1000" => 1 <= len(a), len(b) <= 10}; SC = O(1)
    # Easiest Explanation:
    # https://leetcode.com/problems/sum-of-two-integers/discuss/132479/Simple-explanation-on-how-to-arrive-at-the-solution
    # Intuition: We can't use `+` or `__add__`, so let's try it with Bit Manipulation.
    #   1 -> 01      2 -> 010
    # + 2 -> 10    + 3 -> 011
    # = 3 -> 11    = 5 -> 101
    # What results do we want? We want:
    # 0 0 -> 0
    # 0 1 -> 1
    # 1 0 -> 1
    # 1 1 -> 0 (and 1 carry, let's leave it for later)
    # So, we can observe that this is nothing but Truth Table of our loving XOR (^).
    # Now, the case of carry, we can clearly see it will only arrive with both 1 bits, so, yes, AND (&).
    # But, we need the carry to be placed on the left of what we'll get from AND, so we can just "LEFT SHIFT" (<<) by 1.
    # Now, we just need to find a way to combine these two.
    # Just XOR them two, and repeat till carry is not 0.

    """
    while True:
        sum_wo_carry = a ^ b  # sum without carry using XOR
        carry = (a & b) << 1  # carry using AND & LEFT SHIFT
        if carry:  # repeat if carry is there
            a, b = sum_wo_carry, carry
        else:
            return sum_wo_carry
    """
    # Conciser:
    """
    while b:  # while carry is there
        a, b = a ^ b, (a & b) << 1  # sum without carry using XOR, carry using AND & LEFT SHIFT
    return a
    """

    # But what if a or b is negative?
    # Binary world handles negative cases by itself, in other words no matter is it "7" or "-7" - in binary world they
    # are just two different numbers. For example, "-1" is "11111111111111111111111111111111"; "-2" is
    # "11111111111111111111111111111110"; "-3" is "11111111111111111111111111111101".
    # FOR OTHER LANGS, NOT FOR PYTHON!!!!
    # https://leetcode.com/problems/sum-of-two-integers/discuss/776952/Python-BEST-LeetCode-371-Explanation-for-Python
    # The correctness of this version relies on the fact that integers have fixed length (32 bits) in java.
    # So carry (or b) will eventually be moved out of boundary and go to 0, and you can get out of the while loop.
    # This is NOT the case for the Python! Python allows unlimited length of integers.
    # If you try to mimic the code above, you will get to infinite loop!

    # 0) LOL: TC = O(1); SC = O(1)

    return sum((a, b))


# Bit Hacks: http://graphics.stanford.edu/~seander/bithacks.html
