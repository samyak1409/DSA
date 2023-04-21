"""
https://leetcode.com/problems/form-smallest-number-from-two-digit-arrays
"""


def min_number(nums1: list[int], nums2: list[int]) -> int:
    """"""

    # How many digits will the resulting number have at most?
    # The resulting number will have either one or two digits. Try to find when each case is possible.

    # 1) Optimal (HashSet): TC = O(n); SC = O(n)

    """
    # Find Min Intersection:
    nums1 = set(nums1)  # O(1) lookup
    min_ = float('inf')  # init
    for num in nums2:
        if num in nums1:
            min_ = min(min_, num)
    '''
    # If intersection is there return the min one:
    if min_ != float('inf'):
        return min_
    # Else just choose the smallest digits out of the two and make a min num from them and return:
    x, y = sorted([min(nums1), min(nums2)])
    return x*10 + y
    '''
    # One liner:
    # return min_ if min_ != float('inf') else int(''.join(map(str, sorted([min(nums1), min(nums2)]))))
    # Better:
    return min_ if min_ != float('inf') else min(tup := (min(nums1), min(nums2)))*10 + max(tup)
    """

    # Shorter using `set.intersection`:
    # https://leetcode.com/problems/form-smallest-number-from-two-digit-arrays/solutions/3366413/intersection

    return min(set(nums1).intersection(set(nums2)), default=None) or min(tup := (min(nums1), min(nums2)))*10 + max(tup)
