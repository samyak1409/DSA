"""
https://leetcode.com/problems/find-xor-beauty-of-array
"""


def xor_beauty(nums: list[int]) -> int:
    """"""

    # 1) Optimal (Simplify & XOR): TC = O(n); SC = O(1)
    # Try to simplify the given expression.
    # Try constructing the answer bit by bit.
    # "Proof:
    # -> First, note that by symmetry of i and j, we know that the value of ((nums[i] | nums[j]) & nums[k]) and
    # ((nums[j] | nums[i]) & nums[k]) are equal. Which then implies that for a pair of (i, j) where i != j, the bitwise
    # XOR of ((nums[i] | nums[j]) & nums[k]) and ((nums[j] | nums[i]) & nums[k]) is 0. Thus, we only need to deal with
    # the triplets (i, j, k) where i == j.
    # -> Now we only need to consider the triplets (i, j, k) where i == j, so that ((nums[i] | nums[j]) & nums[k]) =
    # ((nums[i] | nums[i]) & nums[k]) = nums[i] & nums[k]. By symmetry of i and k, we know that the value of nums[i] &
    # nums[k] and nums[k] & nums[i] are equal. Which then implies that for a pair of (i, k) where i != k, the bitwise
    # XOR of nums[i] & nums[k] and nums[k] & nums[i] is 0. Thus, we only need to deal with the case of i == k.
    # -> Therefore, we only need to consider the triplets (i, j, k) where i == j == k, and the final answer reduces to
    # the bitwise XOR of ((nums[i] | nums[j]) & nums[k]) = ((nums[i] | nums[i]) & nums[i]) = nums[i]."
    # -https://leetcode.com/problems/find-xor-beauty-of-array/solutions/3014972/python3-one-liner-with-formal-proof
    # https://leetcode.com/problems/find-xor-beauty-of-array/solutions/3015014/why-just-xor-of-all-numbers-works

    """
    xor = 0
    for num in nums:
        xor ^= num
    return xor
    """

    # (Pythonic):

    from functools import reduce
    from operator import xor

    return reduce(xor, nums)
