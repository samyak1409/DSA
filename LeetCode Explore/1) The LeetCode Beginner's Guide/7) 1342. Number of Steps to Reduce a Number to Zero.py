"""
https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero
"""


def number_of_steps(num: int) -> int:
    """"""

    # 2) Optimal: TC = O(log2(n)); SC = O(1)

    # 2.1) Simulate the process to get the final answer:

    """
    steps = 0
    while num:
        '''
        if num % 2 == 0:
            num //= 2
        else:
            num -= 1
        '''
        num = num-1 if num % 2 else num//2
        steps += 1
    return steps
    """

    # 2.2) Bit Manipulation:
    # See the top-notch video explanation here:
    # https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4425

    """
    steps = 0
    while num:
        '''
        if num & 1 == 0:  # `1`: Bitmask! (https://en.wikipedia.org/wiki/Mask_(computing))
            num >>= 1
        else:
            num -= 1
        '''
        num = num-1 if num & 1 else num >> 1
        steps += 1
    return steps
    """

    # 1) Time-optimal (Binary Repr, One Liner): TC = O(log2(n)); SC = O(log2(n))
    # Now, with above algo in mind, we can just do:
    # In binary repr, `0` means /2 is possible so one step.
    # `1` means -1, and then /2 so two steps.
    # And in the last when only `1` is left, then only -1 is required which will make the num zero, so one step.

    bin_str = bin(num)[2:]
    return bin_str.count('0') + bin_str.count('1')*2 - 1
