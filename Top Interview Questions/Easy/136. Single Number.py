"""
https://leetcode.com/problems/single-number/
"""


from typing import List


def singleNumber(nums: List[int]) -> int:

    # 1) Using Bitwise XOR Operator (^): TC = O(n); SC = O(1)

    """
    res = 0  # (A ^ A = 0)
    for num in nums:
        res ^= num  # https://en.wikipedia.org/wiki/Exclusive_or#Truth_table -> (BITWISE)
    return res
    """

    # Note- Order of numbers is different, still it's working, why?
    #       Because XOR is Commutative, why?
    #               Because We're using BITWISE XOR (applying XOR bit by bit)

    # 1.1) Pythonic way of doing the same thing: Using functools.reduce():

    from functools import reduce
    return reduce(lambda x, y: x ^ y, nums)  # reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates ((((1+2)+3)+4)+5)

    # 2) Using MATHEMATICS: TC = O(n) = SC

    # return 2*sum(set(nums)) - sum(nums)
