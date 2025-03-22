"""
https://practice.geeksforgeeks.org/problems/-minimum-number-of-coins4426/1
"""


def min_partition(n: int) -> list[int]:
    """"""

    # This question is an easy version of https://www.geeksforgeeks.org/find-minimum-number-of-coins-that-make-a-change
    # (https://leetcode.com/problems/coin-change),
    # which itself is an easy version of https://www.geeksforgeeks.org/coin-change-dp-7
    # (https://leetcode.com/problems/coin-change-ii).

    # 1) Optimal (Greedy: Start from Biggest Coin): TC = O(1); SC = O(1)
    # Simple Intuition: If we want to minimize the number of coins, let's take the coins with the highest value first.
    # V.IMP: Why does greedy approach work here, and when will it not? https://youtu.be/mVg9CfJvayM?t=420 👌
    # SO, GREEDY APPROACH WOULD WORK EVERYWHERE WHERE IN THE DENOMINATIONS, SUM OF *NO* TWO SMALLER DENOMINATIONS (SAME
    # OR DIFFERENT) IS GREATER THAN ANY BIGGER DENOMINATION.

    # O(n):

    """
    coins = (2000, 500, 200, 100, 50, 20, 10, 5, 2, 1)
    i = 0
    ans = []

    while n:
        if n >= (coin := coins[i]):
            n -= coin
            ans.append(coin)
        else:
            i += 1

    return ans
    """

    # O(1):

    coins = (2000, 500, 200, 100, 50, 20, 10, 5, 2, 1)
    i = 0
    ans = []

    while n:
        if freq := n // (coin := coins[i]):  # `freq`: # of coins (of `coin`)
            n -= freq * coin
            ans.extend(coin for _ in range(freq))
        else:
            i += 1

    return ans


# Similar Questions:
# https://leetcode.com/problems/minimum-number-of-operations-to-convert-time
# https://leetcode.com/problems/minimum-operations-to-reduce-an-integer-to-0
