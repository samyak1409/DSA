"""
https://leetcode.com/problems/contains-duplicate/
"""


from typing import List


def containsDuplicate(nums: List[int]) -> bool:

    # Method 2 (Similar; Generic): TC = O(n) = SC

    """
    hashset = set()

    for num in nums:

        if num in hashset:  # O(1)
            return True

        hashset.add(num)

    return False
    """

    # Method 1 (Pythonic): TC = O(n) = SC

    return len(nums) != len(set(nums))
