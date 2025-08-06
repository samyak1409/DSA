"""
https://leetcode.com/problems/smallest-index-with-digit-sum-equal-to-index
"""


def smallest_index(nums: list[int]) -> int:
    """"""

    # 1) Optimal (Simulate: Loop, to_str): TC = O(n); SC = O(1)

    for i, num in enumerate(nums):
        if sum(map(int, str(num))) == i:
            return i
    return -1
