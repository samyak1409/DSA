"""
https://leetcode.com/problems/missing-number/
"""


from typing import List


def missingNumber(nums: List[int]) -> int:

    n = len(nums)
    return ((n*(n+1))//2) - sum(nums)  # TC = O(n); SC = O(1)
