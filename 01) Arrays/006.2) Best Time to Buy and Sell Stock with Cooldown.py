"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown
"""


def max_profit(prices: list[int]) -> int:
    """"""

    # Just for elaboration:
    # -1) [WA] Optimal (Greedy: Consider +ve difference of prices b/w every two consecutive days): TC = O(n); SC = O(1)
    # At first, you might think that Greedy approach that we used in `006.1) Best Time to Buy and Sell Stock II.py`
    # (https://github.com/samyak1409/DSA/blob/main/01%29%20Arrays/006.1%29%20Best%20Time%20to%20Buy%20and%20Sell%20Stock%20II.py)
    # will work here too, but it'll not. See: Input: [1,2,4]; Output: 1; Expected: 3

    """
    maxi_profit = 0
    cooldown = None
    for i in range(len(prices)-1):
        if cooldown:
            cooldown = False
            continue  # "After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day)."
        profit = prices[i+1] - prices[i]  # profit (+/0/-) if we buy today and sell tomorrow
        if profit > 0:  # if profit was made
            maxi_profit += profit
            cooldown = True
    return maxi_profit
    """

    # 1) Optimal (DP): TC = O(n); SC = O(1)
    # https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/discuss
