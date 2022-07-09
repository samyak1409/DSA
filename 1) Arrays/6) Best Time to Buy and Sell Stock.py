"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock
"""


from typing import List


def maxProfit(prices: List[int]) -> int:

    # 0) Brute-force (Calculating profits for all the combinations) (TLE): TC = O(n^2); SC = O(1)

    n = len(prices)
    max_profit = 0
    for i in range(n):  # considering all the prices in the array one by one as cost price
        for j in range(i+1, n):  # for a particular cost price, all the prices in the next days will be the selling prices
            profit = prices[j] - prices[i]  # selling_price - cost_price
            if profit > max_profit:
                max_profit = profit
    return max_profit
