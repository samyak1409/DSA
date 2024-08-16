"""
https://leetcode.com/problems/intersection-of-two-arrays-ii
"""


def intersect(nums1: list[int], nums2: list[int]) -> list[int]:

    # 0) Brute Force: TC = O(mn); SC = O(1)

    """
    for num in nums1:  # O(m)
        if num in nums2:  # O(n)
            yield num
            nums2.remove(num)  # O(n)
    """

    # 1) Sort, then 2 pointers: TC = O(m log m + n log n); SC = O(1)

    """
    for x in (nums1, nums2):
        x.sort()

    i = j = 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            i += 1
        elif nums1[i] > nums2[j]:
            j += 1
        else:
            yield nums1[i]
            i += 1
            j += 1
    """

    # 2) Using Hash Table: TC = O(m+n); SC = O(min(m, n))

    if len(nums2) < len(nums1):  # 👌
        yield from intersect(nums2, nums1)
        return  # "don't execute the following code" (because yield doesn't return)

    """
    ht = {}
    for num in nums1:  # O(m)
        ht[num] = ht.get(num, 0) + 1
    """

    from collections import Counter
    ht = Counter(nums1)  # O(m); does the same work as above

    for num in nums2:  # O(n)
        if ht[num] > 0:
            yield num
            ht[num] -= 1

    # Follow up:

    # What if the given array is already sorted? How would you optimize your algorithm?
    # => will use two pointer approach, TC = O(max(m, n)); SC = O(1)

    # What if nums1's size is small compared to nums2's size? Which algorithm is better?
    # => using hash table, TC = O(m+n); SC(m) (m is small)

    # What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements
    # into the memory at once?
    # => use hash table approach (create hash table of nums1, then sequentially load chunks of nums2 and process.)
