"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii
"""


def max_profit(prices: list[int]) -> int:
    """"""

    # 1) Optimal (Linear Pass, Greedy): TC = O(n); SC = O(1)
    # https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/solution/#approach-3-simple-one-pass

    maxi_profit = 0
    for i in range(len(prices)-1):
        profit = prices[i+1] - prices[i]  # profit/0/loss if I buy today and sell tomorrow
        if profit > 0:  # if profit was made
            maxi_profit += profit
    return maxi_profit
