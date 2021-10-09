"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array/
"""


from typing import List


def removeDuplicates(nums: List[int]) -> int:

    # Method 1 (Generic): TC = O(n^2); SC = O(1)

    """
    prev = 101  # acc. to constraints
    i = 0

    for _ in range(len(nums)):  # O(n)

        if nums[i] == prev:
            nums.pop(i)  # O(n)

        else:
            prev = nums[i]
            i += 1

    return len(nums)
    """

    # Method 2 (Pythonic): TC = O(n log n); SC = O(n)

    """
    nums[:] = sorted(set(nums))  # nums[:] -> not creating new object
    return len(nums)
    """

    # Method 3 (Best, as acc. to the Q. we don't have to worry what is at the end of the array): TC = O(n); SC = O(1)

    x = 1

    for i in range(len(nums)-1):

        if nums[i] != nums[i+1]:

            nums[x] = nums[i+1]
            x += 1

    return x
