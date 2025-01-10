"""
https://leetcode.com/problems/minimum-number-of-operations-to-make-elements-in-array-distinct
"""


def minimum_operations(nums: list[int]) -> int:
    """"""

    # 1) Brute-force (Simulate: HashSet, Loop): TC = O(n^2); SC = O(n)

    """
    cnt = 0
    while len(set(nums)) != len(nums):
        nums = nums[3:]
        cnt += 1
    return cnt
    """

    # 1) Optimal (Reverse Iterate, HashSet, Maths: Directly calc the ops): TC = O(n); SC = O(n)

    from math import ceil

    hs = set()
    # Reverse iter:
    for i in range(len(nums)-1, -1, -1):
        # If num is already seen:
        if (num := nums[i]) in hs:
            # We need to remove all the elements from beginning till here in the chunks of 3, directly calc:
            return ceil((i+1)/3)  # (`i` is index, so +1 to get the num of elements)
        hs.add(num)
    # Arr had no duplicates, so return 0:
    return 0
