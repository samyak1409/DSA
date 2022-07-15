"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock
"""


def maxProfit(prices: list[int]) -> int:
    """"""

    # 0) Brute-force (Calculating profits for all the combinations) (TLE): TC = O(n^2); SC = O(1)

    """
    n = len(prices)
    max_profit = 0
    for i in range(n):  # considering all the prices in the array one by one as cost price
        for j in range(i+1, n):  # for a particular cost price, all the prices in the next days will be the selling prices
            current_profit = prices[j] - prices[i]  # selling_price - cost_price
            if current_profit > max_profit:
                max_profit = current_profit
    return max_profit
    """

    # 1) Kadane's Algo: TC = O(n); SC = O(1)

    cost_price = prices[0]  # initialization
    max_profit = 0
    for current_price in prices[1:]:
        if current_price < cost_price:
            cost_price = current_price  # bought stock at a lesser price
            continue  # bought stock on this day, so doesn't make sense to try selling because profit will obviously be 0
        current_profit = current_price - cost_price
        if current_profit > max_profit:
            max_profit = current_profit
    return max_profit
