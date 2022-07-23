"""
https://leetcode.com/problems/two-sum
"""


def twoSum(nums: list[int], target: int) -> list[int]:
    """"""

    # 0) Brute-force (Nested Loop): TC = O(n^2); SC = O(1)

    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
