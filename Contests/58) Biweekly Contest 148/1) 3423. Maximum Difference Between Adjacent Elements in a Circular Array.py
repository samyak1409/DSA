"""
https://leetcode.com/problems/maximum-difference-between-adjacent-elements-in-a-circular-array
"""


def max_adjacent_distance(nums: list[int]) -> int:
    """"""

    # 1) Optimal (Iterate): TC = O(n); SC = O(1)

    """
    ans = abs(nums[0]-nums[-1])  # for first and last element
    # For all others:
    for i in range(len(nums)-1):
        ans = max(ans, abs(nums[i+1]-nums[i]))
    return ans
    """

    # Benefitting from negative indexing, we can handle the corner case in main iteration only:

    return max(abs(nums[i]-nums[i-1]) for i in range(len(nums)))
