"""
https://leetcode.com/problems/contains-duplicate/
"""


from typing import List


def containsDuplicate(nums: List[int]) -> bool:

    # Using Set: TC = O(n) = SC

    return len(nums) != len(set(nums))
