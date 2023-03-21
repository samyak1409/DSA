"""
https://leetcode.com/problems/maximize-greatness-of-an-array
"""


def maximize_greatness(nums: list[int]) -> int:
    """"""

    # Can we use sorting and two pointers here?
    # Assign every element the next bigger unused element as many times as possible.

    # 1) Sub-Optimal (Sort + 2 Pointers): TC = O(n*log(n)); SC = O(n)
    # https://leetcode.com/problems/maximize-greatness-of-an-array/solutions/3312061/java-c-python-easy-and-concise-o-n

    """
    nums = sorted(nums)

    i, j = 0, 1
    while j != len(nums):
        if nums[j] > nums[i]:
            i += 1
        j += 1
    return i
    """
    # More Concise:
    """
    nums = sorted(nums)

    i = 0
    for num in nums:
        if num > nums[i]:  # we found a bigger num
            i += 1  # let's go to next num
    return i
    """

    # 2) Optimal (Maths): TC = O(n); SC = O(n)
    # This solution is based on the mathematical fact that we can arrange the nums like:
    # (These are indices of the sorted nums.)
    # 0,   1,   2,   3...
    # k, k+1, k+2, k+3...
    # where, k == max(Counter(nums).values())
    # (Dry run on some test cases.)
    # https://leetcode.com/problems/maximize-greatness-of-an-array/solutions/3312061/java-c-python-easy-and-concise-o-n

    from collections import Counter
    return len(nums) - max(Counter(nums).values())
