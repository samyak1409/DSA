"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock
"""


def max_profit(prices: list[int]) -> int:
    """"""

    # 0) [TLE] Brute-force (Calculating profits for all the combinations): TC = O(n^2); SC = O(1)

    """
    max_profit_ = 0
    for i in range(n := len(prices)):  # considering all the prices in the array one by one as cost price
        for j in range(i+1, n):  # for a particular cost price, all the prices in the next days will be selling prices
            profit = prices[j] - prices[i]  # selling_price - cost_price
            max_profit_ = max(max_profit_, profit)
    return max_profit_
    """

    # 1) Optimal (Kadane's Algo): TC = O(n); SC = O(1)

    # Most intuitive implementation:
    """
    min_price = prices[0]  # init first price as min price
    max_profit_ = 0  # (also, "If you cannot achieve any profit, return 0")

    for i in range(1, len(prices)):  # now start with next price
        price = prices[i]
        # Check if profit can be there:
        if (profit := price-min_price) > 0:
            # If yes, (we can sell the stock) update max_profit if needed:
            max_profit_ = max(max_profit_, profit)
        # If profit is not there, (we do not sell the stock, instead buy on this day if price today is even lesser than
        # our stock bought price):
        else:
            min_price = min(min_price, price)

    return max_profit_
    """

    # We can skip initializing to the first val by initializing to `inf`, everything else remains the same:
    """
    min_price, max_profit_ = float('inf'), 0
    for price in prices:
        if (profit := price-min_price) > 0:
            max_profit_ = max(max_profit_, profit)
        else:
            min_price = min(min_price, price)
    return max_profit_
    """

    # Also, we can just skip the if-else checks as well, as the result would not change if the check was to fail, but
    # this could look a little confusing:
    min_price, max_profit_ = float('inf'), 0
    for price in prices:
        max_profit_ = max(max_profit_, price-min_price)
        min_price = min(min_price, price)
    return max_profit_

    # Another angle to look at this problem:
    # https://leetcode.com/problems/best-time-to-buy-and-sell-stock/solutions/39038/kadane-s-algorithm-since-no-one-has-mentioned-about-this-so-far-in-case-if-interviewer-twists-the-input


# Similar Questions:
# https://leetcode.com/problems/maximum-subarray
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown
# https://leetcode.com/problems/sum-of-beauty-in-the-array
# https://leetcode.com/problems/maximum-difference-between-increasing-elements
