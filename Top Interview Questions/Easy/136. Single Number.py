"""
https://leetcode.com/problems/single-number/
"""


from typing import List


def singleNumber(nums: List[int]) -> int:

    # 1) Using Bitwise XOR Operator (^): TC = O(n); SC = O(1)

    """
    res = 0  # (A ^ 0 = A)
    for num in nums:
        res ^= num  # BITWISE https://en.wikipedia.org/wiki/Exclusive_or#Truth_table (same digits -> 0; diff digits -> 1)
    return res
    """

    # Note- Order of numbers is different, still it's working, why?
    #       Because 1) The operation is Commutative
    #               2) A ^ A = 0
    #               3) A ^ 0 = A

    # 1.1) Pythonic way of doing the same thing (using functools.reduce()):

    from functools import reduce
    return reduce(lambda x, y: x ^ y, nums)  # reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) => ((((1+2)+3)+4)+5)

    # 2) Using MATHEMATICS: TC = O(n) = SC

    # return 2*sum(set(nums)) - sum(nums)
