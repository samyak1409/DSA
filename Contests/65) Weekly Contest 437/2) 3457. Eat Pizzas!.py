"""
https://leetcode.com/problems/eat-pizzas
"""


def max_weight(pizzas: list[int]) -> int:
    """"""

    # Note:
    # Days (1-indexed)
    # If odd: Z (max)
    # If even: Y (2nd max)

    # Observation: Since we just need to return the weight, we don't actually need to make the pairs of 4, instead we
    # can just select the `Z` for odd days and `Y` for even days.

    # 1) Optimal (Sort, Greedy): TC = O(n*log(n)); SC = O(n)
    # Observation: We can't greedily choose odd, then even, then odd, and so on, since:
    # Take the test case: [4,2,1,5,2,5,5,4,2,3,2,1]
    # sorted = [5, 5, 5, 4, 4, 3, 2, 2, 2, 2, 1, 1], k = 3
    # Now, for day 1, we'd choose Z, so 5 (index 0 in above arr)
    # For day 2, we'd choose Y, so 5 (index 2, and note that now index 1 is also gone since it's the Z for this day)
    # For day 3, we'd choose Z, so 4 (index 3)
    # Output = 14, but Expected = 15
    # [Caused 1 WA]
    # Correct greedy approach is choosing all odd days first (why? because all those are Zs, i.e. maxes), and then even
    # (viz. 2nd maxes).

    # Sort in order to choose greedily:
    pizzas = sorted(pizzas, reverse=True)  # (avoid modifying input)
    # print(pizzas)  # debug

    k = len(pizzas) // 4  # total no. of days
    odd = (k+1) // 2  # no. of odd days
    even = k - odd  # no. of even days

    # All odds:
    # Greedily choosing odds would be just choosing the max ones:
    ans = sum(pizzas[:odd])

    # All evens:
    # Greedily choosing evens would be choosing the 2nd maxes:
    ans += sum(pizzas[odd+1 : odd+1 + even*2 : 2])

    return ans
