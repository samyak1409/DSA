"""
https://leetcode.com/problems/maximum-difference-between-increasing-elements
"""


def maximum_difference(nums: list[int]) -> int:
    """"""

    # The only difference in code from `006 Best Time to Buy and Sell Stock.py`
    # (https://github.com/samyak1409/DSA/blob/main/01%29%20Arrays/006%29%20Best%20Time%20to%20Buy%20and%20Sell%20Stock.py)
    # is that we need to return -1 if no profit can be made.
    # https://leetcode.com/problems/maximum-difference-between-increasing-elements/discuss/1486523/121.-Best-Time-to-Buy-and-Sell-Stock

    # 1) Optimal (Kadane's Algo): TC = O(n); SC = O(1)

    min_num, max_diff = float('inf'), 0
    for num in nums:
        min_num = min(min_num, num)
        max_diff = max(max_diff, num-min_num)  # `num-min_num` = current difference
    return max_diff or -1
