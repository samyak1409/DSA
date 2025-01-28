"""
https://leetcode.com/problems/sum-of-variable-length-subarrays
"""


def subarray_sum(nums: list[int]) -> int:
    """"""

    # 1) Brute-force (Simulate: Loop): TC = O(n^2); SC = O(1)

    """
    ans = 0
    for i in range(len(nums)):
        start = max(0, i-nums[i])
        ans += sum(nums[j] for j in range(start, i+1))
    return ans
    """

    # 2) Optimal (Prefix Sum): TC = O(n); SC = O(n)

    from itertools import accumulate

    ps = list(accumulate(nums, initial=0))

    ans = 0
    for i in range(len(nums)):
        start = max(0, i-nums[i])
        ans += ps[i+1] - ps[start]
    return ans
