"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock
"""


def max_profit(prices: list[int]) -> int:
    """"""

    # https://leetcode.com/problems/best-time-to-buy-and-sell-stock/solution

    # 0) [TLE] Brute-force (Calculating profits for all the combinations): TC = O(n^2); SC = O(1)

    """
    n = len(prices)
    max_profit_ = 0
    for i in range(n):  # considering all the prices in the array one by one as cost price
        for j in range(i+1, n):  # for a particular cost price, all the prices in the next days will be selling prices
            profit = prices[j] - prices[i]  # selling_price - cost_price
            if profit > max_profit_:
                max_profit_ = profit
    return max_profit_
    """

    # 1) Optimal (Kadane's Algo): TC = O(n); SC = O(1)

    """
    min_price, max_profit_ = float('inf'), 0  # init
    for price in prices:
        if price < min_price:
            min_price = price  # bought stock at a lesser price
            continue  # bought stock on this day, so doesn't make sense selling because profit will obviously be 0
        profit = price - min_price  # selling_price - cost_price
        if profit > max_profit_:
            max_profit_ = profit
    return max_profit_
    """
    min_price, max_profit_ = float('inf'), 0
    for price in prices:
        min_price = min(min_price, price)
        max_profit_ = max(max_profit_, price-min_price)  # `price-min_price` = selling_price-cost_price = current profit
    return max_profit_

    # Another Angle to look at this problem:
    # https://leetcode.com/problems/best-time-to-buy-and-sell-stock/discuss/39038/Kadane's-Algorithm-Since-no-one-has-mentioned-about-this-so-far-:)-(In-case-if-interviewer-twists-the-input)


# Similar Questions:
# https://leetcode.com/problems/maximum-subarray
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown
# https://leetcode.com/problems/sum-of-beauty-in-the-array
# https://leetcode.com/problems/maximum-difference-between-increasing-elements
