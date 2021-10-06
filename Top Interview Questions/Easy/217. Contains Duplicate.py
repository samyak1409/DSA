"""
https://leetcode.com/problems/contains-duplicate/
"""


from typing import List


def containsDuplicate(nums: List[int]) -> bool:

    # Method 2 (Similar; Generic): TC = SC = O(n)

    """
    hashset = set()

    for num in nums:

        if num in hashset:
            return True

        hashset.add(num)

    return False
    """

    # Method 1 (Pythonic): TC = SC = O(n)

    return len(nums) != len(set(nums))
