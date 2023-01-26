"""
https://practice.geeksforgeeks.org/problems/fractional-knapsack-1587115620/1
"""


class Item:
    def __init__(self, value: int, weight: int):
        self.value = value
        self.weight = weight


def fractional_knapsack(w: int, arr: list[Item], n: int) -> int:
    """"""

    # First of all you should know:
    # https://www.geeksforgeeks.org/difference-between-0-1-knapsack-problem-and-fractional-knapsack-problem

    # 1) Optimal (Greedy: Sort by Decreasing Profit per Unit): TC = O(n*log(n)); SC = O(n) {sorting}
    # GFG Article: https://www.geeksforgeeks.org/fractional-knapsack-problem
    # Abdul Bari Sir: https://youtu.be/oTTzNMHM05I (Gold :))

    max_profit = 0

    for item in sorted(arr, key=lambda itm: itm.value/itm.weight, reverse=True):
        if w >= item.weight:  # take whole item
            w -= item.weight
            max_profit += item.value
        else:  # fraction of item has to be taken
            '''
            if w:
                max_profit += item.value / (item.weight / w)
            '''
            max_profit += (item.value * w) / item.weight
            break

    return max_profit
