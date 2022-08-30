"""
https://leetcode.com/problems/merge-sorted-array
"""


def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """Do not return anything, modify nums1 in-place instead."""

    # 0) Brute-force (Add nums2 to nums1[m:], sort num1): TC = O((m+n)*log(m+n)); SC = O(m+n)

    """
    nums1[m:] = nums2  # TC = O(n)
    nums1.sort()  # TC = O((m+n)*log(m+n)); SC = O(m+n)
    """

    # Follow up: Can you come up with an algorithm that runs in O(m + n) time?

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

    # 2) Optimal (Reverse Traverse 👌 and Compare): TC = O(m+n); SC = O(1)
    # https://leetcode.com/problems/merge-sorted-array/discuss/29503/Beautiful-Python-Solution

    while m > 0 and n > 0:
        num1, num2 = nums1[m-1], nums2[n-1]  # -1 coz index
        if num1 > num2:
            nums1[m+n-1] = num1
            m -= 1
        else:
            nums1[m+n-1] = num2
            n -= 1
    nums1[:n] = nums2[:n]  # if nums1 had lesser no. of elements than nums2 (m < n)
    # otherwise (if m > n) the elements are already on the right place only!


# ALSO, the same question with a little variation (https://youtu.be/hVl2b3bLzBw)
# If "To accommodate this, nums1 has a length of m + n" is not the case, and nums1 & nums2 has really the length m & n
# respectively.

# 0) Brute-force (Same intuition as above `0)`): TC = O((m+n)*log(m+n)); SC = O(m+n)

"""
temp_arr = nums1 + nums2  # TC = SC = O(m+n)
temp_arr.sort()  # TC = O((m+n)*log(m+n)); SC = O(m+n)
nums1[:], nums2[:] = temp_arr  # TC = O(m+n)
# IMP: `[:]` (won't create a new object (i.e. new memory address) but modify it only)
"""
# In short:
"""
nums1[:], nums2[:] = sorted(nums1+nums2)
"""

# 1) Space-Optimal (Gap Algo): TC = O((m+n)*log(m+n)); SC = O(1)

"""
from math import ceil
gap = ceil(m+n/2)  # initialize
while gap > 0:  # (last iteration when gap = 1)
    for i in range(m+n-gap):
        j = i + gap
        match (i < m, j < m):
            case (True, False):  # when i lies in nums1 and j in nums2
                if nums1[i] < nums2[j]:
                    nums1[i], nums2[j] = nums2[j], nums1[i]  # swap
            case (True, True):  # when i & j lies in nums1
                if nums1[i] < nums1[j]:
                    nums1[i], nums1[j] = nums1[j], nums1[i]  # swap
            case (False, False):  # when i & j lies in nums2
                if nums2[i] < nums2[j]:
                    nums2[i], nums2[j] = nums2[j], nums2[i]  # swap
    gap = ceil(gap/2)
"""

# 2) Time-Optimal (Same intuition as above `1)`: Copy, Traverse & Compare): TC = O(m+n); SC = O(m+n)
# When the nums1 & nums2 are sorted why just not benefit from this and not sort the summed array and make the TC go
# from O((m+n)*log(m+n)) to O(m+n).

"""
# TC = SC = O(m+n) for following 11 lines:
temp_arr = []
i = j = 0  # two pointers
while i < m and j < n:
    num1, num2 = nums1[i], nums2[j]
    if num1 <= num2:
        temp_arr.append(num1)
        i += 1
    else:
        temp_arr.append(num2)
        j += 1
temp_arr.extend(nums1[i:] or nums2[j:])
nums1[:], nums2[:] = temp_arr  # TC = O(m+n)
"""


# Similar Questions:
# https://leetcode.com/problems/merge-two-sorted-lists
# https://leetcode.com/problems/squares-of-a-sorted-array
# https://leetcode.com/problems/interval-list-intersections
