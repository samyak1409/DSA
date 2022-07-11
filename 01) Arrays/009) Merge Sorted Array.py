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

    """
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
    """

    # 2) Optimal (Reverse Traverse 👌 and Compare) (https://leetcode.com/problems/merge-sorted-array/discuss/29503/Beautiful-Python-Solution): TC = O(m+n); SC = O(1)

    while m > 0 and n > 0:
        num1, num2 = nums1[m - 1], nums2[n - 1]
        if num1 > num2:
            nums1[m + n - 1] = num1
            m -= 1
        else:
            nums1[m + n - 1] = num2
            n -= 1
    nums1[:n] = nums2[:n]  # if nums1 had lesser no. of elements than nums2 (m < n)
    # otherwise (if m > n) the elements are already on the right place only!
