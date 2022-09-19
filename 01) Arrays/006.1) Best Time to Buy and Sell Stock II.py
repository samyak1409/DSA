"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii
"""


def max_profit(prices: list[int]) -> int:
    """"""

    # 1) Optimal (Greedy: Consider +ve difference of prices b/w every two consecutive days): TC = O(n); SC = O(1)
    # https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/solution/#approach-3-simple-one-pass
    # But why does this work? MATHEMATICS!
    # "Suppose the first sequence is "a <= b <= c <= d", the profit is "d - a = (b - a) + (c - b) + (d - c)" without a
    # doubt. And suppose another one is "a <= b >= b' <= c <= d", the profit is not difficult to be figured out as
    # "(b - a) + (d - b')". So you just target at monotone sequences."
    # -https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/discuss/39420/Three-lines-in-C++-with-explanation

    """
    maxi_profit = 0
    for i in range(len(prices)-1):
        profit = prices[i+1] - prices[i]  # profit (+/0/-) if we buy today and sell tomorrow
        if profit > 0:  # if profit was made
            maxi_profit += profit
    return maxi_profit
    """
    # Conciser:
    maxi_profit = 0
    for i in range(len(prices)-1):
        maxi_profit += max(prices[i+1]-prices[i], 0)  # `prices[i+1]-prices[i]`: profit;
        # so `max(prices[i+1]-prices[i], 0)` means: profit if it's +ve else 0
    return maxi_profit
