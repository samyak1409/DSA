"""
https://practice.geeksforgeeks.org/problems/fractional-knapsack-1587115620/1
"""


def fractional_knapsack(values: list[int], weights: list[int], capacity: int) -> float:
    """"""

    # First of all you should know:
    # https://www.geeksforgeeks.org/difference-between-0-1-knapsack-problem-and-fractional-knapsack-problem
    # 0/1: https://en.wikipedia.org/wiki/Knapsack_problem
    # Fractional: https://en.wikipedia.org/wiki/Continuous_knapsack_problem

    # 1) Optimal (Greedy: Sort by Decreasing Profit per Unit): TC = O(n*log(n)); SC = O(n) {sorting}
    # GFG Article: https://www.geeksforgeeks.org/fractional-knapsack-problem
    # Abdul Bari Sir: https://youtu.be/oTTzNMHM05I (Gold)

    """
    max_total_val = 0
    for val, wt in sorted(zip(values, weights), key=lambda tup: tup[0]/tup[1], reverse=True):
        if wt <= capacity:  # we can take the whole item
            max_total_val += val
            capacity -= wt
        else:  # we need to take a fraction of item
            max_total_val += capacity * (val / wt)  # `(val / wt)` = unit value
            break
    return max_total_val
    """

    # Or:

    max_total_val = 0
    for val, wt in sorted(zip(values, weights), key=lambda tup: tup[0]/tup[1], reverse=True):
        if capacity == 0:
            break
        # `min(wt, capacity)` == `wt if wt <= capacity else capacity`:
        max_total_val += (x := min(wt, capacity)) * (val / wt)  # `(val / wt)` = unit value
        capacity -= x
    return max_total_val


# Similar Questions:
# https://leetcode.com/problems/maximum-units-on-a-truck
# https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks
