"""
https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer
"""


def maximum_count(nums: list[int]) -> int:
    """"""

    # Count how many positive integers and negative integers are in the array.
    # 0) Brute-force (Linearly Count and Return Max): TC = O(n); SC = O(1)

    """
    p = n = 0
    for num in nums:
        p += num > 0
        n += num < 0
    return max(p, n)
    """

    # One liner:
    """
    return max(sum(num > 0 for num in nums), sum(num < 0 for num in nums))
    """

    # Since the array is sorted, can we use the binary search?
    # 1) Optimal (Binary Search): TC = O(log(n)); SC = O(1)
    # https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/solutions/3017003/c-java-python3-binary-search

    """
    # Helper Function:
    # https://github.com/python/cpython/blob/main/Lib/bisect.py
    # https://en.wikipedia.org/wiki/Binary_search_algorithm#Procedure_for_finding_the_leftmost_element
    def bisect_left(a: list[int], x: int) -> int:
        lo, hi = 0, len(a)
        while lo < hi:
            mid = (lo + hi) // 2
            if a[mid] < x:
                lo = mid + 1
            else:
                hi = mid
        return lo

    return max(bisect_left(nums, 0), len(nums)-bisect_left(nums, 1))
    """

    # Or use builtins:
    from bisect import bisect_left, bisect_right
    return max(bisect_left(nums, 0), len(nums)-bisect_right(nums, 0))
