"""
https://leetcode.com/problems/minimum-pair-removal-to-sort-array-i
"""


def minimum_pair_removal(nums: list[int]) -> int:
    """"""

    # 1) Brute-force (Simulate; Nested Loop): TC = O(n^2); SC = O(n) {sort}

    ops = 0
    while nums != sorted(nums):
        min_sum, idx = float('inf'), None
        for i in range(len(nums)-1):
            if (curr_sum:=nums[i]+nums[i+1]) < min_sum:
                idx, min_sum = i, curr_sum
        nums.pop(idx)
        nums[idx] = min_sum
        ops += 1
    return ops
