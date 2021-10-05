"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array/
"""


from typing import List


def removeDuplicates(nums: List[int]) -> int:

    # Method 1 (Generic):

    """
    prev = 101  # acc. to constraints
    i = 0

    for _ in range(len(nums)):

        if nums[i] == prev:
            nums.pop(i)

        else:
            prev = nums[i]
            i += 1

    return len(nums)
    """

    # Method 2 (Pythonic):

    nums[:] = sorted(set(nums))  # nums[:] -> not creating new object
    return len(nums)
