"""
https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero
"""


def number_of_steps(num: int) -> int:
    """"""

    # 1) Optimal: TC = O(log2(n)); SC = O(1)

    # 1.1) Simulate the process to get the final answer:

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

    # 1.2) Bit Manipulation:
    # See the top-notch video explanation here:
    # https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4425

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
