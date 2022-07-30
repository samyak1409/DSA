"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock
"""


def max_profit(prices: list[int]) -> int:
    """"""

    # 0) [TLE] Brute-force (Calculating profits for all the combinations): TC = O(n^2); SC = O(1)

    """
    n = len(prices)
    max_profit_ = 0
    for i in range(n):  # considering all the prices in the array one by one as cost price
        for j in range(i+1, n):  # for a particular cost price, all the prices in the next days will be selling prices
            current_profit = prices[j] - prices[i]  # selling_price - cost_price
            if current_profit > max_profit_:
                max_profit_ = current_profit
    return max_profit_
    """

    # 1) Optimal (Kadane's Algo): TC = O(n); SC = O(1)

    cost_price = prices[0]  # initialization
    max_profit_ = 0
    for current_price in prices[1:]:
        if current_price < cost_price:
            cost_price = current_price  # bought stock at a lesser price
            continue  # bought stock on this day, so doesn't make sense selling because profit will obviously be 0
        current_profit = current_price - cost_price
        if current_profit > max_profit_:
            max_profit_ = current_profit
    return max_profit_
