"""
https://leetcode.com/problems/number-of-distinct-averages
"""


def distinct_averages(nums: list[int]) -> int:
    """"""

    # 1) Optimal (Sort): TC = O(n*log(n)); SC = O(n)
    # Try sorting the array.
    # Store the averages being calculated, and find the distinct ones.

    nums = sorted(nums)  # TC = O(n*log(n))
    distinct = set()  # SC = O(n)
    for i in range(len(nums)//2):  # TC = O(n)
        distinct.add((nums[i]+nums[~i])/2)
    return len(distinct)
