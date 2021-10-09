"""
https://leetcode.com/problems/maximum-subarray/
"""


from typing import List


def maxSubArray(nums: List[int]) -> int:

    # https://en.wikipedia.org/wiki/Maximum_subarray_problem#Kadane's_algorithm: TC = O(n); SC = O(1)

    for i in range(1, len(nums)):

        if nums[i-1] > 0:

            nums[i] += nums[i-1]

    return max(nums)

    # The thought follows a simple rule:
    # If the sum of a sub-array is positive, it has possible to make the next value bigger, so we keep do it until it turn to negative.
    # If the sum is negative, it has no use to the next element, so we break.
    # It is a game of sum, not the elements.
