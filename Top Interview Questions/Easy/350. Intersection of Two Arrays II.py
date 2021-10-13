"""
https://leetcode.com/problems/intersection-of-two-arrays-ii/
"""


from typing import List


def intersect(nums1: List[int], nums2: List[int]) -> List[int]:

    # 1) Brute Force (Space Optimized using yield): TC = O(mn); SC = O(1)

    """
    for num in nums1:  # O(m)
        if num in nums2:  # O(n)
            yield num
            nums2.remove(num)  # O(n)
    """

    # 2) Using Hash Table: TC = O(m+n); SC = O(m)

    """
    ht = {}
    for num in nums1:
        ht[num] = ht.get(num, 0) + 1
    """

    from collections import Counter
    ht = Counter(nums1)  # does the same work as above

    for num in nums2:
        if ht.get(num):
            yield num
            ht[num] -= 1
