"""
https://leetcode.com/problems/minimum-common-value
"""


def get_common(nums1: list[int], nums2: list[int]) -> int:
    """"""

    # Try to use a set.
    # 1) Time Optimal (Set): TC = O(n); SC = O(n)

    """
    nums1 = set(nums1)  # hash nums1 for O(1) lookup
    # Traverse nums2 and return first common:
    for num in nums2:
        if num in nums1:
            return num
    # If no common returned:
    return -1
    """

    # Otherwise, try to use a two-pointer approach.
    # 2) Optimal (Two-Pointers): TC = O(n); SC = O(1)
    # Like `Merge Two Sorted Array`
    # https://leetcode.com/problems/minimum-common-value/solutions/3082138/two-pointer-vs-one-hashset

    n1, n2 = len(nums1), len(nums2)
    i = j = 0

    while i < n1 and j < n2:  # while not out of both
        if (num1 := nums1[i]) == (num2 := nums2[j]):  # if equal (common)
            return num1
        # else increment the one with the lesser val:
        if num1 > num2:
            j += 1
        else:  # (num1 < num2)
            i += 1

    return -1  # no common found
