"""
https://leetcode.com/problems/maximum-difference-between-increasing-elements
"""


def maximum_difference(nums: list[int]) -> int:
    """"""

    # https://leetcode.com/problems/maximum-difference-between-increasing-elements/discuss/1486523/121.-Best-Time-to-Buy-and-Sell-Stock
    # The only difference from "Best Time to Buy and Sell Stock" is that we need to return -1 if no profit can be made.
    # https://github.com/samyak1409/DSA/blob/main/01%29%20Arrays/006%29%20Best%20Time%20to%20Buy%20and%20Sell%20Stock.py

    smallest = float('inf')
    max_diff = 0
    for num in nums:
        smallest = min(smallest, num)
        max_diff = max(max_diff, num-smallest)  # `num-smallest` = current difference
    return max_diff or -1
