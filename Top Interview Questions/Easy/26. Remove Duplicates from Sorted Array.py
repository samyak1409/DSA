"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array/
"""


from typing import List


def removeDuplicates(nums: List[int]) -> int:

    # Two Pointers: TC = O(n); SC = O(1)

    """
    prev = None
    i = -1
    
    for num in nums:
        if num != prev:
            i += 1
            nums[i] = num
            prev = num

    return i+1
    """

    i = 0

    for num in nums[1:]:
        if num != nums[i]:
            i += 1
            nums[i] = num

    return i+1
