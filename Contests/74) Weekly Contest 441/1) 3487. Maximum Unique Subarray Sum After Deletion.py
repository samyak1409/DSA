"""
https://leetcode.com/problems/maximum-unique-subarray-sum-after-deletion
"""


def max_sum(nums: list[int]) -> int:
    """"""

    # 1) Optimal (HashSet, Greedy): TC = O(n); SC = O(n)

    ans = 0
    # Loop on unique elements:
    for num in set(nums):
        # Since we want to maximize, only consider +ve nums [Greedy]:
        if num > 0:
            ans += num
    # If we got no sums in `ans`, return `max(nums)` as we can't make the arr empty, else return `ans`:
    return ans if ans else max(nums)
