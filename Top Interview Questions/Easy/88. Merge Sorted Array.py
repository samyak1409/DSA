"""
https://leetcode.com/problems/merge-sorted-array/
"""


from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """Do not return anything, modify nums1 in-place instead."""

    # TC = O(m+n); SC = O(m)

    copy = nums1[:m]

    i = j = k = 0

    while i < m and j < n:

        if copy[i] <= nums2[j]:
            nums1[k] = copy[i]
            i += 1
        else:
            nums1[k] = nums2[j]
            j += 1
        k += 1

    if i < m:
        nums1[k:] = copy[i:]
    elif j < n:
        nums1[k:] = nums2[j:]
