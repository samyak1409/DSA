"""
https://leetcode.com/problems/single-number
"""


def single_number(nums: list[int]) -> int:
    """"""

    # https://leetcode.com/problems/single-number/solutions/1771720/c-easy-solutions-sorting-xor-maps-or-frequency-array

    # 0.1) Brute-force (Sort): TC = O(n*log(n)); SC = O(n)

    # 0.2) Time-Optimal Brute-force (`collections.Counter`): TC = O(n); SC = O(n)

    # 1) Time-Optimal (Maths & HashSet): TC = O(n); SC = O(n)

    """
    return 2*sum(set(nums)) - sum(nums)
    """

    # 2) Optimal (Bit Manipulation: Using XOR): TC = O(n); SC = O(1)
    # A ^ A = 0

    """
    ans = 0  # (A ^ 0 = A, so we can init with 0)
    for num in nums:
        ans ^= num  # BITWISE; https://en.wikipedia.org/wiki/Exclusive_or#Bitwise_operation
        # (same digit -> 0; diff digit -> 1)
    return ans
    """

    # Note - Order of numbers is different, still it's working, why? Because:
    # 1) The operation is Commutative (a binary operation is commutative if changing the order of the operands does not
    # change the result)
    # 2) A ^ A = 0
    # 3) A ^ 0 = A

    # Pythonic way of doing the same thing (using `functools.reduce`):
    from functools import reduce
    return reduce(lambda x, y: x ^ y, nums)  # reduce(lambda x, y: x+y, [1, 2, 3, 4]) = ((1 + 2) + 3) + 4

    # Hence, the requirement in the problem statement,
    # "You must implement a solution with a linear runtime complexity and use only constant extra space."
    # can be satisfied ONLY AND ONLY IF one know about XOR.
