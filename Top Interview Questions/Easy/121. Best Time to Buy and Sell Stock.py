"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""


from typing import List


def maxProfit(prices: List[int]) -> int:

    # Kadane's Algo: TC = O(n); SC = O(1)

    cost_price = float('inf')  # at first, any price will be less than this
    max_profit = 0  # at first, any day's profit will be greater than this

    for cur_price in prices:  # n prices

        if cur_price < cost_price:  # buy stock
            cost_price = cur_price

        else:
            cur_profit = cur_price - cost_price
            if cur_profit > max_profit:
                max_profit = cur_profit

    return max_profit
