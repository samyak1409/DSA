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

    # Since the array is sorted, can we use the binary search?
    # 1) Optimal (Binary Search): TC = O(log(n)); SC = O(1)

    # Write yourself like this:
    # https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/solutions/3016725/java-binary-search-commented

    # Or use builtins:
    # https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/solutions/3017003/c-java-python3-binary-search
    from bisect import bisect_left, bisect_right
    return max(bisect_left(nums, 0), len(nums)-bisect_right(nums, 0))
