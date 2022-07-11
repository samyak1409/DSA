"""
https://leetcode.com/problems/merge-sorted-array
"""


from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """Do not return anything, modify nums1 in-place instead."""

    # 0) Brute-force (Add nums2 to nums1[m:], sort num1): TC = O((m+n)*log(m+n)); SC = O(1)

    """
    nums1[m:] = nums2  # TC = O(n)
    nums1.sort()  # TC = O((m+n)*log(m+n))
    """

    # 1) Better (Copy, Traverse & Compare): TC = O(m+n); SC = O(m)

    nums1_copy = nums1[:m]  # SC = O(m)
    i = j = 0  # two pointers
    while i < m and j < n:
        num1, num2 = nums1_copy[i], nums2[j]
        if num1 <= num2:
            nums1[i+j] = num1
            i += 1
        else:
            nums1[i+j] = num2
            j += 1
    nums1[i+j:] = nums1_copy[i:] or nums2[j:]
