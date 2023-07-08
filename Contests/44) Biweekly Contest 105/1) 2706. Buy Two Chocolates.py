"""
https://leetcode.com/problems/buy-two-chocolates
"""


def buy_choco(prices: list[int], money: int) -> int:
    """"""

    # Sort the array and check if the money is more than or equal to the sum of the two cheapest elements.

    # 1) Sub-Optimal (Sort): TC = O(n*log(n)); SC = O(n)

    """
    return leftover if (leftover := money-sum(sorted(prices)[:2])) >= 0 else money
    """

    # 2) Optimal (Two Smallest Numbers): TC = O(n); SC = O(1)

    min1, i1 = float('inf'), -1
    for i, price in enumerate(prices):  # O(n)
        if price < min1:
            min1, i1 = price, i

    if (leftover1 := money-min1) < 0:  # minor optimization
        return money

    min2 = float('inf')
    for i, price in enumerate(prices):  # O(n)
        if i != i1 and price < min2:
            min2 = price

    return leftover if (leftover := leftover1-min2) >= 0 else money
