"""
https://leetcode.com/problems/minimum-operations-to-make-array-sum-divisible-by-k
"""


def min_operations(nums: list[int], k: int) -> int:
    """"""

    # 1) Optimal (Maths): TC = O(n); SC = O(1)

    return sum(nums) % k
