"""
https://leetcode.com/problems/sort-colors
"""


from typing import List


def sortColors(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """

    # 0) Brute-force (Sorting): TC = O(n*log(n)); SC = O(1)

    """
    nums.sort()
    """

    # 1) Counting Sort (two-pass algorithm using constant extra space): TC = O(n); SC = O(1)

    """
    from collections import Counter

    n = Counter(nums)  # O(n)
    # print(n)  #debugging

    nums[:] = [0]*n[0] + [1]*n[1] + [2]*n[2]  # O(n)
    # New Discovery: e.g. 2 is not there in nums, still n[2] will not give an error because n is a Counter object, and it handles that (by default returns 0 value if a key is not there)
    """
