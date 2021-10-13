"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""


from typing import List


def maxProfit(prices: List[int]) -> int:

    # Kadane's Algo: TC = O(n); SC = O(1)

    min_price = float('inf')  # at first, any price will be less than this
    max_profit = 0  # at first, any day's profit will be greater than this

    for price in prices:

        if price < min_price:
            min_price = price

        elif price-min_price > max_profit:  # price-min_price = current day profit
            max_profit = price - min_price

    return max_profit
