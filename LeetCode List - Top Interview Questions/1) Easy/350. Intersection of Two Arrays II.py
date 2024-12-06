"""
https://leetcode.com/problems/intersection-of-two-arrays-ii
"""


def intersect(nums1: list[int], nums2: list[int]) -> list[int]:
    """"""

    # 0) Brute-force (Two Loops): TC = O(m*n); SC = O(1)

    # Loop and compare:
    """
    res = []
    for num1 in nums1:  # O(m)
        for num2 in nums2:  # O(n)
            if num1 == num2:
                res.append(num1)
                nums2.remove(num2)  # so that num2 is not considered in next iter of outer loop; O(n)
                break
    return res
    """

    # Direct check membership:
    """
    res = []
    for num in nums1:  # O(m)
        if num in nums2:  # O(n)
            res.append(num)
            nums2.remove(num)  # O(n)
    return res
    """

    # Using try-except (EAFP):
    """
    res = []
    for num in nums1:  # O(m)
        try:
            nums2.remove(num)  # O(n)
        except ValueError:
            pass
        else:
            res.append(num)
    return res
    """

    # 1) Sub-optimal (Sort, Two Pointers): TC = O(m*log(m) + n*log(n)); SC = O(m+n)

    """
    nums1.sort(), nums2.sort()  # TC = O(m*log(m) + n*log(n)); SC = O(m+n)

    res = []
    i = j = 0
    while i < len(nums1) and j < len(nums2):  # O(m+n)
        if nums1[i] < nums2[j]:
            i += 1
        elif nums1[i] > nums2[j]:
            j += 1
        else:
            res.append(nums1[i])
            i, j = i+1, j+1
    return res
    """

    # 2) Optimal (HashMap): TC = O(m+n); SC = O(min(m, n))

    from collections import Counter

    if len(nums2) < len(nums1):  # making sure `nums1` is smaller array
        return intersect(nums2, nums1)

    '''
    ht = {}
    for num in nums1:  # TC = SC = O(m)
        ht[num] = ht.get(num, 0) + 1
    '''
    # Or just use `collections`:
    ht = Counter(nums1)  # TC = SC = O(m)

    res = []
    for num in nums2:  # O(n)
        if ht[num] > 0:
            res.append(num)
            ht[num] -= 1
    return res

    # Follow up:

    # What if the given array is already sorted? How would you optimize your algorithm?
    # => Two Pointers: TC = O(m+n); SC = O(1)

    # What if nums1's size is small compared to nums2's size? Which algorithm is better?
    # => HashMap on nums1: TC = O(m+n); SC(m) {m is smaller}

    # What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements
    # into the memory at once?
    # => Create hashmap of nums1, then sequentially load chunks of nums2 and process.

    # https://leetcode.com/problems/intersection-of-two-arrays-ii/solutions/1468295/python-2-approaches-3-follow-up-questions-clean-concise
