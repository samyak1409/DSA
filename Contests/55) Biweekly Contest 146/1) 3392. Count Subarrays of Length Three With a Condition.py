"""
https://leetcode.com/problems/count-subarrays-of-length-three-with-a-condition
"""


def count_subarrays(nums: list[int]) -> int:
    """"""

    # 1) Optimal (Iterate): TC = O(n); SC = O(1)

    """
    ans = 0
    for i in range(len(nums)-2):
        ans += (nums[i]+nums[i+2])*2 == nums[i+1]  # "Why divide when you can multiply."
    return ans
    """
    # One-liner:
    return sum((nums[i]+nums[i+2])*2 == nums[i+1] for i in range(len(nums)-2))
