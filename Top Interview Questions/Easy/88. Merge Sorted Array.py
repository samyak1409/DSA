"""
https://leetcode.com/problems/merge-sorted-array/
"""


from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """Do not return anything, modify nums1 in-place instead."""

    # 1) Naive (Copy, Traverse and Compare): TC = O(m+n); SC = O(m)

    """
    n1_copy = nums1[:m]

    i = j = k = 0

    while i < m and j < n:

        if n1_copy[i] <= nums2[j]:
            nums1[k] = n1_copy[i]
            i += 1

        else:
            nums1[k] = nums2[j]
            j += 1

        k += 1

    '''
    if i < m:
        nums1[k:] = n1_copy[i:]

    elif j < n:
        nums1[k:] = nums2[j:]
    '''
    # or:
    nums1[k:] = n1_copy[i:] or nums2[j:]  # (unexpectedly Python doesn't throw error if 'i' or 'j' is greater than the lists' length while slicing)
    """

    # 2) Beautiful (Reverse Traverse 👌 and Compare) (https://leetcode.com/problems/merge-sorted-array/discuss/29503/Beautiful-Python-Solution): TC = O(m+n); SC = O(1)

    while m > 0 and n > 0:

        num1, num2 = nums1[m-1], nums2[n-1]

        if num1 > num2:
            nums1[m+n-1] = num1
            m -= 1

        else:
            nums1[m+n-1] = num2
            n -= 1

    nums1[:n] = nums2[:n]  # if nums2 had greater no. of elements than nums1
